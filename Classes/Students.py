# define a class called students
class Student:
    # doc string
    """This is a student class"""

    # the init method or construct to store scores students
    def __init__(self, name, maths, python):
        # instance variable
        self.maths = maths
        self.python = python
        self.name = name

    # counts number of students
    def printScore(self):
        print(
            f"Hello, {self.name}, Your Python Score is {self.python} and your maths score is {self.maths}")

    def printStudents(self):
        pass


# creating an object
Student_1 = Student("Jesse", 4, 5)
Student_2 = Student("Jessica", 5, 8)

print(Student_2.printScore())
print(Student_1.printScore())
