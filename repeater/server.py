import socket

PORT = 5050
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#creates the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("[STARTING] Server is loading...")

conn, addr = server.accept()
print(f"[CONNECTED] {addr}")

connected = True
while connected:
    #gets messages
    msg = conn.recv(1024).decode(FORMAT)

    if msg == DISCONNECT_MESSAGE:
        connected = False
        print(f"[Disconnected] client ahs left")

    print(f"[CLIENT] {msg}")

    #repeats
    conn.send(f"Echo: {msg}".encode(FORMAT))

conn.close()