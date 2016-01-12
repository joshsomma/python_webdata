# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Position - ')
# count = raw_input('Count - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# set up helper functions
def retrieveLine(getPos):
    global soup
    tags = soup('a')
    print "Retrieving:", tags[int(pos)].get('href')

retrieveLine(pos)
