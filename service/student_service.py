from os.path import commonpath

from repository.student_repository import StudentRepository
from repository.course_repository import CourseRepository

from utils.schema import StudentResponse, StudentCreate, StudentUpdate
from model.student import Students
from model.subjects import Subjects

class StudentService:
    def __init__(self):
        self.repository = StudentRepository()
        self.subject_repository = CourseRepository()

    def get_students(self):
        students =  self.repository.get_all_student()
        student_list = []
        for student in students:
            course_score : Subjects = self.subject_repository.get_course_by_roll(student.roll)
            average = (course_score.english_score + course_score.math_score + course_score.history_score) / 3

            if average >= 90:
                comment = "Excellent"
            elif average >= 80:
                comment = "Better"
            elif average >= 70:
                comment = "Good"
            else:
                comment = "Need Improvement"

            student_response = StudentResponse(
                id = student.id,
                name = student.name,
                age = student.age,
                email = student.email,
                roll = student.roll,
                session = student.session,
                english_score = course_score.english_score,
                math_score = course_score.math_score,
                history_score = course_score.history_score,
                comment = comment
            )

            student_list.append(student_response)
        return student_list

    def add_student(self, student_payload : StudentCreate):
        student = Students(**student_payload.to_student_dict())
        self.repository.create_student(student)

        subject = Subjects(student_roll= student_payload.roll,
                           english_score = student_payload.english_score,
                           math_score = student_payload.math_score,
                           history_score =student_payload.history_score
                           )
        self.subject_repository.add_subject_score(subject)


    def delete_student(self, student_roll: int):
        self.subject_repository.delete_subject_score(student_roll)
        self.repository.delete_student(student_roll)

    def update_student(self, roll: int, update_payload : StudentUpdate):
        student = self.repository.get_student_by_roll(roll)
        if student is None:
            return
        if update_payload.name is not None:
            student.name = update_payload.name
        if update_payload.email is not None:
            student.email = update_payload.email
        self.repository.update_student(student)

        course_score = self.subject_repository.get_course_by_roll(roll)
        if course_score is None:
            return
        if update_payload.english_score is not None:
            course_score.english_score = update_payload.english_score
        if update_payload.math_score is not None:
            course_score.math_score = update_payload.math_score
        if update_payload.history_score is not None:
            course_score.history_score = update_payload.history_score
        self.subject_repository.update_subject_score(course_score)
