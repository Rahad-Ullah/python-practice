# 1+2+3+4+....+n

n = int(input("Enter the last number:"))
sum = 0
for x in range(1, n, 1):
    sum = sum + x
    print(x)
print(sum)

