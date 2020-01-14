"""
Created on Monday, Nov 5 2019
Author: Ejona Kocibelli
Project Description: Classic Books
"""

from operator import itemgetter
from string import punctuation


def classic_books():
    """Function classic_books reads a file and returns a summary of total words, total distinct words, the top 25 most
    frequent words and counts and the character frequency sorted from most frequent to least frequent characters"""
    file_name = input('Enter the file name: ')
    try:
        fp = open(file_name, 'r', encoding="utf-8")  # tries to open the file for reading
    except FileNotFoundError:
        print(f"File {file_name} cannot be opened")  # raises FileNotFoundError if the file cannot be opened
    else:
        with fp:
            alphabet_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0,
                              "l": 0, "m": 0,
                              "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                              "y": 0, "z": 0}  # keys: alphabet_characters values: number of occurrence of each char
            counts = dict()
            for line in fp:
                line = line.rstrip()
                punc_translator = str.maketrans({key: None for key in punctuation})  # remove punctuation from the file
                line = line.translate(punc_translator)
                line = line.lower()
                words = line.split()
                if words is not []:
                    for word in words:
                        if word.isalpha():
                            if word in counts:
                                counts[word] += 1
                            else:
                                counts[word] = 1
                            for character in word:
                                alphabet_count[character] += 1

        most_frequent_words = sorted(counts.items(), key=itemgetter(1), reverse=True)  # sorted most frequent words and counts
        character_frequency = sorted(alphabet_count.items(), key=itemgetter(1), reverse=True)  # sorted char frequency

        print("The number of total words is: ", sum(counts.values()))  # print total words
        print("The number of distict words is: ", len(counts))  # print distint words
        print("The 25 most frequest used words are:", most_frequent_words[:25])  # print 25 most freq words and counts
        print("The frequency of each character: ", character_frequency)  # print each character and the frequency


def main():
    classic_books()


if __name__ == '__main__':
    main()
