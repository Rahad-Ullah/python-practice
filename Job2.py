#Factorial number
n = int(input("Enter the last number:"))
sum = 1
for x in range(1, n+1, 1):
    print(x)
    sum = sum * x
print(sum)