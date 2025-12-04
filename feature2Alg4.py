# feature2Alg4.py
import sys
import threading
from socket import *

# Usage: python3 feature2Alg4.py <server_ip> <server_port>
if (len(sys.argv) < 3):
    print("Usage: python3 " + sys.argv[0] + " server_ip server_port")
    sys.exit(1)
assert(len(sys.argv) == 3)

serverName = sys.argv[1]          # e.g., "127.0.0.1"
serverPort = int(sys.argv[2])     # e.g., 12000

# Create a TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server using the server’s IP address and port
clientSocket.connect((serverName, serverPort))

# Wait for the server to request a username
prompt = clientSocket.recv(1024)
if prompt:
    print(prompt.decode(), end='')  # e.g. "Enter username: "

# Input the username from the user and send it to the server
username = input()
clientSocket.send(username.encode())


def receive_messages():
    """
    Background thread:
    Continuously receive incoming messages from the server
    and display them to the user.
    """
    while True:
        data = clientSocket.recv(1024)
        if not data:
            # Server closed the connection
            print("\nConnection closed by server.")
            break
        print("\n" + data.decode())
    # When we break out of loop, ensure socket is closed
    try:
        clientSocket.close()
    except:
        pass


# Start a background thread to receive messages from server
receiver_thread = threading.Thread(target=receive_messages)
receiver_thread.daemon = True
receiver_thread.start()

print("You are logged in as:", username)
print("To send a private message, type: @username message")
print("Type /quit to exit.")

# In the main thread, repeatedly accept user input and send to server
while True:
    try:
        msg = input()
    except EOFError:
        break

    if msg == "/quit":
        break

    if len(msg) == 0:
        continue

    clientSocket.send(msg.encode())

# Close the socket connection
try:
    clientSocket.close()
except:
    pass