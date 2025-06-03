# Caminho do ambiente virtual (ajuste se necessário)
VENV=source .venv/bin/activate

venv:
	source $(VENV)

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

up:
	docker-compose up --build

down:
	docker-compose down

migrate:
	alembic upgrade head

# Gera uma nova migração (use: make revision msg="sua mensagem")
revision:
	alembic revision --autogenerate -m "$(pao)"

# Entra no shell do container do app
bash:
	docker exec -it fastapi_app /bin/sh

# Apaga os volumes e containers (com força)
clean:
	docker-compose down -v --remove-orphans
