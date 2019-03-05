from flask import Flask, request
from student import Student
from school import School
import json
app = Flask(__name__)

school = School('BCIT')

@app.route('/school/students', methods=['POST'])
def add_student():
    """adds a student to the school and attaches the courses"""
    content = request.json
    try:
        student = Student(content['first_name'],content['last_name'],
                          content['student_number'],content['program'])
        if(school.student_exists(content['student_number']) == True):
            raise ValueError ('Student Exists')
        else:
            school.add_student(student)
            for course in content['courses']:
                student.add_course(course)

        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/school/students/<student_number>', methods=['PUT'])
def update_student(student_number):
    """updates a student by student number"""
    content = request.json
    try:
        if(school.student_exists(content['student_number']) == False):
            raise ValueError ('No student found with this number')
        else:
            student = Student(content['first_name'], content['last_name'],
                          student_number,content['program'])
            school.remove_student(student_number)
            school.add_student(student)
            for course in content['courses']:
                student.add_course(course)

            response = app.response_class(
                status=200
            )
    except ValueError as e:
        response = app.response_class(
            status=404
        )
    return response

@app.route('/school/students/<student_number>', methods=['DELETE'])
def delete_student(student_number):
    """deletes a student by student number"""
    try:
        if (school.student_exists(student_number) == False):
            raise ValueError('Student Number is invalid')
        school.remove_student(student_number)
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/school/students/<student_number>', methods=['GET'])
def get_student(student_number):
    """shows a students information by student number"""
    try:
        if (school.student_exists(student_number) == False):
            raise ValueError('Student Number is invalid')
        student = school.get_student(student_number)

        response = app.response_class(
            status=200,
            response=json.dumps(student.to_dict()),
            mimetype='application/json'
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
        return response

@app.route('/school/students/all', methods=['GET'])
def get_all_students():
    """returns all students"""
    students = school.get_all_students()
    student_list = []

    for student in students:
        student_list.append(student.to_dict())
    response = app.response_class(
        status=200,
        response=json.dumps(student_list),
        mimetype='application/json'
    )
    return response

@app.route('/school/students/program/<program>', methods=['GET'])
def get_student_program(program):
    """shows all students who are in a specified program"""
    students = school.get_all_students()
    student_list = []
    try:
        for student in students:
            if student.get_program() == program:
                student_list.append(student.to_dict())
        if len(student_list) == 0:
            raise ValueError ('No students in the given program')
        response = app.response_class(
            status=200,
            response=json.dumps(student_list),
            mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=404,
            response=str(e)
        )
    return response

@app.route('/school', methods=['GET'])
def get_school():
    """returns the school details"""
    school_details ={}
    school_details['Name'] = school._school_name
    school_details['Num_students'] = school.get_num_students()
    school_details['Programs'] = school.get_programs()

    response = app.response_class(
        status=200,
        response=json.dumps(school_details),
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)