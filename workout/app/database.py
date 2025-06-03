"""
from
{"slqalchemy.ext.asyncio": "usado para trabalhar com SQLAlchemy de forma assíncrona",
    "sqlalchemy.orm": "usado para criar sessões e gerenciar transações com o banco de dados",
    "os": "usado para acessar variáveis de ambiente"}
import
{"AsyncSession": "classe para criar sessões assíncronas com o banco de dados",
    "create_async_engine": "função para criar um motor assíncrono de conexão com o banco de dados",
    "sessionmaker": "função para criar uma fábrica de sessões",
    "os": "módulo python para acessar variáveis de ambiente"}
"""
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# Pega a URL do banco de dados da variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:senha123@localhost:5433/meubanco")
# Instancio a create_async_engine com a URL do banco de dados
# echo=True para exibir as consultas SQL no console para debug
engine = create_async_engine(DATABASE_URL, echo=True)

# Cria a sessão assíncrona
AsyncSessionLocal = sessionmaker(# Sessionmaker é uma fábrica de sessões que retorna uma nova sessão para cada chamada
    bind=engine,# Conecta a variavel engine ao sessionmaker
    class_=AsyncSession, # Define a classe de sessão como AsyncSession ou assincrona
    expire_on_commit=False # Não expira os objetos após o commit, por ser assincrono assim preciso manter os objetos na sessão
)

#forneco uma função para obter injetar a sessão no endpoint na fastapi
async def get_db():
    async with AsyncSessionLocal() as session: #a sessao ira se fechar automaticamente ao sair do bloco
        yield session

# proximo passo models