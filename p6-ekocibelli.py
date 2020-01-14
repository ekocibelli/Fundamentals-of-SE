"""
Created on Monday, Oct 14 2019
Author: Ejona Kocibelli
Project Description: Slicing and dicing files
"""


def average_spam_confidence():
    """average_spam_confidence function gets a file input from the user, and finds the average spam confidence in that
    file"""
    file_name = input('Enter the file name: ')         # gets from user a file as an input
    try:
        fp = open(file_name, 'r')                      # tries to open the file for reading
    except FileNotFoundError:
        print(f"File {file_name} cannot be opened")    # raises FileNotFoundError if the file cannot be opened
    else:
        count = 0                                      # initialize a counter to 0
        total = 0                                      # initialize a total to 0
        with fp:
            for line in fp:
                if line.startswith('X-DSPAM-Confidence:'):
                    count = count + 1                  # if the line starts with X-DSPAM-Confidence, ups the count + 1
                    offset = line.find(' ')            # finds the position of it in line
                    value = line[offset:].rstrip()     # gets the float part
                    value = float(value)
                    total = total + value              # add the float part to the total
            if count > 0:
                '''if there is found at least one or more X-DSPAM-Confidence in file, return the average rounded by 
                4 decimals'''
                print('Average spam confidence: ', round((total / count), 4))
            else:
                """If there is no X-DSPAM-Confidence line in File print an error No X-DSPAM-Confidence Line Found """
                print('No X-DSPAM-Confidence Line Found')


def main():
    average_spam_confidence()


if __name__ == '__main__':
    main()
