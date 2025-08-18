"""
constructor or init methods automatically set the value. No need to set maually.
"""

class Student:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll} , GPA : {self.gpa}")

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

Rafin = Student(101, 4.50)
Rafin.display()

Ahsan = Student(102, 4.55)
Ahsan.display()