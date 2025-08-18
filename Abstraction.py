from abc import ABC,abstractmethod

class Shape(ABC):
    def __int__(self, Dimension1, Dimension2):
        self.Dimension1 = Dimension1
        self.Dimension2 = Dimension2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.Dimension1 * self.Dimension2
        print("Area of Triangle = ", area)

class Rectangle(Shape):
    def area(self):
        area = self.Dimension1 * self.Dimension2
        print("Area of Rectangle = ", area)

a = float(input("Enter Dimension1"))
b = float(input("Enter Dimension2"))

t1 = Triangle(a, b)
t1.area()

r1 = Rectangle(a, b)
r1.area()
