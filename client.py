import socket

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_server.connect(("192.168.100.55", 9999))

loop = True
while loop:
    client_server.send(input("message >").encode())
    server_message = client_server.recv(1024).decode('utf-8')
    print(server_message)




