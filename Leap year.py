year = int(input('Please enter the value of year:'))
if (year%4==0 and year%100!=0) or (year%100==0):
    print('this is a leap year')
else:
    print('this is not a leap year')
