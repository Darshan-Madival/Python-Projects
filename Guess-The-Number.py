import random

number = random.randint(1, 100)

userguess = None
guess = 0

print("******Computer Has Guessed A Random Number From 1 To 100! It's Your Turn******")
while (userguess != number):
    userguess = int(input("Guess The number: "))
    if (userguess == number):
        print("You gussed right")
    else:
        print("You guessd Wrong")

    if (number < userguess):
        print("Lower number please")
    elif (number > userguess):
        print("Higer number please")
    guess += 1

print(f"You guessed in {guess} attempts ")






