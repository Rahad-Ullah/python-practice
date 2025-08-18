class A:
    def display(self):
        print("I am in class A")

class B:
    #display1
    def display(self):
        print("I am in class B")

class C(B,A):
    # display1
    # display2
    pass

obj1 = C()
obj1.display()