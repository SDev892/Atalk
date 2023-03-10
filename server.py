import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9999))
server.listen()

while True:
    comunication_bot,address_client = server.accept()
    message_of_client = comunication_bot.recv(1024)
    comunication_bot.send("Welcome To Atalk!".encode("utf-8"))
    if comunication_bot.decode('utf-8') == "Quit":
        comunication_bot.close()
    else:
        print(message_of_client.decode('utf-8'))
