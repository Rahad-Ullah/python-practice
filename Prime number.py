#prime number
num = int(input('Enter the number:'))

if num>1:
    for x in range(2, num):
        if num%x==0:
            print('The number is not a prime number.')
    else:
        print('The number is a prime number.')
else:
    print('The number is not a prime number')