# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import re

def checklink(link):
    result = requests.get(link)
    parsed = BeautifulSoup(result.text, 'html.parser')
    list1 = ['HIPAA', 'characteristic']
    if any(word in parsed.text for word in list1):
        print("found a word in " + link)
        #add link to a list or something? download pdf or somethin

def main(link):
    # Use a breakpoint in the code line below to debug your script.
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    titles = soup.find_all('h3')
    print(soup.text)
    #not sure  how to differentiate between http and https so loop for both :)
    for x in titles:
        print("test")
        link = x.find_all('a', attrs={'href': re.compile("^https://")})
        for y in link:
            checklink(y.get('href'))
        link = x.find_all('a', attrs={'href': re.compile("^http://")})
        for y in link:
            checklink(y.get('href'))
        print(x.text + "\n")
    next = soup.find_all('td', attrs={'align': 'left'})
    main(next.get('href'))

    #print(soup.div)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #plans to add command line functions that will allow the user give the search and key words
    main('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C36&q=Hipaa+breaches&btnG=')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
