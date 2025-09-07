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
# 1. Top 5 students with the highest average score
python -c "from pkg.db.requests import select_1; print(select_1())"

# 2. Student with the highest average score in a subject
python -c "from pkg.db.requests import select_2; print(select_2('Math'))"

# 3. Average score in groups for a subject
python -c "from pkg.db.requests import select_3; print(select_3('Math'))"

# 4. Average score for all students
python -c "from pkg.db.requests import select_4; print(select_4())"

# 5. Courses taught by a specific teacher
python -c "from pkg.db.requests import select_5; print(select_5(1))"

# 6. List of students in a specific group
python -c "from pkg.db.requests import select_6; print(select_6(1))"

# 7. Grades of students in a group for a subject
python -c "from pkg.db.requests import select_7; print(select_7(1, 'Math'))"

# 8. Average score given by a specific teacher
python -c "from pkg.db.requests import select_8; print(select_8(1))"

# 9. List of courses attended by a specific student
python -c "from pkg.db.requests import select_9; print(select_9(1))"

# 10. List of courses taught to a student by a specific teacher
python -c "from pkg.db.requests import select_10; print(select_10(1, 1))"
```

---

> For proper operation, make sure the database connection settings are specified in .env or alembic.ini.
