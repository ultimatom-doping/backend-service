from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.database.database import Base
import datetime

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    deleted_at = Column(TIMESTAMP, nullable=True)

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    deleted_at = Column(TIMESTAMP, nullable=True)

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    deleted_at = Column(TIMESTAMP, nullable=True)

    subject = relationship("Subject")

class QuizQuestion(Base):
    __tablename__ = "quizzes_questions"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))

class StudentQuestion(Base):
    __tablename__ = "students_questions"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    result = Column(String, nullable=False)
    attempted_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
