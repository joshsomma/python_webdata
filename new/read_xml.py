# import libs
import urllib
import xml.etree.ElementTree as ET

# prompt to enter data location
address = raw_input('Enter location: ')

print 'Retrieving', address

# open and store data from location
uh = urllib.urlopen(address)
data = uh.read()

# parse data in object
tree = ET.fromstring(data)

total = 0

for num in tree.iter('count'):
    #print num.text
    total += int(num.text)

print "The total is: ", total
