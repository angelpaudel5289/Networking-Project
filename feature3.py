# simple chat interface using tkinter
from socket import *
import threading
from tkinter import *

server_ip = "127.0.0.1"
server_port = 5000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))



