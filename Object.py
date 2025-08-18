class Student:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll} , GPA : {self.gpa}")

Rafin = Student()
Rafin.roll = 101
Rafin.gpa = 4.50
Rafin.display()

Ahsan = Student()
Ahsan.roll = 102
Ahsan.gpa = 4.55
Ahsan.display()


"""Alternative Way"""
#Using Methods
class Student:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll} , GPA : {self.gpa}")

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

Rafin = Student()
Rafin.set_value(101, 4.50)
Rafin.display()

Ahsan = Student()
Ahsan.set_value(102, 4.55)
Ahsan.display()