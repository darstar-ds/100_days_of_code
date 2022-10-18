from art import logo
import numpy as np
import os

def clear():
    # clear the terminal
     os.system("cls")

def low_high(the_number, user_guess):
    # is the guess right?
    if the_number>user_guess:
        communicate = "Too low. \nGuess again."
        is_finished = False
    elif the_number<user_guess:
        communicate = "Too high. \nGuess again."
        is_finished = False
    else:
        communicate = "You are right!!!"
        is_finished = True
    return communicate, is_finished

def guess_until_guessed(guess_no, the_number, is_game_finished):
    # repeat guessing until success or no more attempts
    while is_game_finished == False and guess_no > 0: 
        print(f"You have {guess_no} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        # verify the guess and decide to continue the game
        communicate, is_game_finished = low_high(the_number, user_guess)
        print(communicate)
        guess_no -= 1
        if guess_no == 0:
            print("You have no more attempts. :-(")
        

def start_the_game():
    '''
    start the game
    clear the terminal
    choose the number
    choose the difficulty level
    '''
    clear()
    print(logo)
    print("Welcome to the Number guessing game!")
    print("I am thinking of a number from 1 to 100.")
    # choose random number from 0 to 100
    the_number = np.random.randint(1, 100)
    print(f"I think of {the_number}")
    # a user choose the difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        guess_no = 5
    else:
        guess_no = 10
    return guess_no, the_number

play_again = "y"
while not play_again == "n":
    is_game_finished = False
    guess_no, the_number = start_the_game()
    guess_until_guessed(guess_no, the_number, is_game_finished)
    play_again = input("Do you want to play again (y/n)? ")


