' The code is a Python script that creates a socket object '
' connects to a remote server over a TCP connection '
' sends an HTTP GET request to retrieve a web page '
' prints out the contents of the web page received from the server '

# import the Python socket module
# which provides low-level networking functionality
import socket

# create a new socket object called mysock
# using the AF_INET and SOCK_STREAM constants
# AF_INET indicates that the socket will use the IPv4 address family
# while SOCK_STREAM indicates that the socket will use the TCP protocol
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the remote server at data.pr4e.org on port 80
# which is the default port for HTTP traffic
mysock.connect(('data.pr4e.org', 80))

# create an HTTP GET request for the web page 
# located at /page1.htm on the remote server
# encode it as a byte string using the encode() method
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# send the HTTP GET request to the remote server 
# using the send() method of the socket object
mysock.send(cmd)

# receive the response from the server in chunks of up to 512 bytes at a time 
# using the recv() method of the socket object
# the loop continues until the server has finished sending data 
# indicated by receiving an empty string
while True:
    data = mysock.recv(512)

    # checks if the length of the received data is less than 1 byte
    # indicating that the server has finished sending data
    # if so, it breaks out of the loop
    if len(data)  < 1:
        break
    
    # print out the received data
    # decoded as a string using the decode() method
    # with the end='' argument used to suppress the newline character
    # that would normally be printed at the end
    print(data.decode(), end='')

# close the socket connection to the server.
mysock.close()