# Project: Student Management (SQLAlchemy, Alembic, PostgreSQL)

This project demonstrates working with a student database using SQLAlchemy, Alembic, and PostgreSQL. It includes test data generation, migrations, and query examples.

## 1. Running PostgreSQL with Docker
Make sure Docker is installed and running. Execute the following command to create a PostgreSQL container:
```bash
docker run --name postgres-hw6 \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=students_db \
  -p 5432:5432 \
  -d postgres
```

## 2. Creating .env file
Create a file named `.env` in the root of your project and add the following line:
```dotenv
DATABASE_URL=postgresql://postgres:password@localhost:5432/postgres
```
This environment variable is required for database connection configuration.

## 3. Setting up Python virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows PowerShell
```

## 4. Installing dependencies
```bash
pip install sqlalchemy psycopg2-binary alembic faker python-dotenv
```

## 5. Alembic setup and migrations
Initialize Alembic and apply migrations:
```bash
alembic init alembic
alembic revision --autogenerate -m "create initial tables"
alembic upgrade head
```

## 6. Generating test data
Run the data generation script:
```bash
python pkg/db/seed/seed.py
```

## 7. Query examples
Run query examples:
```bash
python -c "from pkg.requests import select_1; print(select_1())"
python -c "from pkg.requests import select_2; print(select_2(1))"
python -c "from pkg.requests import select_3; print(select_3())"
```

---

> For proper operation, make sure the database connection settings are specified in .env or alembic.ini.
