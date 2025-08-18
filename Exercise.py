class  Triangle:
    base = ""
    hight = ""

    def __init__(self, base, hight):
        self.base = base
        self.hight = hight

    def area(self):
        area = 0.5 * self.base * self.hight
        print("Area of the triangle = ", area)

base = float((input("Enter the base: ")))
hight = float((input("Enter the hight: ")))
t1 =  Triangle(base, hight)
t1.area()

