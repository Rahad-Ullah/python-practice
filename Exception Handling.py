"""
Except Handling is a most important part of a program.
To write a user-friendly program it must have used.
"""
try:
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")
finally:
    print("Succesful")

#Second part
try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    result = num1/num2
    print(result)

except ValueError:
    print("You have entered incorrect value.")
except ZeroDivisionError:
    print("Divided by zero is not possible.")

finally:
    print("Thanks!!!")

"""
alternative way:
except ValueError, ZeroDivisionError:
    print("You have entered incorrect value.")
"""

def voter (age):
    if age <18:
        raise ValueError("Alas! You are not aged for this.")
    return "You are allowed to vote."


try:
    age = int(input("Enter your age"))
    print(voter(age))
except ValueError as e:
    print(e)

finally:
    print("Thanks!!!")