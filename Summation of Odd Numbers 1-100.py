#Summation of odd numbers 1-100

# Using 'for' loop
sum = 0
for x in range(2, 100+1, 2):
    sum = sum + x
    print(x)
print("The sum is== ", sum)

# Using 'while' loop
sum = 0
i = 2
while i <= 100:
    sum = sum + i
    print(i)
    i = i + 2
print("The sum is== ", sum)

