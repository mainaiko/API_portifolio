# Objetivos

Criar uma API Restful capaz de executar operaçoes CRUD utilizando um servidor SQL


# Ferramentas

python 🐍 | FastApi | PostgreSQL | Docker 🐋

# Descrição

Fiz esse projeto com o intuito de testar minhas habilidades em python criando uma API totalmente do zero. Pesquisei a melhor framework para meu projeto e utilizei o postgreSQL pois estava mais familizaridada com minhas aulas do dia a dia. Docker e alembic realmente foram uma novidade para mim.
Bom inicialmente criei o docker file para minha imagem principal em seguida defini o docker compose para trabalhar com 2 containers, criei o data base para injeçao de dados com seçoes assincronas no banco de dados (bem complexo para mim demorei a compreender) apos isso foi a hora dos models e schemas simples e rapido, apos isso fui configurar o alembic para as operaçoes CRUD e pela sua praticidade com o SQLalchemy, 

# Como testar?

certifique-se que esta na pasta workout e rode na linha de comando

docker-compose up --build -d


docker-compose exec web bash


alembic init app/migrations


alembic revision --autogenerate -m "criação inicial"