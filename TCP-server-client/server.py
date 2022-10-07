import socket
import threading # Roda diferentes blocos de codigo ao mesmo tempo

HEADER = 64 # valor maximo de bytes a ser recebido
PORT = 5050 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT!"

# Especifica a versao do ip (ipv4) e o protocolo de envio
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}]{msg}")
            conn.send("Msg received".encode('utf-8'))
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Espera por uma conexão e armazena nas variaveis conn e addr
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(F"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()




