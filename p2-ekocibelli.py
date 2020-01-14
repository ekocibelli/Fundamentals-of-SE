"""
Created on Monday, Sept 16 2019
Author: Ejona Kocibelli
Project Description: A simple project that converts numeric scores to grades.
"""


def get_score(prompt):
    """get score function gets an input from the user and makes sure that the input is a number,
       if not raises an exception and notifies user to enter a number"""
    while True:
        inp = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not u number. Please try again...")


def score_to_grade():
    """score_to_grade function calls function get_score and gets an input from user. If the user's input is a score
    number from 1-100, prints the grade that belongs to that score. If the score number entered by user is not in 1-100
    range, notifies the user that the number is not in the range and asks the user to enter another score btw 1-100"""
    user_input = get_score("Enter a score 0-100: ")
    while 0 <= user_input <= 100:
        if user_input >= 93:
            print("A")
        elif 90 <= user_input < 93:
            print("A-")
            break
        elif 87 <= user_input < 90:
            print("B+")
            break
        elif 83 <= user_input < 87:
            print("B")
            break
        elif 80 <= user_input < 83:
            print("B-")
            break
        elif 70 <= user_input < 80:
            print("C")
            break
        else:
            print("F")
            break
    else:

        print("Error:", {user_input}, " is not in the range. Please try again...")
        return score_to_grade()


def main():
    """Main function"""
    score_to_grade()


if __name__ == "__main__":
    main()