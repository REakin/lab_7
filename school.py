from student import Student


class School:
    """ School class """

    SCHOOL_NAME_FIELD = "School Name"
    STUDENT_NUM_FIELD = "Student Number"
    PROG_NAME_FIELD = "Program Name"

    def __init__(self, school_name):
        """ Initializes school object with specified name """

        School._validate_string_input(School.SCHOOL_NAME_FIELD, school_name)
        self._school_name = school_name
        self._students = []

    def add_student(self, student):
        """ Adds a student to the school. """

        School._validate_student(student)
        if student not in self._students:
            self._students.append(student)

    def student_exists(self, student_number):
        """ Checks if student is in the school. """

        School._validate_string_input(School.STUDENT_NUM_FIELD, student_number)
        enrolled_list = [student.get_student_number()
                         for student in self._students]

        if student_number in enrolled_list:
            return True

        return False

    def remove_student(self, student_number):
        """ Removes a student from the school. """

        School._validate_string_input(School.STUDENT_NUM_FIELD, student_number)
        enrolled_list = [student.get_student_number()
                         for student in self._students]

        if student_number in enrolled_list:
            del self._students[enrolled_list.index(student_number)]

    def get_student(self, student_number):
        """ Returns the student with the given student_number. """

        School._validate_string_input(School.STUDENT_NUM_FIELD, student_number)
        enrolled_list = [student.get_student_number()
                         for student in self._students]

        if student_number in enrolled_list:
            return self._students[enrolled_list.index(student_number)]

    def get_num_students_in_program(self, program):
        """ Returns the number of students in a given program. """

        School._validate_string_input(School.PROG_NAME_FIELD, program)
        program_students = [student for student in self._students
                            if student.get_program() == program]

        return len(program_students)

    def get_num_students(self):
        """ Returns the number of students enrolled in the school. """

        return len(self._students)

    def get_all_students(self):
        """returns the list of students"""
        return self._students

    def get_programs(self):
        """ Returns a dictionary representation of a point """
        programs=[]
        for student in self._students:
            program = student.get_program()
            if program not in programs:
                programs.append(program)
        return programs

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_student(student):
        """ Private helper to validate students """

        if student is None:
            raise ValueError("Student must be defined.")
