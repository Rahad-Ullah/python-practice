#(2)^2+(4)^2+(6)^2+.....+n^2=?
n = int(input('Enter the number = '))
sum = 0
for x in range(2, n+1, 2):
    x = x*x
    sum = sum + x
    print(x)
print('sum of the series =', sum)
