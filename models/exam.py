from db import db


class ExamModel(db.Model):
    __tablename__ = "exams"

    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.String(80), unique=False, nullable=False)
    exam_description = db.Column(db.String(256), unique=False, nullable=False)
    # exam_grade = db.Column(db.Float(precision=2), unique=False, nullable=True)
    examssubmission = db.relationship("ExamSubmissionModel", back_populates="exam", lazy="dynamic")
    course_id = db.Column(
        db.Integer, db.ForeignKey("courses.id"), unique=False, nullable=False
    )
    course = db.relationship("CourseModel", back_populates="exams")

    professor_id = db.Column(
        db.Integer, db.ForeignKey("professors.id"), unique=False, nullable=False
    )
    professor = db.relationship("ProfessorModel", back_populates="exams")