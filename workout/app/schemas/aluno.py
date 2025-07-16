"""
from
{"pydantic": "usado para criar modelos de dados com validação",
    "typing": "usado para tipos opcionais e data/hora",
    "datetime": "usado para manipulação de datas e horas"}
import
{"BaseModel": "classe base para modelos de dados",
    "EmailStr": "tipo de dado para validar emails",
    "Optional": "usado para campos opcionais",
    "date": "tipo de dado para datas",
    "datetime": "tipo de dado para data e hora"}
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

# Modelos de dados para o Aluno
class AlunoBase(BaseModel):
    nome: str
    idade: int
    email: EmailStr
    data_nascimento: date
    telefone: str

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    email: Optional[EmailStr] = None

class AlunoOut(AlunoBase):
    id: int
    data_nascimento: date
    telefone: str
    criado_em: datetime
    atualizado_em: Optional[datetime] = None

    # Configuração para permitir que modelos ORM sejam convertidos para Pydantic
    class Config:
        from_attributes = True