"""
Created on Monday, Oct 7 2019
Author: Ejona Kocibelli
Project Description: Converting singular words to plurals
"""


def plural(s):
    """plural(s) is a function that gets from user an input which is a list of words and
    returns the plural form of the words or notifies if the input is not a string"""
    vowels = 'aeuio'
    sl = s.lower()
    lst = []

    for word in sl.split():
        if word.isalpha():                                       # checks if the input is a string
            if word.endswith('y') and word[-2] in vowels:        # checks if the word ends with ay,ey,uy,iy,oy
                new_word = (word[:] + 's')
            elif word.endswith('y') and word[-2] not in vowels:  # checks if word ends with y and not vowel precedent
                new_word = (word[:-1] + 'ies')
            elif word.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):   # checks if the word ends with o,ch,s,sh,x,z
                new_word = (word[:] + 'es')
            else:
                new_word = (word[:] + 's')                       # all other words
            lst.append(new_word)                                 # add all the new plural words in a list
        else:
            print(f"{word} is not a string.")                    # notifies if it is not a string

    print(lst)                                                   # print the list with plural words


def main():
    s = input("Enter a list of words: ")
    plural(s)


if __name__ == '__main__':
    main()
