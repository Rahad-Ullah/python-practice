class Shape:
    def __int__(self, Dimension1, Dimension2):
        self.Dimension1 = Dimension1
        self.Dimension2 = Dimension2

    def area(self):
        print("I am in shap class")

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.Dimension1 * self.Dimension2
        print("Area of Triangle = ", area)

class Rectangle(Shape):
    def area(self):
        area = self.Dimension1 * self.Dimension2
        print("Area of Rectangle = ", area)

t1 = Triangle(20, 30)
t1.area()

r1 = Rectangle(20, 30)
r1.area()