# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Position - ')
count = raw_input('Count - ')

# set up helper functions
def retrieve(getUrl,getPos):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print "Retrieving:", tags[int(pos)].get('href')
    getUrl = tags[int(pos)].get('href')

counter = 0
while (counter < count):
    retrieve(url,pos)
    counter += 1
