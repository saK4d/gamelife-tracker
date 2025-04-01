# models.py - Define a estrutura das tabelas do banco de dados

from sqlalchemy import Table, Column, Integer, String, Date, MetaData  # Importa componentes para definir tabelas e tipos

metadata = MetaData()  # Objeto que armazena o esquema (estrutura) do banco de dados

# Define a tabela "jogatina" com seus respectivos campos (colunas)
jogatina = Table(
    "jogatina",  # Nome da tabela
    metadata,  # Esquema ao qual a tabela pertence
    Column("id", Integer, primary_key=True),  # ID único da jogatina
    Column("jogo", String, nullable=False),  # Nome do jogo (obrigatório)
    Column("duracao_em_minutos", Integer),  # Duração da sessão de jogo
    Column("humor_antes", String),  # Estado emocional antes de jogar
    Column("humor_depois", String),  # Estado emocional depois de jogar
    Column("data", Date)  # Data da jogatina
)

# Define a tabela "tarefa" com seus respectivos campos (colunas)
tarefa = Table(
    "tarefa",  # Nome da tabela
    metadata,  # Esquema ao qual a tabela pertence
    Column("id", Integer, primary_key=True),  # ID único da tarefa
    Column("tipo", String, nullable=False),  # Tipo da tarefa ou estudo realizado
    Column("duracao_em_minutos", Integer),  # Duração da tarefa
    Column("produtividade", String),  # Qualidade da produtividade (baixa, média, alta)
    Column("data", Date)  # Data da tarefa
)