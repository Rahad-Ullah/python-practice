#Prime number indicator
n = int(input("Enter the last number:"))
for x in range(2, n, 1):
    print(x)
div = n/x
if div == div.is_integer():
    print("The number is not a prime number")
else:
    print("The number is prime number")  
