import random

## Prompts the user for a level
while True:
    user_input = input("Level: ")
    if user_input.isdigit() == True:
        if int(user_input) > 0:
            break

## Randomly generates an integer between 1 and user_input
level = random.randint(1, int(user_input))

## Prompt the user to guess that integer
while True:
    user_guess = input("Guess: ")
    if user_guess.isdigit() == True:
        if int(user_guess) > 0:
            if int(user_guess) < level:
                print("Too small!")
            elif int(user_guess) > level:
                print("Too large!")
            else:
                print("Just right!")
                break
