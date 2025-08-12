# 📚 BookStore APP

Aplicativo web desenvolvido com Django para gerenciamento de uma livraria. Permite cadastro, visualização e manipulação de livros via API.

## 🚀 Funcionalidades

- CRUD de livros
- Integração com banco de dados SQLite
- Estrutura modular com Django
- API RESTful para consumo externo

## 🛠 Tecnologias utilizadas

- Python 3.11+
- Django
- SQLite
- Poetry (gerenciador de dependências)

## 📁 Estrutura do projeto

- `bookstore/`: Configurações principais do projeto Django
- `api/`: Aplicação responsável pela lógica da livraria
- `manage.py`: Script de gerenciamento do Django
- `db.sqlite3`: Banco de dados local
- `.github/workflows/`: Configuração de CI com GitHub Actions

## ⚙️ Como rodar o projeto

```bash
# Instale as dependências
poetry install

# Ative o ambiente virtual
poetry shell

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
