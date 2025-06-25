# Objetivos

Criar uma API Restful capaz de executar operaçoes CRUD utilizando um servidor SQL

# Ferramentas

python 🐍 | FastApi | PostgreSQL SQLalchemy | Docker 🐋 | Alembic

# Descrição

Fiz esse projeto com o intuito de testar minhas habilidades em python criando uma API totalmente do zero. Pesquisei a melhor framework para meu projeto e utilizei o postgreSQL pois estava mais familizaridada com minhas aulas do dia a dia. Docker e alembic realmente foram uma novidade para mim.
Bom inicialmente criei o docker file para minha imagem principal em seguida defini o docker compose para trabalhar com 2 containers, criei o data base para injeçao de dados no banco sincrono, apos isso foi a hora dos models e schemas simples e rapido, fui configurar o alembic para as operaçoes CRUD, criei o arquivo main onde tudo acontece e por fim fiz umas configuraçoes no alembic.ini. Apos algumas correçoes de erros e algumas frustraçoes cheguei no resultado final tive que deixar o banco de dados sincrono porque o assincrono estava dando muitos erros e n conseguia chegar a uma conclusao(coisa de iniciante talvez).

# Como testar?

requisitos: docker, docker compose, postgresql-client


No terminal

```bash
#Imagem do fastapi
docker pull aikomarques/workout-web:latest

#Imagem do banco
docker pull aikomarques/postgres:15
```
_______________________________________________________________________________________
Inicie o banco de dados com a imagem oficial
```bash
docker run -d \
  --name workout-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=senha123 \
  -e POSTGRES_DB=workout \
  -p 5433:5432 \
  postgres:15
```

Conferir se esta ativo
```bash
docker ps
```

Inicie a aplicação web apontando para o banco
```bash
docker run -d \
  --name workout-web \
  -e DATABASE_URL=postgresql://postgres:senha123@workout-db:5432/workout \
  --link workout-db \
  -p 8000:8000 \
  aikomarques/workout-web:latest
```

Teste de conexão
```bash
psql -h localhost -p 5433 -U postgres -d workout
```
_______________________________________________________________________________________

Acesse a aplicação
```bash
http://localhost:8000/
```


Pare os containers
```bash
docker stop workout-web workout-db
docker rm workout-web workout-db
```

Para dúvidas, abra uma issue ou envie um email para aikomarques58912@gmail.com



