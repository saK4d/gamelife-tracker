# database.py - Configuração da conexão com o banco de dados SQLite

from databases import Database  # Importa a biblioteca 'databases' para manipulação assíncrona do banco
from sqlalchemy import create_engine  # Usado para criar o engine do SQLAlchemy
from backend.models import metadata  # Importa o metadata com a estrutura das tabelas definidas em models.py

# Define a URL do banco de dados SQLite (arquivo local chamado gamelife.db)
DATABASE_URL = "sqlite:///./gamelife.db"

# Cria o objeto de banco assíncrono, usado para executar queries async com await
database = Database(DATABASE_URL)

# Cria o engine SQLAlchemy para aplicar a estrutura das tabelas ao banco físico
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)  # Cria todas as tabelas no banco se ainda não existirem