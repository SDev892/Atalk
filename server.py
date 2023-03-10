import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.100.55', 9999))
server.listen()

communication_server,adreess_user = server.accept()
loop = True
while loop:
    print(communication_server.recv(1024).decode())
    communication_server.send(input("Message >").encode())





