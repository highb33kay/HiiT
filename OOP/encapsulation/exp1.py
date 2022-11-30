# Base Class
class School():
    def __init__(self, Teacher, Student):
        # defining a protected variable
        self._Teacher = Teacher
        self._Student = Student
        self._number = 59

    # class method using protected member
    def print_students(self):
        print(
            f'this is a protected member: {self._Teacher} and {self._Student}')

# subclass of the base class


class LabA(School):
    def __init__(self, Teacher, Student):
        School.__init__(self, Teacher, Student)
        self._number = 60


Student1 = LabA('Highb33kay', 'Jesse')

Student2 = School('David', 'James')

print(Student1.print_students())
