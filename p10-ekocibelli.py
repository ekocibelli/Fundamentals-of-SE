"""
Created on Monday, Nov 11 2019
Author: Ejona Kocibelli
Project Description: Writing Regex's
"""
import re


def write_regex():
    """write_regex function gets a file input from the user, and looks for lines of the form New Revision: 39772,
     extract the number from each of the lines, and  prints out the average and the number of lines """
    file_name = input('Enter the file name: ')  # gets from user a file as an input
    try:
        fp = open(file_name, 'r')  # tries to open the file for reading
    except FileNotFoundError:
        print(f"File {file_name} cannot be opened")  # raises FileNotFoundError if the file cannot be opened
    else:
        with fp:
            find_pattern = re.findall(r'New Revision: (\d+)', fp.read())
            counter = 0  # initialize counter to 0
            total = 0  # initialize total to 0
            for line in find_pattern:
                counter += 1
                try:
                    total += int(line)
                except ValueError:  # raise a Value Error if New Revision: is not followed by integers
                    raise ValueError(f"Not integers found in line: {counter}")
            try:
                average = total / counter
            except ZeroDivisionError:  # raise a ZeroDivisionError if New Revision is not found in file
                raise ZeroDivisionError(f"There is no 'New Revision: ' in this file")
            else:
                print(f"Average is: {round(average, 1)}")
                print(f"Line count is: {counter}")


def main():
    try:
        write_regex()
    except ZeroDivisionError as zde:
        print(zde)
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    main()
