from flask import Blueprint, jsonify, request
from Model.repositories.students_repository import StudentsRepository

students_bp = Blueprint('students',__name__)
repo = StudentsRepository()

@students_bp.route("/", methods=["GET"])
def list_students():
    students = repo.select_all_students()
    students_data = []
    for student in students:
        students_data.append({
            "Matrícula": student.registration,
            "Aluno": student.name,
            "Turma": student.student_class
        })

    return jsonify(students_data)