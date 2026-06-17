# Ulysses Veículos - Locadora de Veículos

Sistema web para locação de veículos desenvolvido com Django.

## Tecnologias

- **Python 3.10+** / **Django 4.1**
- **SQLite** (banco de dados)
- **Bootstrap 5** (interface)
- **jQuery** + **DataTables** + **OwlCarousel**
- **django-braces** / **django-crispy-forms**

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
pip install django-braces django-crispy-forms requests

# 3. Rodar o servidor
python locadora\manage.py runserver
```

Acesse em `http://localhost:8000`

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

## Grupo

Amanda, Déborah, Gabriela e Vinícius — IFMA
