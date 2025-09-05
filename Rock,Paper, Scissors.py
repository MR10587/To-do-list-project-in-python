import random

def user_choice():
    user_choice =  input("Rock, paper, or scissors: (r/p/s): ").strip().lower()
    while True:
        if user_choice == 'r':
            user_choice = 'rock'
            break
        elif user_choice == 'p':
            user_choice = 'paper'
            break
        elif user_choice == 's':
            user_choice = 'scissors'
            break
        else:
            print("Invalid choice. Please choose r, p, or s.")
            user_choice =  input("Rock, paper, or scissors: (r/p/s): ").strip().lower()

def computer_choice():
    computer_choice = random.choice(['r', 'p', 's'])
    if computer_choice == 'r':
        computer_choice = 'rock'
    elif computer_choice == 'p':
        computer_choice = 'paper'
    elif computer_choice == 's':
        computer_choice = 'scissors'

def game():
    user_choice = user_choice()
    computer_choice = computer_choice()
    if user_choice == computer_choice:
        print(f"You chose {user_choice} and the computer chose {computer_choice}.")
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 'p' and computer_choice == 'r') or \
        (user_choice == 's' and computer_choice == 'p'):
        print(f"You chose {user_choice} and the computer chose {computer_choice}.")
        print("You win!")
    else:
        print(f"You chose {user_choice} and the computer chose {computer_choice}.")
        print("You lose!")

def exit():
    exit_choice = input("Do you want to play again? (y/n): ").strip().lower()
    if exit_choice == 'y':
        game()
    elif exit_choice == 'n':
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid choice. Please choose y or n.")
        
