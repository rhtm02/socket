import server
import client



if __name__ == "__main__":
    host = str(input("address : "))
    port = int(input("port : "))
    Server = server(host, port)

    
