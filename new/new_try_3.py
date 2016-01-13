# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Position - ')
count = raw_input('Count - ')
i = 0

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')

while i < int(count):
    newLink = tags[int(pos) - 1].get('href')
    print "Retrieving URL: ", tags[int(pos) - 1].get('href')
    newHtml = urllib.urlopen(newLink).read()
    soup = BeautifulSoup(newHtml)
    tags = soup('a')
    i = i + 1
