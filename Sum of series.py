#1+2+3+4+5=?
n = int(input('Please enter the input: '))
if n<0:
    print('Sorry! Please enter a positive number.')
else:
    sum = 0
    for x in range(1, n+1):
        sum = sum + x
    print(sum)

#using while loop:
    sum = 0
    i = 1
    while i<=n:
        sum = sum + i
        i = i + 100
    print(sum)

