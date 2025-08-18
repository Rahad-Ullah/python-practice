mark = 55

if mark>=80:
    print("A+")
elif mark>=70:
    print("A")
elif mark>=60:
    print("A-")
elif mark>=50:
    print("B")
elif mark>=40:
    print("C")
else:
    print("Failed")


#Marking the largest bitween 3 numbers
num1 = 1200
num2 = 130
num3 = 500

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
