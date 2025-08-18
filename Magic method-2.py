class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return (f"Name = {self.name}, Color = {self.color}")

    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")


bike1 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha L34", "Red")
print(bike1)