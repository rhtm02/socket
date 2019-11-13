import server
import client



if __name__ == "__main__":
    #host = str(input("address : "))
    #port = int(input("port : "))
    Server = server.SocketServer(host = "127.0.0.1", port = 2222)
    Client = client.SocketClient(host = "127.0.0.1", port = 2222)
    Client.Connection()
    Server.Connection()
    while(1):
        msg = input('type your message(EXIT q) : ')
        if (msg == 'q'):
            break
        Client.SendMessage(msg)
        Server.LoadData()
    
    print("END PROGRAM")
    
