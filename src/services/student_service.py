from sqlalchemy.orm import Session
from src.database.models import StudentQuestion
from typing import Optional
from datetime import datetime
# import os
# from dotenv import load_dotenv

# load_dotenv()

# ML_SERVICE_URL = os.getenv("ML_SERVICE_URL")

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

# def get_suggested_question(student_id: int, subject_id: int):
#     url = ML_SERVICE_URL + "/api/students/" + student_id + "/suggest-question/" + subject_id
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return

#     data = response.json()