import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
pos = raw_input('Position - ')
count = raw_input('Count - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# helper functions
def retrieve(getUrl,getPos):
    global pos
    data = urllib.urlopen(url).read()
    dataSoup = BeautifulSoup(html)
    dataLinks = []
    dataTags = soup('a')
    for tag in dataTags:
        dataLinks.append(tag.get('href', None))
    print "Retrieving:", dataLinks[int(pos) - 1]
    newUrl = dataLinks[int(pos) - 1]
    retrieve(newUrl,pos)

# counter = 0
# while (counter < count):
#    print retrieve(url,pos)
#    counter += 1
