from socket import *
from select import *


class SocketServer:


    def __init__(self, host = '', port = 10000):

        self.HOST = host
        self.PORT = port
        self.BUFSIZE = 1024
        self.ADDR = (HOST, PORT)
        #server socket init
        self.ServerScoket = socket(AF_INET, SOCK_STREAM)
        self.ClientSocket = 0

    def Connection(self):


        self.ServerScoket.bind(self.ADDR)
        print("ADDRESS BIND")

        self.ServerScoket.listen(100)
        print("SERVER LISTEN")

        self.ClientSocket, addr_info = self.ServerScoket.accept()
        if self.ClientSocket:
            print("ACEEPT")
            print("CLIENT INFOMATION : " + str(self.ClientSocket))
            print("CONNECTION SUCCESS")
            return 1
        else:
            print("CONNECTION FAIL")
            return 0

        return 0
    def LoadData(self):

        data = self.ClientSocket.recev(65535)

        if (data):
            print("RECEIVE DATA : " + str(data.decode()))
            return 1
        else:
            print("NOT RECEIVE DATA")
            return 0

        return 0
    

if __name__ == "__main__":
    print("THIS MODULE IS NOT STANDALONE")
    print("JUST SERVER")