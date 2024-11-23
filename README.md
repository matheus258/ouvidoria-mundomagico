# Ouvidoria - Mundo Mágico ✨

Este projeto de ouvidoria permite o gerenciamento e visualização de manifestações de usuários, incluindo reclamações, sugestões e elogios, com a finalidade de melhorar a experiência e atendimento no ambiente do Mundo Mágico.

## Equipe do Projeto

- Vinicius Miguel
- Matheus Marques
- Higor
- Ruan Montenegro
- Juan Wagner
- Roberto
- Gustavo

## Estrutura do Projeto

As manifestações são armazenadas em um banco de dados MySQL e possuem os seguintes parâmetros:

- **Código**: Identificação única de cada manifestação.
- **Descrição**: Detalhes sobre a manifestação.
- **Autor**: Nome do autor da manifestação.
- **Categoria**: Tipo de manifestação, que pode ser uma das seguintes opções:
  - 🛑 Reclamação
  - 💡 Sugestão
  - 👍 Elogio
  - 🚨 Denúncia
  - ℹ️ Informação
  - ❓ Outros

## Tecnologias Utilizadas

O projeto é desenvolvido em:

- **Frontend**: Vue.js 🖥️, usando JavaScript, Bootstrap, e Axios para a comunicação com o backend.
- **Backend**: Python 🐍 com o Flask, usando as bibliotecas `Flask`, `request`, `jsonify`, `CORS` para o gerenciamento das manifestações.
- **Banco de Dados**: MySQL 🗄️, que armazena as manifestações.

---

## Como Iniciar o Projeto

### Frontend (Vue.js)

1. Clone o repositório do frontend:
    ```bash
    git clone https://github.com/matheus258/ouvidoria-mundomagico.git
    cd ouvidoria-mundomagico/front-project
    ```

2. Instale as dependências do projeto usando npm:
    ```bash
    npm install
    ```

3. Inicie o servidor de desenvolvimento Vue.js:
    ```bash
    npm run serve
    ```

Isso abrirá o frontend em `http://localhost:8080`, onde você poderá visualizar e interagir com o formulário de ouvidoria.

O formulário permite que o usuário cadastre informações sobre a manifestação, incluindo:
- **Nome (Autor)**: O nome do autor da manifestação.
- **Tipo (Categoria)**: O tipo da manifestação, como Reclamação, Sugestão ou Elogio.
- **Descrição**: Uma descrição detalhada da manifestação.

### Backend (Flask)

1. Clone o repositório do backend:
    ```bash
    git clone https://github.com/matheus258/ouvidoria-mundomagico.git
    cd ouvidoria-mundomagico/backend
    ```

2. Instale as dependências do backend usando pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Para iniciar o servidor do backend, execute o script `CRUD.py`:
    ```bash
    python CRUD.py
    ```

Isso iniciará o servidor Flask em `http://localhost:5000`, onde o backend estará pronto para interagir com o frontend e o banco de dados.

O backend implementa os seguintes métodos HTTP:
- **GET**: Para listar todas as manifestações.
- **POST**: Para cadastrar novas manifestações.
- **PUT**: Para atualizar manifestações existentes.
- **DELETE**: Para excluir manifestações.

### Banco de Dados

Para criar a tabela necessária no banco de dados **MySQL**, use o seguinte script SQL:

```sql
CREATE DATABASE ouvidoria_final;

USE ouvidoria_final;

CREATE TABLE Manifestacoes (
    codigo INT AUTO_INCREMENT,
    autor VARCHAR(100),
    descricao VARCHAR(300),
    categoria VARCHAR(100),
    PRIMARY KEY(codigo)
);

```
---

Este projeto foi desenvolvido com o apoio e orientação do professor [Daniel Abella](https://github.com/daniel-abella), a quem agradecemos pela contribuição e suporte.
