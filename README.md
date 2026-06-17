# 💰 Finance Manager

Sistema desktop de gerenciamento financeiro desenvolvido em **Python** utilizando **PySide6**, com banco de dados **SQLite** e arquitetura organizada em camadas.

O objetivo do projeto é criar uma aplicação moderna para controle financeiro pessoal, permitindo cadastro de receitas e despesas, acompanhamento através de dashboard, gráficos e geração de insights financeiros.

---

## 🚀 Funcionalidades

### 📊 Dashboard Financeiro

* Visualização do saldo atual
* Total de receitas
* Total de despesas
* Insights financeiros automáticos
* Atualização dos valores conforme novos lançamentos

---

### 💰 Controle de Rendas

* Cadastro de receitas

* Tipos de renda personalizados:

  * Salário
  * Extra
  * Saldo Restante Anterior
  * Décimo Terceiro
  * PIS/PASEP
  * Outros

* Forma de pagamento:

  * PIX
  * Cartão de Crédito
  * Dinheiro
  * Outros

* Validação de valores

* Edição de registros

* Exclusão de registros

* Atualização automática da tabela

---

### 📈 Gráficos

* Despesas por categoria
* Comparativo entre receitas e despesas

Visualização criada utilizando integração com Matplotlib.

---

### 💡 Insights Financeiros

O sistema analisa os dados cadastrados e apresenta informações como:

* Controle de gastos
* Percentual de despesas sobre a renda
* Maior categoria de gasto
* Valor disponível restante
* Alertas financeiros

---

## 🛠 Tecnologias utilizadas

* Python 3
* PySide6
* SQLite
* Matplotlib
* Git
* GitHub

---

## 🏗 Arquitetura do Projeto

O projeto segue uma organização separada por responsabilidades:

```
finance_manager/

│
├── app/
│
│   ├── database/
│   │   ├── database.py
│   │   └── repository.py
│   │
│   ├── models/
│   │   └── transaction.py
│   │
│   ├── services/
│   │   ├── finance_service.py
│   │   ├── insights_service.py
│   │   └── insights_engine.py
│   │
│   └── ui/
│       │
│       ├── pages/
│       │   ├── income_page.py
│       │   └── ...
│       │
│       ├── widgets/
│       │   ├── dashboard_widget.py
│       │   ├── financial_card.py
│       │   ├── income_table.py
│       │   └── charts_widget.py
│       │
│       └── theme.qss
│
├── main.py
│
└── README.md
```

---

## 📚 Conceitos aplicados

Durante o desenvolvimento foram utilizados conceitos importantes:

* Programação orientada a objetos
* Separação de responsabilidades
* Arquitetura em camadas
* Componentização de interface
* Signals e Slots do PySide6
* Manipulação de banco SQLite
* Persistência de dados
* Estilização com QSS
* Controle de versão com Git

---

## 🎨 Interface

A interface utiliza:

* Tema personalizado em QSS
* Componentes reutilizáveis
* Cards financeiros
* Tabelas estilizadas
* Layout organizado
* Experiência semelhante a aplicações comerciais

---

## ▶️ Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/MaiconDante/finance_manager.git
```

Entre na pasta:

```bash
cd finance_manager
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

---

## 📦 Banco de Dados

O projeto utiliza SQLite.

O banco é criado automaticamente na primeira execução:

```
finance.db
```

---

## 🔄 Próximas melhorias

Planejamento de evolução do projeto:

* Cadastro de despesas fixas
* Cadastro de despesas variáveis
* Categorias financeiras personalizadas
* Relatórios financeiros
* Exportação de dados
* Backup do banco
* Melhorias de UX/UI
* Sistema de login de usuários

---

## 📝 Histórico de desenvolvimento

Projeto desenvolvido com foco em aprendizado e evolução prática utilizando Python para criação de aplicações desktop profissionais.

O desenvolvimento segue boas práticas:

* Commits organizados
* Evolução incremental
* Código separado por responsabilidades
* Melhorias contínuas na interface e arquitetura

---

## 👨‍💻 Autor

**MaiconDante**

Projeto desenvolvido para estudo e prática de desenvolvimento desktop com Python.

---

⭐ Se este projeto foi útil, considere deixar uma estrela no repositório.
