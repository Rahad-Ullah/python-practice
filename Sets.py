num1 = {1,2,3,4,5,6}
num2 = set([5,6,7,8])
num1.add(5)
num1.remove(5)
print(num1)
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
