import socket

HEADER = 64 # valor maximo de bytes a ser recebido
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = "!DISCONNECT!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
client.connect(ADDR)

def send(msg):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))

send("Hello World!")
#send(DISCONNECT_MESSAGE)
