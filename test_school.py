from unittest import TestCase
from school import School
from student import Student


class TestSchool(TestCase):
    """ Unit Tests for the School Class """

    def test_school(self):
        """ 010A - Valid Construction """

        test_school = School("Computing and Academic Studies")
        self.assertIsNotNone(test_school, "School must be defined")

    def test_school_invalid_parameters(self):
        """ 010B - Invalid Construction Parameters """

        # Must reject an undefined school name
        undefined_school = None
        self.assertRaisesRegex(ValueError, "School Name cannot be undefined", School, undefined_school)

        # Must reject an empty school name
        empty_school = ""
        self.assertRaisesRegex(ValueError, "School Name cannot be empty.", School, empty_school)

    def test_add_student(self):
        """ 020A - Valid Add Student """
        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CIT")
        test_student_2.add_course("ACIT2515")
        test_student_2.add_course("COMP1409")

        test_school = School("Computing and Academic Studies")
        self.assertEqual(test_school.get_num_students(), 0, "School must have no students")

        test_school.add_student(test_student_1)
        self.assertEqual(test_school.get_num_students(), 1, "School must have 1 student")

        test_school.add_student(test_student_2)
        self.assertEqual(test_school.get_num_students(), 2, "School must have 2 students")

    def test_add_student_undefined(self):
        """ 020B - Invalid Add Student Parameters """

        test_school = School("Computing and Academic Studies")

        invalid_student = None
        self.assertRaisesRegex(ValueError, "Student must be defined.", test_school.add_student, invalid_student)

    def test_add_student_already_exists(self):
        """ 020C - Student Already Exists """

        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_school = School("Computing and Academic Studies")
        self.assertEqual(test_school.get_num_students(), 0, "School must have no students")

        test_school.add_student(test_student_1)
        self.assertEqual(test_school.get_num_students(), 1, "School must have 1 student")

        # Add the same student again
        test_school.add_student(test_student_1)
        self.assertEqual(test_school.get_num_students(), 1, "School must have 1 student")

    def test_student_exists(self):
        """ 030A - Valid Student Exists """

        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CIT")
        test_student_2.add_course("ACIT2515")
        test_student_2.add_course("COMP1409")

        test_school = School("Computing and Academic Studies")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)

        self.assertTrue(test_school.student_exists("A0100000000"), "Student A0100000000 must exist")
        self.assertTrue(test_school.student_exists("A0100000001"), "Student A0100000001 must exist")

    def test_student_exists_invalid_student_id(self):
        """ 030B - Invalid Student Exists Parameters """

        test_school = School("Computing and Academic Studies")

        student_id_undef = None
        self.assertRaisesRegex(ValueError, "Student Number cannot be undefined.", test_school.student_exists, student_id_undef)

        student_id_empty = ""
        self.assertRaisesRegex(ValueError, "Student Number cannot be empty.", test_school.student_exists, student_id_empty)

    def test_student_exists_not_existent_student(self):
        """ 030C - Valid Student Does Not Exist """

        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CIT")
        test_student_2.add_course("ACIT2515")
        test_student_2.add_course("COMP1409")

        test_school = School("Computing and Academic Studies")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)

        self.assertFalse(test_school.student_exists("B0100000000"), "Student B0100000000 must NOT exist")
        self.assertFalse(test_school.student_exists("A0100000002"), "Student A0100000002 must NOT exist")

    def test_remove_student(self):
        """ 040A - Valid Remove Student """

        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CIT")
        test_student_2.add_course("ACIT2515")
        test_student_2.add_course("COMP1409")

        test_school = School("Computing and Academic Studies")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)

        self.assertEqual(test_school.get_num_students(), 2, "School must have 2 students")
        self.assertTrue(test_school.student_exists("A0100000000"))
        self.assertTrue(test_school.student_exists("A0100000001"))

        test_school.remove_student("A0100000001")
        self.assertEqual(test_school.get_num_students(), 1, "School must have 1 student")
        self.assertFalse(test_school.student_exists("A0100000001"))

    def test_remove_student_invalid_student_id(self):
        """ 040B - Invalid Remove Student Parameters """

        test_school = School("Computing and Academic Studies")

        student_id_undef = None
        self.assertRaisesRegex(ValueError, "Student Number cannot be undefined.", test_school.remove_student, student_id_undef)

        student_id_empty = ""
        self.assertRaisesRegex(ValueError, "Student Number cannot be empty.", test_school.remove_student, student_id_empty)

    def test_remove_non_existent_student(self):
        """ 040C - Invalid Remove Student Non-Existent """

        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CIT")
        test_student_2.add_course("ACIT2515")
        test_student_2.add_course("COMP1409")

        test_school = School("Computing and Academic Studies")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)

        self.assertEqual(test_school.get_num_students(), 2, "School must have 2 students")
        self.assertTrue(test_school.student_exists("A0100000000"))
        self.assertTrue(test_school.student_exists("A0100000001"))

        test_school.remove_student("B0100000001")
        self.assertEqual(test_school.get_num_students(), 2, "School must have 2 students")

    def test_get_student(self):
        """ 050A - Valid Get Student """
        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CIT")
        test_student_2.add_course("ACIT2515")
        test_student_2.add_course("COMP1409")

        test_school = School("Computing and Academic Studies")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)

        retrieved_student = test_school.get_student("A0100000001")
        self.assertEqual(retrieved_student.get_student_number(), "A0100000001", "Student must have student number A0100000001")
        self.assertEqual(retrieved_student.get_program(), "CIT", "Student must be in CIT program")

    def test_get_student_invalid_student_id(self):
        """ 050B - Invalid Get Student Parameters """

        test_school = School("Computing and Academic Studies")

        student_id_undef = None
        self.assertRaisesRegex(ValueError, "Student Number cannot be undefined.", test_school.get_student, student_id_undef)

        student_id_empty = ""
        self.assertRaisesRegex(ValueError, "Student Number cannot be empty.", test_school.get_student, student_id_empty)

    def test_get_non_existent_student(self):
        """ 050C - Invalid Get Student Non-Existent """

        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CIT")
        test_student_2.add_course("ACIT2515")
        test_student_2.add_course("COMP1409")

        test_school = School("Computing and Academic Studies")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)

        self.assertIsNone(test_school.get_student("AXXXYYYZZZ"), "No student should exists for AXXXYYYZZZ")

    def test_get_num_students_in_program(self):
        """ 060A - Valid Get Number of Student in Program """

        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_1.add_course("ACIT2515")

        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CSD")
        test_student_2.add_course("COMP1510")

        test_student_3 = Student("Sally", "Jones", "A0100000002", "CSD")
        test_student_3.add_course("COMP1510")

        test_student_4 = Student("Julie", "Wong", "A0100000003", "CSD")
        test_student_4.add_course("COMP1510")

        test_school = School("Computing and Academic Studies")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)
        test_school.add_student(test_student_3)
        test_school.add_student(test_student_4)

        self.assertEqual(test_school.get_num_students_in_program("CIT"), 1, "Must be only 1 CIT student")
        self.assertEqual(test_school.get_num_students_in_program("CSD"), 3, "Must be 3 CSD students")
        self.assertEqual(test_school.get_num_students_in_program("SSD"), 0, "Must be no SSD students")

    def test_get_all_students(self):
        """creates 3 students and adds them to the school and sees how many are returned"""
        test_school = School("Computing and Academic Studies")
        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CSD")
        test_student_3 = Student("Sally", "Jones", "A0100000002", "CSD")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)
        test_school.add_student(test_student_3)

        self.assertEqual(len(test_school.get_all_students()),3)



    def test_get_programs(self):
        """adds students and checks what programs are returned"""
        test_school = School("Computing and Academic Studies")
        test_student_1 = Student("Bill", "Smith", "A0100000000", "CIT")
        test_student_2 = Student("Ken", "Rodgers", "A0100000001", "CSD")
        test_student_3 = Student("Sally", "Jones", "A0100000002", "CSD")
        test_school.add_student(test_student_1)
        test_school.add_student(test_student_2)
        test_school.add_student(test_student_3)

        self.assertEqual(test_school.get_programs(),["CIT","CSD"])
    def test_get_num_student_in_program_invalid_program_name(self):
        """ 060B - Invalid Get Num Students in Program Parameters """

        test_school = School("Computing and Academic Studies")

        program_name_undef = None
        self.assertRaisesRegex(ValueError, "Program Name cannot be undefined.", test_school.get_num_students_in_program, program_name_undef)

        program_name_empty = ""
        self.assertRaisesRegex(ValueError, "Program Name cannot be empty.", test_school.get_num_students_in_program, program_name_empty)

