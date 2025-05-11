# Estudo sobre Python e Flask no Backend

Este documento tem como objetivo fornecer uma visão geral sobre **Python e Flask aplicados ao desenvolvimento backend**, servindo como material de apoio para os integrantes do grupo no contexto da disciplina.

> ⚠️ O resumo serve como ponto de partida para aprofundar os estudos conforme o projeto avança, portanto, pode ser modificado.

---

## 🐍 O que é o Python?

**Python** é uma linguagem de programação de alto nível, interpretada e de tipagem dinâmica. É amplamente utilizada por sua sintaxe simples e legibilidade, sendo aplicada em diversas áreas como ciência de dados, automação, inteligência artificial e desenvolvimento web.

No contexto de **backend**, Python se destaca por sua ampla gama de bibliotecas e frameworks que facilitam a criação de APIs e aplicações web escaláveis.

---

## 🌐 O que é o Flask?

**Flask** é um microframework web para Python. Ele permite a criação rápida e simples de servidores web e APIs RESTful, oferecendo flexibilidade e controle total sobre a estrutura da aplicação.

É ideal para projetos pequenos a médios ou para quando o desenvolvedor deseja ter mais controle sobre os componentes do backend.

---

## 🔧 Como funciona o Flask?

- O Flask escuta requisições HTTP (como GET e POST) e responde com dados (normalmente JSON ou HTML).
- As rotas são criadas com decoradores (`@app.route`) que associam URLs a funções Python.
- O framework pode usar **Jinja2** para renderizar páginas HTML dinamicamente.
- Pode ser facilmente integrado com bancos de dados (como SQLite, PostgreSQL) e bibliotecas externas.

---

## 🧱 Principais Recursos do Flask

- ✅ Criação de rotas para diferentes URLs (endpoints)
- ✅ Suporte a templates HTML com **Jinja2**
- ✅ Suporte a requisições HTTP (GET, POST, PUT, DELETE, etc.)
- ✅ Integração com bancos de dados via ORM (como SQLAlchemy)
- ✅ Extensível com plugins (login, CORS, validações, etc.)
- ✅ Ideal para criação de **APIs RESTful**

---

## 📚 Referencias

-> <https://wiki.python.org/moin/BeginnersGuide>
-> 
-> 

## 🗂️ Estrutura básica de um projeto Flask

```text
meu_app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── requirements.txt