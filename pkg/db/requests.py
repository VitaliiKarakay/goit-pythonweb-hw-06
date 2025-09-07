import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pkg.db.models import Student, Grade, Subject, Teacher, Group

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    session = Session()
    try:
        q = (
            session.query(
                Student.id,
                Student.first_name,
                Student.last_name,
                func.avg(Grade.value).label("avg_score")
            )
            .join(Grade)
            .group_by(Student.id)
            .order_by(func.avg(Grade.value).desc())
            .limit(5)
        )
        return q.all()
    finally:
        session.close()


# 2. Знайти студента із найвищим середнім балом з певного предмета.
def select_2(subject_name):
    session = Session()
    try:
        q = (
            session.query(
                Student.id,
                Student.first_name,
                Student.last_name,
                func.avg(Grade.value).label("avg_score")
            )
            .join(Grade)
            .join(Subject)
            .filter(Subject.name == subject_name)
            .group_by(Student.id)
            .order_by(func.avg(Grade.value).desc())
            .limit(1)
        )
        return q.first()
    finally:
        session.close()


# 3. Знайти середній бал у групах з певного предмета.
def select_3(subject_name):
    session = Session()
    try:
        q = (
            session.query(
                Group.name.label("group_name"),
                func.avg(Grade.value).label("avg_score")
            )
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject)
            .filter(Subject.name == subject_name)
            .group_by(Group.id)
            .order_by(func.avg(Grade.value).desc())
        )
        return q.all()
    finally:
        session.close()


# 4. Середній бал на потоці (всі оцінки)
def select_4():
    session = Session()
    try:
        avg_score = session.query(func.avg(Grade.value)).scalar()
        return avg_score
    finally:
        session.close()


# 5. Знайти які курси читає певний викладач.
def select_5(teacher_id):
    session = Session()
    try:
        q = session.query(Subject).filter(Subject.teacher_id == teacher_id).all()
        return q
    finally:
        session.close()


# 6. Знайти список студентів у певній групі.
def select_6(group_id):
    session = Session()
    try:
        q = session.query(Student).filter(Student.group_id == group_id).all()
        return q
    finally:
        session.close()


# 7. Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(group_id, subject_name):
    session = Session()
    try:
        q = (
            session.query(
                Student.id, Student.first_name, Student.last_name, Grade.value, Grade.created_at
            )
            .join(Grade)
            .join(Subject)
            .filter(Student.group_id == group_id, Subject.name == subject_name)
            .order_by(Student.id)
        )
        return q.all()
    finally:
        session.close()


# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(teacher_id):
    session = Session()
    try:
        q = (
            session.query(func.avg(Grade.value))
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Subject.teacher_id == teacher_id)
        )
        return q.scalar()
    finally:
        session.close()


# 9. Знайти список курсів, які відвідує певний студент.
def select_9(student_id):
    session = Session()
    try:
        q = (
            session.query(Subject)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(Grade.student_id == student_id)
            .group_by(Subject.id)
        )
        return q.all()
    finally:
        session.close()


# 10. Список курсів, які певному студенту читає певний викладач.
def select_10(student_id, teacher_id):
    session = Session()
    try:
        q = (
            session.query(Subject)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
            .group_by(Subject.id)
        )
        return q.all()
    finally:
        session.close()
