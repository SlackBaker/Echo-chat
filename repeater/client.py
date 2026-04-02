import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = ("Ip of your server")
ADDR = (SERVER, PORT)

#creates client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    #sends message
    client.send(msg.encode(FORMAT))
    #gets message
    response = client.recv(1025).decode(FORMAT)
    print(f"[SERVER]: {response}")

#main loop

while True:
    message = input("You:")
    send(message)
    if message == DISCONNECT_MESSAGE:
        break

client.close()