import socket
import threading

active_clients = []  

def handle_client(client_socket):
    """Client handler for receiving & broadcasting messages."""
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            for c in active_clients:
                if c != client_socket:
                    c.send(msg)
        except:
            break

    active_clients.remove(client_socket)
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen()

    print("[SERVER] Listening on port 5555...")

    while True:
        client_socket, _ = server.accept()
        active_clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

main()