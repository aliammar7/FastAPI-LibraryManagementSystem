# FastAPI - Library Management System

This is a Library Management System based in FastAPI with the following features:
- FastAPI
- JWT Authentication
- SQLAlchemy ORM
- Alembic migrations (Extendable)
- Clean architecture (services, repositories, schemas)

## 📁 Project Structure

app/
│
├── main.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   ├── security.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│
├── schemas/
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│   ├── auth.py
│
├── repositories/
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│
├── services/
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│   ├── auth.py
│
├── api/
│   ├── __init__.py
│   ├── deps.py
│   └── v1/
│       ├── __init__.py
│       ├── auth.py
│       ├── users.py
│       └── books.py
│
├── utils/
│   └── hashing.py
│
└── alembic/


# How to run
## Install Postgres on Mac

brew install postgresql
brew services start postgresql

Check Installation
psql --version

## Set up Postgres Database
psql postgres

### Create database and User
-- Create a user
CREATE USER library_user WITH PASSWORD 'library_pass';

-- Create a database
CREATE DATABASE library_db OWNER library_user;

-- Optional: allow password login
ALTER USER library_user WITH SUPERUSER;

## Set Up Virtual Enviornment

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

## Install required Python packages

pip install fastapi[all] sqlalchemy psycopg2-binary pydantic-settings passlib[bcrypt] python-jose[cryptography]
pip install alembic

## Run the FastAPI app

python -m uvicorn app.main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000

## Test the App

http://127.0.0.1:8000/docs

