# Guia de Contribuição - Code Quiz

Obrigado por considerar contribuir com o Code Quiz! Este documento fornece instruções claras para configurar o ambiente de desenvolvimento e contribuir com o projeto.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.11+** ([Download aqui](https://www.python.org/downloads/))
- **pip** (geralmente vem com Python)
- **Git** ([Download aqui](https://git-scm.com/downloads))
- **Google Chrome** (para testes E2E)
- **ChromeDriver** (para Selenium - [Download aqui](https://chromedriver.chromium.org/downloads))

## 🚀 Configuração do Ambiente

### 1. Clone o Repositório

```bash
git clone https://github.com/Bernalencouto/Code_Quiz.git
cd Code_Quiz
```

### 2. Crie um Ambiente Virtual

**No macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**No Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados

```bash
python manage.py migrate
```

Este comando irá criar o banco de dados e carregar automaticamente os dados iniciais através das migrações.

### 5. Crie um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### 6. Execute o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

Acesse o projeto em: `http://127.0.0.1:8000/`

## 🧪 Executando os Testes

### Testes Unitários

```bash
pytest
```

### Testes E2E (End-to-End)

**Importante:** Certifique-se de que o servidor está rodando antes de executar os testes E2E.

Em um terminal:
```bash
python manage.py runserver
```

Em outro terminal:
```bash
python teste_e2e.py
```

Ou com mais detalhes:
```bash
python teste_e2e.py -v
```

**Nota:** Para os testes E2E funcionarem, você precisa ter um usuário chamado `testeE2E` com senha `123teste123`. Você pode criá-lo manualmente ou através do admin do Django.

## 📁 Estrutura do Projeto

```
Code_Quiz/
├── manage.py                 # Script principal do Django
├── db.sqlite3               # Banco de dados SQLite
├── requirements.txt         # Dependências do projeto
├── pytest.ini              # Configuração do pytest
├── teste_e2e.py            # Testes End-to-End
├── project/                # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── setup/                  # App principal
    ├── models.py           # Modelos do banco
    ├── views.py            # Views/Controllers
    ├── urls.py             # Rotas da aplicação
    ├── admin.py            # Configuração do admin
    ├── templates/          # Templates HTML
    ├── static/             # Arquivos estáticos (CSS)
    ├── fixtures/           # Dados iniciais
    └── migrations/         # Migrações do banco
```

## 🤝 Como Contribuir

### 1. Crie uma Branch

```bash
git checkout -b feature/sua-feature
```

ou

```bash
git checkout -b fix/seu-fix
```

### 2. Faça suas Alterações

- Escreva código limpo e bem documentado
- Siga as convenções do Python (PEP 8)
- Adicione testes para novas funcionalidades
- Certifique-se de que todos os testes passam

### 3. Commit suas Alterações

```bash
git add .
git commit -m "feat: descrição clara da sua alteração"
```

**Convenções de commit:**
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` alterações na documentação
- `style:` formatação, ponto e vírgula faltando, etc
- `refactor:` refatoração de código
- `test:` adição ou modificação de testes
- `chore:` atualização de dependências, etc

### 4. Push para o GitHub

```bash
git push origin feature/sua-feature
```

### 5. Abra um Pull Request

- Vá para o repositório no GitHub
- Clique em "Pull Requests" → "New Pull Request"
- Selecione sua branch
- Descreva suas alterações de forma clara
- Aguarde a revisão

## 🎯 Diretrizes de Código

### Python/Django

- Siga a [PEP 8](https://peps.python.org/pep-0008/)
- Use nomes descritivos para variáveis e funções
- Mantenha funções pequenas e focadas
- Documente funções complexas

### HTML/CSS

- Use indentação de 4 espaços
- Mantenha o código organizado e legível
- Use classes CSS semânticas

### Testes

- Escreva testes para novas funcionalidades
- Mantenha a cobertura de testes alta
- Teste casos de erro e edge cases

## 🐛 Reportando Bugs

Ao reportar bugs, inclua:

1. **Descrição clara** do problema
2. **Passos para reproduzir** o bug
3. **Comportamento esperado** vs **comportamento atual**
4. **Screenshots** (se aplicável)
5. **Ambiente** (SO, versão do Python, navegador)

## 💡 Sugestões de Funcionalidades

Ao sugerir novas funcionalidades:

1. Explique o **problema** que a funcionalidade resolve
2. Descreva a **solução proposta**
3. Considere **alternativas**
4. Adicione **contexto adicional** se necessário

## 📚 Recursos Úteis

- [Documentação do Django](https://docs.djangoproject.com/)
- [Python PEP 8](https://peps.python.org/pep-0008/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [pytest Documentation](https://docs.pytest.org/)

## ❓ Precisa de Ajuda?

- Abra uma [Issue](https://github.com/gabrielpferreira15/Code_Quiz/issues)
- Entre em contato com os mantenedores

**Obrigado por contribuir! 🎉**
