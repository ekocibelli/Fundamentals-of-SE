"""
Created on Monday, Sept 20 2019
Author: Ejona Kocibelli
Project Description: A simple project that finds the maximum of three values.
"""


def get_int(prompt):
    """get_int function gets an input from the user and makes sure that the input is a number,
       if not raises an exception and notifies user to enter a number"""
    while True:
        inp = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not u number. Please type a number...")


def maxOfThree():
    """maxOfThree function gets three values from the user, and returns the maximum value."""
    value1 = get_int("Enter first value: ")
    value2 = get_int("Enter second value: ")
    value3 = get_int("Enter third value: ")
    if value1 == value2 == value3:
        print("Three values are equal, enter values different from one another")
        return maxOfThree()
    else:
        if (value1 >= value2) and (value1 >= value3):
            largest = value1
        elif (value2 >= value1) and (value2 >= value3):
            largest = value2
        else:
            largest = value3

        print("The max of ", value1, ",", value2, "and", value3, "is", largest)


def main():
    """Main function"""
    maxOfThree()


if __name__ == "__main__":
    main()
