#Using Python to Access Data on the Web
#Week 3 lesson

#import the socket library to make connections
import socket
#create the socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#open connection
mysock.connect(('joshsomma.com', 80))
#send request
mysock.send('GET http://joshsomma.com/stage.txt HTTP/1.0\n\n')

#process return data

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data;

#close connection
mysock.close()
