import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'catalogo.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Obra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    nota = db.Column(db.Text, nullable=False)
    comentario = db.Column(db.Text, nullable=True)
    url_capa = db.Column(db.String(450), nullable=True)

    def __repr__(self):
        return f'<Obra {self.titulo}>'
    

@app.route('/')
def index():
    """Página principal que exibe as obras com filtros."""

    tipos_unicos = db.session.query(Obra.tipo).distinct().order_by(Obra.tipo).all()
    categorias_unicas = db.session.query(Obra.categoria).distinct().order_by(Obra.categoria).all()

    tipos = [t[0] for t in tipos_unicos]
    categorias = [c[0] for c in categorias_unicas]

    filtro_tipo = request.args.get('tipo', '')
    filtro_categoria = request.args.get('categoria', '')

    query = Obra.query

    if filtro_tipo:
        query = query.filter(Obra.tipo == filtro_tipo)
    
    if filtro_categoria:
        query = query.filter(Obra.categoria == filtro_categoria)

    obras = query.order_by(Obra.id.desc()).all()

    return render_template('index.html', 
                           obras=obras, 
                           tipos=tipos, 
                           categorias=categorias,
                           filtro_tipo_ativo=filtro_tipo,
                           filtro_categoria_ativo=filtro_categoria)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    """Página para adicionar uma nova obra ao catálogo."""
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        categoria = request.form['categoria']
        nota = request.form['nota']
        comentario = request.form['comentario']
        url_capa = request.form['url_capa']

        if not titulo or not tipo or not categoria or not nota:
            flash('Por favor, preencha todos os campos obrigatórios.', 'erro')
            return redirect(url_for('adicionar'))
        
        nova_obra = Obra(
            titulo=titulo, 
            tipo=tipo, 
            categoria=categoria, 
            nota=nota, 
            comentario=comentario,
            url_capa=url_capa
        )
        db.session.add(nova_obra)
        db.session.commit()

        flash('Obra adicionada com sucesso!', 'sucesso')
        return redirect(url_for('index'))
    
    return render_template('adicionar.html')

@app.route('/editar/<int:obra_id>', methods=['GET', 'POST'])
def editar(obra_id):
    """Página para editar uma obra existente no catálogo."""
    obra = Obra.query.get_or_404(obra_id)

    if request.method == 'POST':
        obra.titulo = request.form['titulo']
        obra.tipo = request.form['tipo']
        obra.categoria = request.form['categoria']
        obra.nota = request.form['nota']
        obra.comentario = request.form['comentario']
        obra.url_capa = request.form['url_capa']

        db.session.commit()
        flash('Obra atulizada com sucesso!', 'sucesso')
        return redirect(url_for('index'))
    
    return render_template('editar.html', obra=obra)

@app.route('/deletar/<int:obra_id>', methods=['POST'])
def deletar(obra_id):
    """Rota para deletar uma obra."""
    obra_a_deletar = Obra.query.get_or_404(obra_id)
    
    try:
        db.session.delete(obra_a_deletar)
        db.session.commit()
        flash('Obra deletada com sucesso!', 'sucesso')
    except:
        db.session.rollback()
        flash('Erro ao deletar a obra.', 'erro')

    return redirect(url_for('index'))

@app.route('/estatisticas')
def estatisticas():
    """Página que exibe estatísticas sobre o catálogo."""
    
    total_obras = Obra.query.count()

    nota_media_raw = db.session.query(func.avg(Obra.nota)).scalar()
    nota_media = round(nota_media_raw, 2) if nota_media_raw else 0

    contagem_por_categoria = db.session.query(
        Obra.categoria, 
        func.count(Obra.id)
    ).group_by(Obra.categoria).order_by(Obra.categoria).all()

    contagem_por_tipo = db.session.query(
        Obra.tipo, 
        func.count(Obra.id)
    ).group_by(Obra.tipo).order_by(Obra.tipo).all()

    return render_template('estatisticas.html', 
                           total_obras=total_obras,
                           nota_media=nota_media,
                           contagem_por_categoria=contagem_por_categoria,
                           contagem_por_tipo=contagem_por_tipo)

if __name__ == '__main__':
    with app.app_context():
        instance_path = os.path.join(basedir, 'instance')
        if not os.path.exists(instance_path):
            os.makedirs(instance_path)
        db.create_all()
    app.run(debug=True)