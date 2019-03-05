class Student:
    """ Student Class - Maintains the details of a student """

    FIRST_NAME_FIELD = "First Name"
    LAST_NAME_FIELD = "Last Name"
    STUD_NUM_FIELD = "Student Number"
    PROG_NAME_FIELD = "Program Name"
    COURSE_ID_FIELD = "Course ID"

    def __init__(self, first_name, last_name, student_number, program):
        """ Constructor - Initializes the main attributes of a student """

        Student._validate_string_input(Student.FIRST_NAME_FIELD, first_name)
        self._first_name = first_name

        Student._validate_string_input(Student.LAST_NAME_FIELD, last_name)
        self._last_name = last_name

        Student._validate_string_input(Student.STUD_NUM_FIELD, student_number)
        self._student_number = student_number

        Student._validate_string_input(Student.PROG_NAME_FIELD, program)
        self._program = program

        self._courses=[]

    def get_student_number(self):
        """returns the student number"""
        return self._student_number

    def get_program(self):
        """returns the student program"""
        return self._program

    def add_course(self, course_id):
        """ Adds a course to the student. Rejects duplicate courses. """
        Student._validate_string_input(Student.COURSE_ID_FIELD, course_id)

        if not self.is_enrolled_in_course(course_id):
            self._courses.append(course_id)

    def remove_course(self, course_id):
        """ Removes a course from a student """

        Student._validate_string_input(Student.COURSE_ID_FIELD, course_id)

        if self.is_enrolled_in_course(course_id):
           self._courses.remove(course_id)

    def is_enrolled_in_course(self, course_id):
        """ Checks if enrolled in course """

        Student._validate_string_input(Student.COURSE_ID_FIELD, course_id)

        if self._courses.count(course_id) > 0:
            return True

        return False

    def get_num_courses(self):
        """ Returns the number of courses a student is enrolled in """
        return len(self._courses)

    def get_details(self):
        """ Returns the student details in a printable format """
        course_list = "None"

        if len(self._courses) > 0:
            course_list = ', '.join(str(x) for x in self._courses)

        details = self._first_name + " " + self._last_name + " is a student in the " + self._program + \
                  " Program taking the following courses: " + course_list

        return details

    def to_dict(self):
        """ Returns a dictionary representation of a point """
        dict = {}
        dict['first_name'] = self._first_name
        dict['last_name'] = self._last_name
        dict['student_number'] = self._student_number
        dict['program'] = self._program
        dict['courses'] = self._courses
        return dict

    @classmethod
    def _validate_string_input(cls, display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")