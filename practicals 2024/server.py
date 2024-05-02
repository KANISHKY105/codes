# echo-server.py

import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

clients = []

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        clients.append(conn)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            broadcast(data)

def broadcast(message):
    for client in clients:
        try:
            client.sendall(message)
        except:
            clients.remove(client)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
