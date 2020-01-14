"""
Created on Monday, Oct 21 2019
Author: Ejona Kocibelli
Project Description: Finding unique strings
"""


def unique_email_addresses():
    """unique_email_addresses function gets a file input from the user, and finds all the unique addresses in that file
    file"""
    file_name = input('Enter the file name: ')         # gets from user a file as an input
    try:
        fp = open(file_name, 'r')                      # tries to open the file for reading
    except FileNotFoundError:
        print(f"File {file_name} cannot be opened")    # raises FileNotFoundError if the file cannot be opened
    else:
        set1 = set()
        with fp:
            for line in fp:
                if line.startswith('From:'):
                    offset = line.find('From:')            # finds the position of it in line
                    value = line[offset:].rstrip()         # gets the address part
                    set1.add(value)                        # adds it into a set
            if len(set1) > 0:
                '''if there is found at least one or more From: in file, return the length of the set which is 
                equivalent number of unique addresses '''
                print(f"There are {len(set1)} unique email addresses.")
            else:
                """If there is no From: line in file print an error No From: Line Found """
                print("No 'From:' Line Found.")


def main():
    unique_email_addresses()


if __name__ == '__main__':
    main()
