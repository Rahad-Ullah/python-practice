# Find factors of a number

def print_factors(num):
    print("The factors of", num, 'are: ')
    for x in range(1, num + 1):
        if (num % x) == 0:
            print(x)

print_factors(40)
