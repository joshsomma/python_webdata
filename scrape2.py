# import libs
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('Count - ')
pos = raw_input('Position - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')


#def retrieve(getUrl,getPos):
#   result = urllib.urlopen(getUrl).read()
#   mySoup = BeautifulSoup(result)
#   myTags = soup('a')
#   newUrl = myTags[int(getPos)].get('href', None)
#   print "Retrieving:",myTags[int(getPos)].get('href', None)

print "Retrieving:",tags[int(2)].get('href', None)
nextUrl = tags[int(pos)].get('href', None)
mycount = 0
while (mycount < int(count)):
    "Retrieving:",tags[int(pos)].get('href', None)
    nextUrl = tags[int(pos)].get('href', None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    mycount += 1
