# echo-client.py

import socket
import threading

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def receive_messages(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())

def send_messages(sock):
    while True:
        message = input("Enter message: ")
        sock.sendall(message.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(s,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(s,))
    send_thread.start()

    receive_thread.join()
    send_thread.join()
