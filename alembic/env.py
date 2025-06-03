"""
from
{"logging.config": "usado para configurar o logging do Alembic"
    "sqlalchemy": "usado para criar o motor de conexão com o banco de dados",
    "alembic": "usado para gerenciar migrações de banco de dados"
    "sqlalchemy.ext.asyncio": "usado para criar um motor de conexão assíncrono com o banco de dados",}
import
{"fileConfig": "usado para carregar a configuração de logging do Alembic",
    "pool": "usado para gerenciar conexões com o banco de dados",
    "create_engine": "usado para criar o motor de conexão com o banco de dados"
    "AsyncEngine": "objeto retornado pelo create_async_engine para conexões assíncronas",
    "context": "usado para gerenciar o contexto de migração do Alembic",
    "os": "usado para manipular caminhos e variáveis de ambiente python",
    "sys": "usado para manipular o caminho do sistema python"
    "asyncio": "usado para executar funções assíncronas"}
"""
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import pool

from alembic import context

import os
import sys
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from workout.app.models.base import BaseModel  # aqui a Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = BaseModel.metadata  # metadata alvo para as migrações

def run_migrations_offline():
    #Executa as migrações em modo offline (gera SQL sem aplicar).
    url = config.get_main_option("sqlalchemy.url")
    # Cria o motor de conexão com o banco de dados
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    # Executa as migrações offline
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    #Executa as migrações em modo online com SQLAlchemy async.
    connectable: AsyncEngine = create_async_engine(
        # Cria o motor de conexão assíncrono com o banco de dados
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )
    # Configura o contexto de migração com o motor de conexão
    async with connectable.connect() as connection:
        await connection.run_sync(
            lambda sync_connection: context.configure(
                connection=sync_connection,
                target_metadata=target_metadata,
            )
        )

        async with connection.begin():
            await connection.run_sync(context.run_migrations)

    await connectable.dispose()


def run_migrations_online():
    #Executa migrações online com suporte a async.
    asyncio.run(run_async_migrations())


# Decide se executa modo offline ou online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

# proximo passo almebic.ini