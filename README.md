# Ulysses Veículos - Locadora de Veículos

Sistema web para locação de veículos desenvolvido com Django.

## Sobre o projeto

Este é um projeto prático desenvolvido em 2023 no Instituto Federal do Maranhão
(IFMA) – Campus Monte Castelo, em São Luís.

## Tecnologias

- **Python 3.10+** / **Django 4.1**
- **SQLite** (banco de dados)
- **Bootstrap 5** (interface)
- **jQuery** + **DataTables** + **OwlCarousel**
- **django-braces** / **django-crispy-forms**
- **crispy-bootstrap4**

## Funcionalidades

- Cadastro e login de usuários
- Cadastro, edição, exclusão e listagem de veículos
- Controle de aluguéis (alugados/devolvidos)
- Perfil do usuário (nome, CPF, RG, celular, endereço)
- Busca por cidade
- Páginas institucionais (sobre, serviços, contato, política, suporte)
- Painel administrativo Django

## Como rodar

```powershell
# 1. Criar e ativar ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Instalar dependências
pip install django-braces django-crispy-forms crispy-bootstrap4 requests

# 3. Aplicar as migrações do banco de dados
python locadora\manage.py migrate

# 4. Rodar o servidor
python locadora\manage.py runserver
```

Acesse em `http://localhost:8000`

## Acesso administrativo

Acesse `http://localhost:8000/admin/` com:

- **Usuário:** `admin`
- **Senha:** `12345678`

## Estrutura

```
LocadoraDeVeiculos/
├── locadora/
│   ├── cadastros/       # CRUD de veículos e aluguéis
│   ├── usuarios/        # Autenticação e perfil
│   ├── paginas/         # Páginas estáticas do site
│   ├── locadora/        # Configuração do Django
│   ├── static/          # CSS, JS, imagens
│   └── db.sqlite3       # Banco de dados
├── venv/                # Ambiente virtual
└── README.md
```
