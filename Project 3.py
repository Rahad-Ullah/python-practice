#ternary operator

num1= 50
num2= 60
num3= 70
max= (num1 if num1>num2 else num2)
print(max)


#logical operator
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)



#vowel - a,e,i,o,u
alphabet= "a"
if alphabet =="a" or alphabet =="e" or alphabet =="i" or alphabet =="o" or alphabet =="u":
    print("Vowel")
else:
    print("constant")


#Marksheet with Letter grade
marks= 65
if marks >=80 and marks <=100:
    print("A+")
if marks >=70 and marks <=79:
    print("A")

#Again
if 80 <= marks <=100:
    print("A+")
if 70 <= marks <=80:
    print("A")

#Loop
i=1
while i<=10:
    print(i)
    i=i+1
print("Programme End")


i=1
while i<=10:
    print(i)
    i=i+1
    