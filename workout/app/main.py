"""
from
{"fastapi": "usado para criar a aplicação web assincrona",
"sqlalchemy.ext.asyncio": "usado para trabalhar com SQLAlchemy de forma assíncrona",
"sqlalchemy.future": "usado para executar consultas assíncronas no banco de dados",
}
import
{"FastAPI": "classe principal da aplicação FastAPI",
"Depends": "usado para injetar dependências nos endpoints via get_db criado na database.py", 
"HTTPException": "usado para lançar exceções HTTP",
"AsyncSession": "classe para criar sessões assíncronas com o banco de dados",
"select": "função para criar consultas SQL assíncronas"}
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Imports de arquivos locais necessarios

from app import database
from app.models import aluno as models
from app.schemas import aluno as schemas 

# Inicio do projeto FastAPI
app = FastAPI()

# Endpoint para criar aluno
@app.post("/alunos/", response_model=schemas.AlunoOut)# Post para criar um novo aluno, utilizo o pydantic AlunoOut para retornar o aluno criado
async def criar_aluno(aluno: schemas.AlunoCreate, db: AsyncSession = Depends(database.get_db)):# Funçao assíncrona para criar um novo aluno, recebe o modelo AlunoCreate e a sessão do banco de dados
    novo_aluno = models.Aluno(nome=aluno.nome, email=aluno.email)# Cria uma nova instância "novo_aluno" do models Aluno com os dados recebidos pelo shemas aluno
    db.add(novo_aluno) # Adiciona o novo aluno à sessão do banco de dados
    await db.commit() # Comita as mudanças na sessão do banco de dados
    await db.refresh(novo_aluno) # Atualiza o objeto "novo_aluno" com os dados do banco de dados após o commit
    return novo_aluno # Retorna o novo aluno criado em formato de resposta JSON

# Listar alunos
@app.get("/alunos/", response_model=list[schemas.AlunoOut])
async def listar_alunos(db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Aluno))
    alunos = result.scalars().all()
    return alunos

# Buscar um aluno específico por ID
@app.get("/alunos/{aluno_id}", response_model=schemas.AlunoOut)
async def buscar_aluno(aluno_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Aluno).where(models.Aluno.id == aluno_id))
    aluno = result.scalar_one_or_none()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# Atualizar aluno
@app.patch("/alunos/{aluno_id}", response_model=schemas.AlunoOut)
async def atualizar_aluno(aluno_id: int, aluno: schemas.AlunoUpdate, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Aluno).where(models.Aluno.id == aluno_id))
    aluno_db = result.scalar_one_or_none()
    if not aluno_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    dados = aluno.dict(exclude_unset=True)
    for chave, valor in dados.items():
        setattr(aluno_db, chave, valor)
    if aluno.email is not None:
        aluno_db.email = aluno.email

    await db.commit()
    await db.refresh(aluno_db)
    return aluno_db

# Deletar aluno
@app.delete("/alunos/{aluno_id}", status_code=204)
async def deletar_aluno(aluno_id: int, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Aluno).where(models.Aluno.id == aluno_id))
    aluno_db = result.scalar_one_or_none()
    if not aluno_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    await db.delete(aluno_db)
    await db.commit()
