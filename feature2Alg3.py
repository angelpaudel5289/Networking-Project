# feature2Alg3.py
import sys
import threading
from socket import *

# Usage: python3 feature2Alg3.py <server_port>
if (len(sys.argv) < 2):
    print("Usage: python3 " + sys.argv[0] + " server_port")
    sys.exit(1)
assert(len(sys.argv) == 2)

serverPort = int(sys.argv[1])

# Create TCP server socket and bind it to an IP address and port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # server listens for incoming client connections

print("One-to-one chat server is ready to receive on port", serverPort)

# Dictionary to store username -> socket
clients = {}
clients_lock = threading.Lock()


def handle_client(connectionSocket, addr, username):
    """
    Client handler: receives messages from this client and sends them
    only to the intended target client (one-to-one).
    """
    print("Client handler started for user:", username, "from", addr)

    while True:
        # Wait to receive a message from the client
        data = connectionSocket.recv(1024)
        if not data:
            # Client disconnected
            break

        message = data.decode()
        if len(message) == 0:
            continue

        # Expect messages in format: @target_username message text
        if message[0] == '@':
            parts = message.split(' ', 1)
            if len(parts) < 2:
                # No message body
                error_msg = "Use correct format: @username message\n"
                connectionSocket.send(error_msg.encode())
                continue

            target_name = parts[0][1:]  # remove '@'
            msg_text = parts[1]

            # Look up target in dictionary
            with clients_lock:
                if target_name in clients:
                    target_socket = clients[target_name]
                    # Send message only to that specific target client
                    full_msg = username + " (private): " + msg_text
                    target_socket.send(full_msg.encode())
                else:
                    # Inform sender that target user not found
                    error_msg = "User " + target_name + " not found\n"
                    connectionSocket.send(error_msg.encode())
        else:
            # Inform sender to use correct format
            info_msg = "Use correct format: @username message\n"
            connectionSocket.send(info_msg.encode())

    # When the client disconnects, remove it from the dictionary
    print("Client", username, "disconnected")

    with clients_lock:
        if username in clients and clients[username] is connectionSocket:
            del clients[username]

    connectionSocket.close()


# Main server loop
while True:
    # Accept a new client connection
    (connectionSocket, addr) = serverSocket.accept()

    # Request and receive the client’s username
    connectionSocket.send("Enter username: ".encode())
    username_bytes = connectionSocket.recv(1024)
    if not username_bytes:
        connectionSocket.close()
        continue

    username = username_bytes.decode().strip()

    # Add username–socket pair to dictionary
    with clients_lock:
        clients[username] = connectionSocket

    print("New client connected:", username, "from", addr)

    # Start a new thread to handle communication with that client
    client_thread = threading.Thread(
        target=handle_client,
        args=(connectionSocket, addr, username)
    )
    client_thread.daemon = True
    client_thread.start()
