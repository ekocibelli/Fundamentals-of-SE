"""
Created on Monday, Sept 27 2019
Author: Ejona Kocibelli
Project Description: Guessing game: User tries to find the number computer is guessing in 6 tries.
"""
import sys
import random


def get_int(prompt):
    """get_int function gets an input from the user and makes sure that the input is a number,
       if not raises an exception and notifies user to enter a number"""
    while True:
        inp = input(prompt)
        try:
            return int(inp)
        except ValueError:
            print(f"Error: '{inp}' is not u number. Please type a number...")


def guessing_game(human_input, computer_guess):
    """guessing_game function has two parameters: human_input and computer_guess and returns 0, -1. 1 after comparing"""
    if human_input == computer_guess:
        return 0
    elif human_input > computer_guess:
        return -1
    else:
        return 1


def play_game():
    """play_game function: compares computer_guess with user_input and helps the user through the game with prints as
       too low, too high. If computer guess is guessed by user, prints in how many tries it was guessed, otherwise
       prints the computer guess"""
    computer_guess = random.randint(1, 20)
    name = input("Hello! What is you name ? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guess_taken = 1
    while guess_taken <= 6:
        human_input = get_int("Take a guess.")
        if 1 <= human_input <= 20:
            compare = guessing_game(human_input, computer_guess)
            if compare == -1:
                print("Your guess is too high.")
            elif compare == 1:
                print("Your guess is too low.")
            else:
                print('Good job ' + name + "! You guessed my number in " + str(guess_taken) + ' guesses!')
                sys.exit()
        else:
            print("Your number should be 1-20 range.")
        guess_taken += 1
    print('The number I was thinking of was ' + str(computer_guess))


if __name__ == '__main__':
    play_game()
