"""
Created on Monday, Nov 18 2019
Author: Ejona Kocibelli
Project Description: Web Browser
"""
from urllib.request import urlopen
import urllib
import re


def web_browser():
    """web_browser function gets a url input from the user, looks for links in that url, and  prints out the total
       number of unique links parsed from the URL"""
    try:
        url = input('Enter a URL: ')
        url = url.lower()
    except EOFError:
        print("Input was interrupted. EOF command given!")  # raise an error if input is interrupted, or EOF
    else:
        if url.startswith('http://') or url.startswith('https://'):
            try:
                html = urllib.request.urlopen(url).read()  # reads the url
            except urllib.error.URLError:
                print(f"This URL {url} cannot be opened.")  # raise an error if the url is not valid, or cannot open
            else:
                links = re.findall(b'"(http[s]?://.*?)"', html)  # find links in the url
                total_links = set()
                for link in links:
                    link = link.decode()
                    link = link.lower()
                    total_links.add(link)  # add link into a set where we have all the links saved
                result = len(total_links)
                if len(links) > 0:  # if there were links found print out the number of links
                    print(f'There are {result} unique links parsed from your URL.')
                else:   # if there is no links, print out there were no links found
                    print("The program did not find any links!")
        else:  # if the url is not valid, print a message to the user to enter a valid url
            print('This URL is invalid! Please make sure it starts with http(s):// and try again.')


def main():
    web_browser()


if __name__ == '__main__':
    main()
