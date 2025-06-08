from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:senha123@localhost:5433/workout")

# Criação do engine síncrono
engine = create_engine(DATABASE_URL, echo=True)

# Sessionmaker síncrona
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Função para injetar a sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
