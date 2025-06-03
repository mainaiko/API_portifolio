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

# Defino os modelos de dados para o Aluno usando Pydantic
class AlunoBase(BaseModel):
    nome: str
    idade: int
    email: EmailStr
    data_nascimento: date
    telefone: str

# Defino o modelo de criação do Aluno, que herda de AlunoBase
class AlunoCreate(AlunoBase):
    pass

# Defino o modelo de atualização do Aluno, que herda de AlunoBase
class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    email: Optional[EmailStr] = None

# Defino o modelo de saída do Aluno, que herda de AlunoBase e inclui campos adicionais
class AlunoOut(AlunoBase):
    id: int
    data_nascimento: date
    telefone: str
    criado_em: datetime
    atualizado_em: Optional[datetime] = None

    # Configuração para permitir que o Pydantic converta modelos ORM em modelos Pydantic
    class Config:
        orm_mode = True

# Proximo passo definir o alembic para criar as tabelas no banco de dados