import socket
import threading

active_clients = []  # List of connected client sockets

def handle_client(client_socket, addr):
    """Handles messages from a single client and broadcasts them."""
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break  # client disconnected

            # Broadcast to all connected clients except sender
            for other in active_clients:
                    other.send(msg)

        except Exception:
            break

    # Remove and close when client disconnects
    print(f"[DISCONNECTED] {addr}")
    active_clients.remove(client_socket)
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Same port must match client
    HOST = "0.0.0.0"
    PORT = 5555
    
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        active_clients.append(client_socket)

        # Start a new thread for each client
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    main()
