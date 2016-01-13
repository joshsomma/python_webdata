# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Position - ')
count = raw_input('Count - ')
nextUrl = ""
names = []
i = 0

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# set up helper functions
def retrieveUrl(startUrl):
    global soup, nextUrl
    tags = soup('a')
    nextUrl = tags[int(pos)].get('href')
    print "Retrieving URL: ", nextUrl
    return nextUrl

#def retrieveLine(getPos):
    #global soup, names
    #tags = soup('a')
    #print "Retrieving URL: ", tags[int(pos)].get('href')
    #print "Retrieving Name: ", tags[int(pos)].string
    #names.append(tags[int(pos)].string)

retrieveUrl(url)
print "break"
retrieveUrl(nextUrl)
