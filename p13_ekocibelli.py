"""
Created on Monday, Dec 09 2019
Author: Ejona Kocibelli
Project Description: Data Visualization
"""
import matplotlib.pyplot as plt


def visualize_data():
    """Function visualize_data reads a file, counts and visualizes in a graph of number of emails sent per each day
    of the week"""
    file_name = input('Enter the file name: ')  # gets from user a file as an input
    try:
        fp = open(file_name, "r")  # tries to open the file for reading
    except FileNotFoundError:
        print(f"File {file_name} cannot be opened")  # raises FileNotFoundError if the file cannot be opened
    else:
        with fp:
            dd = {'Sun': 0, 'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0}  # initialize a dictionary
            for line in fp:
                line = line.strip("\n")
                from_position = line.find("From")  # looks for line starting with 'From'
                at_position = line.find("@")  # looks if the line is followed by @ at a further position
                line = line[-24:]
                at_reoccurence = line.find("@")  # looks if @ reoccures in the line again after the first occurence
                if from_position == 0 and at_position > 0 and at_reoccurence == -1:
                    line = line[:-21]
                    dd[line] += 1

            plt.bar(dd.keys(), dd.values(), align='center', alpha=1.0)

            plt.ylabel('Number of emails')
            plt.title('Emails per day')
            plt.show()


def main():
    visualize_data()


if __name__ == '__main__':
    main()
