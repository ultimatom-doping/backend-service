from sqlalchemy.orm import Session
from src.database.models import StudentQuestion
from typing import Optional
from datetime import datetime

def get_student_questions(db: Session, student_id: int):
    return db.query(StudentQuestion).filter(StudentQuestion.student_id == student_id).all()

def get_student_questions_for_all_students(db: Session, since: Optional[datetime] = None):
    """
    Returns all StudentQuestion records in the database.
    If 'since' is provided, it filters to only those records with attempted_at >= since.
    """
    query = db.query(StudentQuestion)
    if since is not None:
        query = query.filter(StudentQuestion.attempted_at >= since)

    return query.all()