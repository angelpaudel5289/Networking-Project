# simple chat interface using tkinter
from socket import *
import threading
from tkinter import *

server_ip = "127.0.0.1"
server_port = 5000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))

def add_msg(text):
    print(text)

def set_msg_callback(callback):
    global add_message
    add_msg = callback

def rcv_msgs():
    while True:
        try: 
            data = client_socket.recv(1024)
            if not data:
                add_msg("[Server disconnected]")
                break
            add_msg(data.decode())
        except:
            break

threading.Thread(target=rcv_msgs).start()

def send_msg_to_server(msg):
    try:
        client_socket.send(msg.encode())
    except:
        add_msg("[Connection lost]")

def close_connection():
    client_socket.close()
