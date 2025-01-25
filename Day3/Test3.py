import random

def guessNumber():
    numbertoguess = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        if user_guess < numbertoguess:
            print("Too Low!")
        elif user_guess > numbertoguess:
            print("Too High!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
guessNumber()