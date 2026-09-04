# fastapi-skeleton

This is a fast-api skeleton application

# setup commands

```bash
#setup fastapi
  pip install fastapi uvicorn

#run fastapi
  uvicorn src.main:app --reload

#docs
  http://127.0.0.1:8000/docs

#freeze packages
  pip freeze > requirements.txt

# email validator
pip install 'pydantic[email]

```

## database setup (local postgres)

```bash
# check status
- sudo systemctl status postgresql
- sudo systemctl start postgresql
- sudo systemctl enable postgresql

# get in db
- sudo -u postgres psql

# list databases
\l

# list postgres users
\du

# exit
\q

# create a table
CREATE DATABASE fastapi_dev;

# connection string
postgresql://postgres:<password>@localhost:5432/fastapi_dev

# install postgres driver and sqlModel orm
pip install sqlmodel psycopg[binary]

# for env
pip install pydantic-settings

# migration
pip install alembic

# initialize alembic
alembic init alembic

# check alembic
alembic current

# create migration
alembic revision --autogenerate -m "create users table"

# run migration
alembic upgrade head

# migration history
alembic history

```

## install admin

```bash

pip install sqladmin

http://127.0.0.1:8000/admin

```
