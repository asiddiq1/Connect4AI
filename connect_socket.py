

import socket

#Sockets 

from collections import namedtuple
socketcon = namedtuple('socketcon', 'Socket input output')

 

def read_host() -> str:
    '''Asks the user to specify what host they'd like to connect to
    '''

    while True:
        host = input('Host: ').strip()

        if host == '':
            print('Please specify a host (either a name or an IP address)')
        else:
            return host

def read_port() -> int:
    '''Asks the user to specify what port they'd like to connect to
    '''

    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')


def username()->str:
    '''Asks the user their username
    '''
    return input('Username:')
    


def connect(host:str, port:str):
    '''Connects to the echo server
    '''

    my_socket = socket.socket()
    my_socket.connect((host, port))

    my_socket_input = my_socket.makefile('r')
    my_socket_output = my_socket.makefile('w')

    return socketcon(my_socket, my_socket_input, my_socket_output)


def close_sockets(socketcon: 'connection'):
    '''Closes the connection
    '''

    socketcon.Socket.close()
    socketcon.input.close()
    socketcon.output.close()



def send_message(socketcon: 'connection', message:str):
    socketcon.output.write(message + '\r\n')
    socketcon.output.flush()


def recieve_message(socketcon: 'connection'):
    return socketcon.input.readline()[:-1]
  

#Similar to professors code examples (slightly modified)


    



    
    

    
            
        
    

    







