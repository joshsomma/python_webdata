# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
mylist = []
mydata = soup('span')
for myspan in mydata:
    # prints the contents of the span tag
    # print myspan
    # print the content of the span
    # print 'Span:',myspan.contents[0]
    # convert span contents to integer
    # num = int(myspan.contents[0])
    # add number to list
    mylist.append(int(myspan.contents[0]))
print sum(mylist)
