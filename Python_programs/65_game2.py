import random 

number = random.randint(1, 6)
attempt = 0
guess = int(input("Your Turn: "))

while(True):
    if(guess==number):
        print("OUT")
        print(f"Yeah thats the number! You guessed it right in {attempt} attempts")
        break
    elif(guess!=number):
        
        guess = int(input("Guess another number. This one is too less: "))
        attempt=attempt+guess
        print("you scored",{attempt})

    # else:
    #     print(f"Yeah thats the number! You guessed it right in {attempt} attempts")
    #     break