# API de Gerenciamento de Alunos (Workout)

Uma API RESTful para gerenciar informações de alunos, construída com Python, FastAPI, PostgreSQL, SQLAlchemy e Docker.

# Descrição

Fiz esse projeto com o intuito de testar minhas habilidades em python criando uma API totalmente do zero. Pesquisei a melhor framework para meu projeto e utilizei o postgreSQL pois estava mais familizaridada com minhas aulas do dia a dia. Docker e alembic realmente foram uma novidade para mim.
Criei o database e o main em seguida criei os models e schemas, moldei melhor o main e reformulei o data base de acordo com engine sincrona. Coloquei o alembic para melhor automação e controle do Banco de dados. Configurei os arquivos docker e claro que deu erro, tive que reformular melhor o codigo arrumar alguns imports e o alembic. Por fim consegui fazer a aplicação rodar da maneira que gostaria.

## Tecnologias

*   Python
*   FastAPI
*   PostgreSQL
*   SQLAlchemy
*   Alembic
*   Docker

## Pré-requisitos

*   Docker e Docker Compose

## Executando a Aplicação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/mainaiko/API_portifolio.git
    ```

2.  **Inicie os containers:**

    ```bash
    docker compose build
    docker compose up -d
    ```

3.  **Acesse a API:**

    A API estará disponível em `http://localhost:8000/docs`.

## Testando a API

Você pode usar ferramentas como Postman para interagir com a API.

## Migrações (Alembic)

As migrações do banco de dados são gerenciadas com Alembic. Para aplicá-las:

1.  Entre no container da aplicação:

    ```bash
    docker-compose exec web bash
    ```

2.  Execute os comandos do Alembic (dentro do container):

    *   Para aplicar as migrações:  `alembic upgrade head`

## Parando a Aplicação

```bash
docker-compose down
```