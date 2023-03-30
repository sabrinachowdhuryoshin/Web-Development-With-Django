' This code is a Python script that creates a simple HTTP server '
' that listens on port 9000 on the local host '
' When a client connects, the server sends an HTTP response '
' that says "Hello World" '

# import the Python socket module
# which provides low-level networking communication capabilities
from socket import *

# defines a function create_server() 
# that creates a new socket object using the socket() function 
# binds it to the local host on port 9000 using the bind() method
# listens for incoming connections using the listen() method

def create_server():

    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)

        # enters an infinite loop that accepts incoming client connections using the accept() method
        # when a connection is established, it reads data from the client using the recv() method 
        # decodes it as a UTF-8 string
        # splits the received data into lines using the split() method
        # prints the first line (assuming it's an HTTP request)
        # sends an HTTP response back to the client using the sendall() method
        # shuts down the socket for writing using the shutdown() method

        while(1):
            (clientsocket, address) = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if(len(pieces)>0):
                print(pieces[0])
            data = "HTTP/1.1 200 OK\r\n"
            data+= "Content-Type: text/html; charset=utf-8\r\n"
            data+= "\r\n"
            data+= "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

            # catches any exceptions that occur during execution
            # prints an error message
            # closes the server socket using the close() method
            # prints a message to the console 
            # telling the user to access the server at http://localhost:9000

    except KeyboardInterrupt:
        print('\nShutting down...\n')
    except Exception as exc:
        print('Error: \n')
        print(exc)
    
    serversocket.close()

print('Access http://localhost:9000')

# calls the create_server() function
create_server()
