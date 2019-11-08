from socket import *
from select import *
import sys
from time import ctime

class SocketClient:

    def __init__(self, host = '', port = 10000):
        self.HOST = host
        self.PORT = port
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)

        self.ClientSocket = socket(AF_INET, SOCK_STREAM)

    def Connection(self):
        self.ClientSocket.connect(self.ADDR)
        print("CONNECT")

    def SendMessage(self, msg):

        check = self.ClientSocket.send(str(msg).encode())

        if check:
            print("SEND SUCCESS")
        else:
            print("SEND 0 BYTE")
    def EndConnection(self):

        self.ClientSocket.send('end'.encode())

        print("END CONNECTION")


    



if __name__ == "__main__":
    print("THIS MODULE IS NOT STANDALONE")
    print("JUST CLIENT")




