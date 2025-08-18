n = int(input("Enter the last term:"))
sum = 0
k = 0
while k< n:
    sum = sum + k
    k = k + 1
    print(k)
    if k == 30:
        break
print(sum)