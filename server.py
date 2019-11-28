from socket import *
from select import *


class SocketServer:


    def __init__(self, host = '127.0.0.1', port = 10000):

        self.REQUEST_LIST = ['todo','TODO','ToDo','Todo','cal','Cal','CAL']
        self.TODO_STACK = []
        self.OPERATOR = ["*","/","+","-"]

        self.HOST = host
        self.PORT = port
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)
        #server socket init
        self.ServerScoket = socket(AF_INET, SOCK_STREAM)
        self.ClientSocket = 0

        self.ServerScoket.bind(self.ADDR)
        self.ServerScoket.listen(100)
        print("SERVER SETTING")
    def Connection(self):
        self.ClientSocket, addr_info = self.ServerScoket.accept()
        if self.ClientSocket:
            print("ACEEPT")
            #print("CLIENT INFOMATION : " + str(self.ClientSocket))
            print("CONNECTION SUCCESS")
            return 1
        else:
            print("CONNECTION FAIL")
            return 0

        return 0
    def ParsingMsg(self, msg):
        lst = msg.split(' ')
        output = str() 
        temp = str()
        for i in lst:
            temp += i
        lst = temp.split('\'')
        for i in lst[1:]:
            output += i
        return output
    def precedence(self, op):
        if op == '(':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 3

    def Postfix(self, source):
        dst = []
        stack = []
        for i in source:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    t = stack.pop()
                    dst.append(t)
                stack.pop()
            elif (i in self.OPERATOR):
                while len(stack) != 0 and self.precedence(stack[-1]) >= self.precedence(i):
                    dst.append(stack.pop())
                stack.append(i)
            elif '0' <= i <= '9':

                dst.append(i)

        while len(stack) != 0:
            t = stack.pop()
            dst.append(t)

        return(dst)


    def Calculating(self, string):
        #add code for prefix calculating  
        postfixString = self.Postfix(string)
        numStack = []
        #for debug postfix
        print("prefix : " + str(postfixString))
        for i in postfixString:
            if (i not in self.OPERATOR):
                numStack.append(i)
            else:
                if (i == "*"):
                    temp = float(numStack.pop()) * float(numStack.pop())
                    numStack.append(temp)
                elif (i == "/"):
                    temp1 = float(numStack.pop()) 
                    temp2 = float(numStack.pop())
                    numStack.append(temp2 / temp1)
                elif (i == "+"):
                    temp = float(numStack.pop()) + float(numStack.pop())
                    numStack.append(temp)
                elif (i == "-"):
                    temp = float(numStack.pop()) - float(numStack.pop())
                    numStack.append(temp)
        if (len(numStack) != 1):
            print("RESULT STACK LEN IS NOT 1")
            return "ERROR"
        result = numStack.pop()
        return result

    def LoadData(self):

        data = self.ClientSocket.recv(65535)
        print(data)
        #data = self.ParsingMsg(str(data))
        #ADD code for server's service
        if (str(data) in self.REQUEST_LIST):
            if (data in self.REQUEST_LIST[0:3]):
                #self.TODO_STACK.append()
                print("IN STACK(type end for EXIT)")
                while(1):
                    data = self.ClientSocket.recv(65535)
                    #data = self.ParsingMsg(str(data))
                    if(data == 'end'):
                        break
                    self.TODO_STACK.append(data)
                    print("TODO LIST : " + str(self.TODO_STACK))
                    print("STACK DATA")
            else:
                print("CALCULATE SECTION")
                while(1):
                    #add code postfix method for calculating

                    data = self.ClientSocket.recv(65535)
                    #data = self.ParsingMsg(data)
                    result = self.Calculating(data)
                    if (result == "ERROR"):
                        print("ERROR CALCULATING")
                    print("Calculating Result : " + str(result))
            if (len(self.TODO_STACK) != 0):
                print("STACK : " + str(self.TODO_STACK))
            else:
                return 0
        elif (data == 'q'):

            return -1

        else:
            print("Command not supported")
            pass
        '''
        for debug connection 
        if (data):
            print("RECEIVE DATA : " + str(data.decode()))
            return 1
        else:
            print("NOT RECEIVE DATA")
            return 0
        '''
        return 0
    

if __name__ == "__main__":
    #print("THIS MODULE IS NOT STANDALONE")
    #print("JUST SERVER")
    Server = SocketServer(host = "127.0.0.1", port = 2222)
    Server.Connection()
    while(1):
        check = Server.LoadData()
        if (check == -1):
            break
    print("END SERVER")
