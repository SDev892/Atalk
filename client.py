import socket

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_server.connect(("localhost", 9999))

while True:
    def Send(message):
        client_server.send(message.encode('utf-8'))
        Bot_message = client_server.recv(1024).decode()
        print(Bot_message)


    Send(input('message >'))



