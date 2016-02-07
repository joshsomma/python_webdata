# import libs
import json
import urllib

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    print "Retrieving", address
    response_data = urllib.urlopen(address).read()
    app_data = json.loads(response_data)
    total = []
    for item in app_data["comments"]:
        total.append(int(item["count"]))
    print sum(total)
