# Manual Técnico – GameLife Tracker (Versão 0.9)

# 🏗️ 1. Arquitetura Geral do Projeto

Usuário → FastAPI → Validação Pydantic → Banco SQLite via SQLAlchemy

Linguagem principal: Python 3.11+
Framework web/API: FastAPI
Validação de dados: Pydantic
Banco de dados local: SQLite
ORM (modelagem de tabelas): SQLAlchemy
Acesso assíncrono ao banco: Databases

# 🧠 2. Roteiro de Execução da API

O usuário envia um POST para /jogatina ou /tarefa
O FastAPI recebe a requisição e valida os dados com os schemas (Pydantic)
Se os dados estiverem corretos, o main.py constrói uma query de INSERT
Essa query é enviada ao banco SQLite usando database.execute()
Os dados ficam salvos no arquivo gamelife.db
Um GET pode consultar esses dados depois, ou gerar um relatório

# 📦 3. Organização dos Arquivos

| Arquivo           | Função                                        |
|-------------------|-----------------------------------------------|
| `main.py`         | Roteamento da API, lógica principal           |
| `schemas.py`      | Validação e estrutura dos dados da requisição |
| `models.py`       | Estrutura das tabelas do banco                |
| `database.py`     | Conexão com o banco SQLite                    |
| `requirements.txt`| Bibliotecas usadas                            |
| `gamelife.db`     | Banco de dados SQLite local                   |


# 🧩 4. Principais Componentes Técnicos

## FastAPI
    Define rotas com @app.get() e @app.post()
    Usa tipagem forte pra documentação e validação automática
    Gera docs automáticas em /docs

## Pydantic
    Usado com BaseModel
    Fornece validação automática e conversão de tipos
    Impede que dados inválidos cheguem ao banco

## SQLAlchemy
    Cria tabelas com Python
    Define colunas, tipos, chaves primárias
    Trabalha junto com o engine SQLite

## Databases
    Permite executar comandos assíncronos no banco (await database.execute(...))
    Usado pra INSERT, SELECT, etc.

# 🧾 5. Endpoints Criados

##   Rota	                Método	            Função
     /	                    GET	                Teste da API (retorna mensagem)
     /jogatina	            POST	            Registra uma sessão de jogo
     /jogatina	            GET	                Lista todas as jogatinas salvas
     /tarefa	            POST	            Registra uma tarefa ou estudo feito
     /tarefa	            GET	                Lista todas as tarefas
     /relatorio/semana	    GET                 Gera relatório da semana atual (tempo jogado, estudado, humores, etc)


# 🧮 6. Lógica do Relatório

+Calcula a semana atual: segunda até domingo
+Busca jogatinas e tarefas que ocorreram nesse intervalo
+Usa sum() pra somar os tempos
+Usa Counter() pra contar frequência de humores e dias ativos

# 📌 7. Como rodar o projeto

python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
uvicorn backend.main:app --reload
Acesse a documentação: [http://localhost:8000/docs](http://localhost:8000/docs)