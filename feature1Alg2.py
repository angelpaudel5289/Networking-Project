import socket
import threading

server_ip = "127.0.0.1"
server_port = 5555  # Must match server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

print("Connected to server:", (server_ip, server_port))
print("Your address:", client_socket.getsockname())

def receive_messages():
    """Handles receiving messages from the server in the background."""
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Server disconnected.")
                break
            print(data.decode())
        except:
            break

# Start background thread
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

# Main thread sends user messages
while True:
    try:
        msg = input("")
        client_socket.send(msg.encode())
    except:
        print("Connection lost.")
        break

client_socket.close()
