"""
from
{"sqlalchemy" : "usado para definir modelos e colunas do banco de dados"}
import
{"Column": "usado para definir colunas do modelo",
    "Integer": "usado para definir colunas do tipo inteiro",
    "String": "usado para definir colunas do tipo string",
    "Date": "usado para definir colunas do tipo data",
    "Boolean": "usado para definir colunas do tipo booleano"}
"""
from sqlalchemy import Column, Integer, String, Date, Boolean
from .base import BaseModel  

# Modelo Aluno que herda de BaseModel e representa a tabela "alunos" no banco de dados
class Aluno(BaseModel):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    telefone = Column(String, unique=True, nullable=False)
    ativo = Column(Boolean, default=True)
