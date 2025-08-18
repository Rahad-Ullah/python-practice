from random import randint

for x in range(1,10):
    guessNumber = int(input("Enter your guess between 1 to 5 : "))
    randomNumber = randint(1,5)
    if guessNumber == randomNumber:
        print("Yahoo! You have won!")
    else:
        print("Alas! You have lose!")
        print("Random number was:", randomNumber)