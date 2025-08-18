numberofLetters = 0
numberofDigits = 0
numberofWords = 0

text = input("Enter a text include numbers: ")

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberofLetters = numberofLetters + 1
    elif x >= '0' and x <= '9':
        numberofDigits = numberofDigits + 1
    elif x == ' ':
        numberofWords = numberofWords + 1
print("Number of letters:",numberofLetters)
print("Number of Digits:",numberofDigits)
print("Number of Words:",numberofWords + 1)