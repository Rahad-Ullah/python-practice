#Find factorials of a number

num = int(input("Enter the number: "))

sum  = 1
for x in range(1, num + 1):
    sum = sum * x

print(sum)
