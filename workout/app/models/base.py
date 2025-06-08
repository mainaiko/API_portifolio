"""
from
{"sqlalchemy" : "usado para definir modelos e colunas do banco de dados",
    "sqlalchemy.orm": "usado para criar uma classe base declarativa para os modelos"}
import
{"declarative_base": "usado para criar uma classe base declarativa para os modelos"}
"""
from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base

# Classe base declarativa em uma variavel
Base = declarative_base()

# Classe base para os models
class BaseModel(Base):
    __abstract__ = True 
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
