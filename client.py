from socket import *
from select import *
import sys
from time import ctime

class SocketClient:

    def __init__(self, host = '127.0.0.1', port = 10000):
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




    



if __name__ == "__main__":
    #print("THIS MODULE IS NOT STANDALONE")
    #print("JUST CLIENT")

    Client = SocketClient(host = "127.0.0.1", port = 2222)
    Client.Connection()
    while(1):
        msg = input('type your message(EXIT q) : ')
        if (msg == 'q'):
            break
        Client.SendMessage(msg)
    print("END CLIENT")
