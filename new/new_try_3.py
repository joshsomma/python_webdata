# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Position - ')
count = raw_input('Count - ')
links = []
newLink = ''

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')

##############
# HEY REMEMBER YOU NEED TO OPEN THE NEW FILE WITH URLLIB AND READ THE CONTENTS TO GET THE NEXT URL!
# DUHHHHH!
##############

# set up helper functions
def retrieveUrl(startUrl):
    global tags, newLink
    newLink = tags[int(pos)].get('href')
    return newLink

for i in range(0, int(count)):
    retrieveUrl(url)
    links.append(newLink)
    print "Retrieving URL: ", links
