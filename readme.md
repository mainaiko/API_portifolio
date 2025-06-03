# Objetivos

Criar uma API Restful capaz de executar operaçoes CRUD utilizando um servidor SQL


# Ferramentas

python 🐍 | FastApi | PostgreSQL | Docker 🐋

# Descrição

Fiz esse projeto com o intuito de testar minhas habilidades em python criando uma API totalmente do zero. Pesquisei a melhor framework para meu projeto e utilizei o postgreSQL pois estava mais familizaridada com minhas aulas do dia a dia. Docker e alembic realmente foram uma novidade para mim.
Bom inicialmente criei o docker file para minha imagem principal em seguida defini o docker compose para trabalhar com 2 containers, criei o data base para injeçao de dados no banco, apos isso foi a hora dos models e schemas simples e rapido, fui configurar o alembic para as operaçoes CRUD, criei o arquivo main onde tudo acontece e por fim fiz umas configuraçoes no alembic.ini. Apos algumas correçoes de erros e algumas frustraçoes cheguei no resultado final tive que deixar o banco de dados sincrono porque o assincrono estava dando muitos erros e n conseguia chegar a uma conclusao(coisa de iniciante talvez).

# Como testar?

certifique-se que esta na pasta workout e rode na linha de comando

// docker-compose up --build -d

// docker-compose exec web bash

// alembic upgrade head

- se vc receber algo como
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
- entao esta funcionando

- agora vamos fazer algumas alteraçoes no banco
