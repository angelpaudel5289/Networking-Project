from socket import *
import threading
server_ip = "127.0.0.1"
server_port = 5555
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))

print("Connected to server: ", (server_ip, server_port) )
print("Your address: ", client_socket.getsockname())

def receive_msgs():
    while True: 
        try:
            data = client_socket.recv(200)
            if not data:
                print("Server disconnected.")
                break
            print(data.decode())
        except:
            break
thread = threading.Thread(target=receive_msgs)
thread.start()

while True:
    msg = input("")
    try:
        client_socket.send(msg.encode())
    except:
        print("Connection lost.")
        break
client_socket.close()
