import socket

Server = input("enter a host to scan: ")
ServerIp = socket.gethostbyname(Server)

for port in range(1,100):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ServerIp,port))
    if result == 0:
        print("Port {}: Open".format(port))
    else:
        print("Port {}: Close".format(port))
    sock.close()
