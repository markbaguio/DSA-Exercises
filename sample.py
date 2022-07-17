class Student:
    def __init__(self, studenID, name):
        self.studentID = studenID
        self.name = name

    def print_student_info(self):
        print("{}, {}".format(self.studentID, self.name))


a = Student(2018102080, "Mark Godwin C. Baguio")
b = Student(2018102081, "Ada Wong")
a.print_student_info()
b.print_student_info()
