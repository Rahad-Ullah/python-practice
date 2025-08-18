num1 = float(input("Enter the number 1=="))
num2 = float(input("Enter the number 2=="))
num3 = float(input("Enter the number 3=="))

if num1>num2 and num1>num3:
    print("The largest number is",num1)
elif num2>num3:
    print("The largest number is",num2)
else:
    print("The largest number is",num3)

ch = input("Enter the letter==")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
    print('Vowel')
else:
    print('Consonent')

