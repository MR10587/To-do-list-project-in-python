import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != number:
    if guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 10: "))
if guess == number:
    print("Congratulations! You've guessed the number:", number)

