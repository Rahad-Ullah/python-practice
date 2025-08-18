#Find all prime numbers in an interval

lower_number = int(input("Enter the lower number: "))
upper_number = int(input("Enter the upper number: "))

print("Prime numbers between", lower_number, 'and', upper_number, 'are: ')
for num in range(lower_number, upper_number + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for x in range(2, num):
            if (num % x) == 0:
                break
        else:
            print(num)
