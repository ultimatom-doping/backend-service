from sqlalchemy.orm import Session
from src.database.models import StudentQuestion

def get_student_questions(db: Session, student_id: int):
    return db.query(StudentQuestion).filter(StudentQuestion.student_id == student_id).all()
