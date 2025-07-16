# 📊 Catálogo Pessoal de Mídia com Python & Flask

Este projeto é uma aplicação web completa e interativa para catalogar e gerenciar uma coleção pessoal de mídias (livros, filmes, séries, etc.). Construído com **Python** e **Flask**, ele demonstra um ciclo **CRUD** (Create, Read, Update, Delete) completo, persistência de dados com **SQLite** e **SQLAlchemy**, e uma interface dinâmica e moderna com **Jinja2**, **CSS Flexbox** e **Chart.js**.

Este projeto é uma excelente oportunidade para aprofundar conhecimentos e aplicar conceitos em:

* **Python & Flask:**
    * **Estrutura de Aplicação:** Organização de um projeto Flask com rotas, templates e arquivos estáticos.
    * **Roteamento Dinâmico:** Criação de rotas que aceitam parâmetros, como `/editar/<int:obra_id>`.
    * **Manipulação de Requisições:** Processamento de formulários com os métodos `GET` (para filtros) e `POST` (para criação/edição), utilizando `request.form` e `request.args`.
    * **Mensagens de Feedback:** Uso do sistema de "flash messages" do Flask para uma melhor experiência do usuário (UX).

* **Banco de Dados (SQLAlchemy & SQLite):**
    * **Modelagem ORM:** Definição de tabelas do banco de dados como classes Python.
    * **CRUD Completo:** Implementação das quatro operações essenciais: `db.session.add()` (Create), `Obra.query.all()` (Read), atualização de atributos de objeto (Update) e `db.session.delete()` (Delete).
    * **Consultas Avançadas:**
        * **Filtros Dinâmicos:** Construção de queries que se adaptam aos parâmetros enviados pelo usuário (`.filter()`).
        * **Busca de Dados Únicos:** Uso de `.distinct()` para popular os menus de filtro de forma inteligente.
        * **Agregação de Dados:** Cálculo de estatísticas com `func.avg()` (média) e `func.count()` (contagem) combinados com `.group_by()`.

* **Frontend Dinâmico (HTML, CSS, Jinja2):**
    * **Herança de Templates:** Estruturação de um layout base com `{% extends %}` e `{% block %}`.
    * **Renderização Condicional:** Uso de lógica `{% if %}` e `{% for %}` para exibir dados, incluindo a pré-seleção de opções em formulários.
    * **Layout com Flexbox:** Criação de um grid de "cards" responsivo e moderno para uma visualização atraente.
    * **Estilização Profissional:** Aplicação de uma paleta de cores consistente através de variáveis CSS e uso de fontes customizadas (Google Fonts).

* **Arquitetura e Boas Práticas:**
    * **Separação de Responsabilidades:** Divisão clara entre a lógica do back-end (Python), a estrutura (HTML) e a apresentação (CSS).
    * **Padrão Post/Redirect/Get:** Utilização de redirecionamentos após submissões de formulários `POST` para evitar reenvios acidentais.
    * **Ambiente Virtual:** Isolamento das dependências do projeto para garantir a reprodutibilidade.

-----

## ✨ Funcionalidades

* **CRUD Completo:**
    * **C (Create):** Adiciona novas obras (livros, filmes, etc.) ao catálogo através de um formulário completo.
    * **R (Read):** Exibe a coleção completa em um layout de cards visualmente agradável.
    * **U (Update):** Permite a edição de todos os detalhes de uma obra já cadastrada.
    * **D (Delete):** Permite a remoção de obras do catálogo com uma confirmação.
* **Upload de Capas:** Campo para adicionar a URL da capa da obra, que é exibida no card.
* **Filtros Dinâmicos:** Filtra o catálogo em tempo real por "Tipo" (ex: Livro, Filme) e "Categoria" (ex: Fantasia, Drama).
* **Página de Estatísticas:**
    * Exibe o número total de obras cadastradas.
    * Calcula e mostra a nota média de todas as obras.
    * Apresenta tabelas com a contagem de obras por categoria e por tipo.
* **Interface Moderna:** Design limpo e organizado, com uma paleta de cores roxa e lilás, fontes estilizadas e feedback visual para o usuário.

-----

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Flask:** Microframework web para o back-end.
* **SQLAlchemy:** ORM para interação com o banco de dados.
* **Jinja2:** Template engine para renderização de HTML dinâmico.
* **SQLite:** Banco de dados relacional que não requer servidor.
* **HTML5:** Para a estrutura das páginas.
* **CSS3:** Para o design e layout (com Flexbox e Variáveis CSS).

-----

## 🚀 Como Executar Localmente

Para rodar este projeto em sua máquina, você precisará ter o **Python 3** instalado.

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/MaryAylla/personal-catalogue.git](https://github.com/MaryAylla/personal-catalogue.git)
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd nome-da-pasta-do-projeto
    ```

3.  **Crie e ative um ambiente virtual:**
    * No Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Instale as dependências:**
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    O banco de dados (`catalogo.db`) será criado automaticamente na pasta `instance/` na primeira vez que a aplicação for executada.

6.  **Acesse o Projeto:**
    * Abra seu navegador e navegue até a URL:
        ```
        [http://127.0.0.1:5000](http://127.0.0.1:5000)
        ```
