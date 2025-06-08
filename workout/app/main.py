from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from app import database
from app.models import aluno as models
from app.schemas import aluno as schemas

app = FastAPI()

@app.post("/alunos/", response_model=schemas.AlunoOut)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(database.get_db)):
    novo_aluno = models.Aluno(**aluno.dict())
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

@app.get("/alunos/", response_model=list[schemas.AlunoOut])
def listar_alunos(db: Session = Depends(database.get_db)):
    result = db.execute(select(models.Aluno))
    return result.scalars().all()

@app.get("/alunos/{aluno_id}", response_model=schemas.AlunoOut)
def buscar_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    result = db.execute(select(models.Aluno).where(models.Aluno.id == aluno_id))
    aluno = result.scalar_one_or_none()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@app.patch("/alunos/{aluno_id}", response_model=schemas.AlunoOut)
def atualizar_aluno(aluno_id: int, aluno: schemas.AlunoUpdate, db: Session = Depends(database.get_db)):
    result = db.execute(select(models.Aluno).where(models.Aluno.id == aluno_id))
    aluno_db = result.scalar_one_or_none()
    if not aluno_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    for chave, valor in aluno.dict(exclude_unset=True).items():
        setattr(aluno_db, chave, valor)
    db.commit()
    db.refresh(aluno_db)
    return aluno_db

@app.delete("/alunos/{aluno_id}", status_code=204)
def deletar_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    result = db.execute(select(models.Aluno).where(models.Aluno.id == aluno_id))
    aluno_db = result.scalar_one_or_none()
    if not aluno_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(aluno_db)
    db.commit()
