import os
import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models import Base, Group, Student, Teacher, Subject, Grade

load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
fake = Faker()


def create_schema():
    Base.metadata.create_all(engine)


def seed():
    session = Session()
    try:
        groups = []
        for g in ["A1", "B1", "C1"]:
            grp = Group(name=g)
            session.add(grp)
            groups.append(grp)
        session.commit()

        teachers = []
        for _ in range(4):
            t = Teacher(first_name=fake.first_name(), last_name=fake.last_name())
            session.add(t)
            teachers.append(t)
        session.commit()

        subjects = []
        subject_names = ["Mathematics", "Physics", "Programming", "Databases", "Algorithms", "English", "History"]
        random.shuffle(subject_names)
        for name in subject_names[:6]:
            teacher = random.choice(teachers)
            s = Subject(name=name, teacher=teacher)
            session.add(s)
            subjects.append(s)
        session.commit()

        students = []
        for _ in range(40):
            grp = random.choice(groups)
            st = Student(first_name=fake.first_name(), last_name=fake.last_name(), group=grp)
            session.add(st)
            students.append(st)
        session.commit()

        for st in students:
            n = random.randint(5, 20)
            for _ in range(n):
                subj = random.choice(subjects)
                value=random.randint(1, 100),
                g = Grade(student=st, subject=subj, value=value, created_at=fake.date_time_this_decade())
                session.add(g)
        session.commit()
        print("Seeding finished.")
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    create_schema()
    seed()
