"""
Created on Friday, Oct 25 2019
Author: Ejona Kocibelli
Project Description: Counting unique items
"""
from prettytable import PrettyTable


def count_unique_items():
    """count_unique_items function gets a file input from the user, and finds all the email addresses and the total
    number of emails sent by each email address. """
    file_name = input('Enter the file name: ')  # gets from user a file as an input
    try:
        fp = open(file_name, 'r')  # tries to open the file for reading
    except FileNotFoundError:
        print(f"File {file_name} cannot be opened")  # raises FileNotFoundError if the file cannot be opened
    else:
        d = dict()                                   # initialize a dictionary
        with fp:
            for line in fp:
                if line.startswith('From:'):
                    line = line.split()
                    email = line[1]
                    d[email] = d.get(email, 0) + 1

            if len(d) > 0:
                max_nr = 0
                email = ''
                for values in d:
                    if d[values] > max_nr:
                        max_nr = d[values]
                        email = values
                '''returns the email address with the most emails and the total number of emails send by the sender.'''
                pt = PrettyTable(field_names=['Email address that sent most emails', 'Total number of emails'])
                pt.add_row([email, max_nr])
                print(pt)
            else:
                """If there is no From: line in file print an error 'There is no 'From: ' in this file' """
                print("There is no 'From: ' in this file")


def main():
    count_unique_items()


if __name__ == '__main__':
    main()
