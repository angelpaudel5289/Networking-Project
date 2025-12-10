from socket import *
import threading

# Local host: "127.0.0.1"
# Over the air: "75.76.78.170"
# 0.0.0.0
server_ip = "75.76.78.170"
server_port = 5050
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))

print("Connected to server: ", (server_ip, server_port))
print("Your address: ", client_socket.getsockname())

username = input("Enter your username: ").strip()
if username == "":
    username = "Unknown"


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
    if msg.strip() == "":
        continue

    full_msg = f"{username}: {msg}"

    try:
        client_socket.send(full_msg.encode())
    except:
        print("Connection lost.")
        break

client_socket.close()
