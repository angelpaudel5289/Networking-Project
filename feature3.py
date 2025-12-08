import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import queue

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

class ChatServer:
    def __init__(self):
        self.clients = []
        self.clients_lock = threading.Lock()
        self.broadcast_queue = queue.Queue()

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((SERVER_IP, SERVER_PORT))
        self.server_socket.listen(5)

        threading.Thread(target=self.accept_clients, daemon=True).start()
        threading.Thread(target=self.broadcast_from_queue, daemon=True).start()

    def accept_clients(self):
        while True:
            client, addr = self.server_socket.accept()
            with self.clients_lock:
                self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client,), daemon=True).start()

    def handle_client(self, client):
        while True:
            try:
                msg = client.recv(1024)
                if not msg:
                    with self.clients_lock:
                        if client in self.clients:
                            self.clients.remove(client)
                    break
                self.broadcast(msg)
            except Exception as e:
                print(f"Error handling client: {e}")
                with self.clients_lock:
                    if client in self.clients:
                        self.clients.remove(client)
                break

    def broadcast(self, msg):
        with self.clients_lock:
            for client in self.clients[:]:
                try:
                    client.send(msg)
                except Exception as e:
                    print(f"Error broadcasting to client: {e}")
                    self.clients.remove(client)

    def broadcast_from_queue(self):
        while True:
            msg = self.broadcast_queue.get()
            if msg is None:
                break
            self.broadcast(msg)


class ChatClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Announcement Chat - Server & Client")
        master.configure(bg="#f0f0f0")

        # Frames for split view
        self.frame = tk.Frame(master, bg="#f0f0f0")
        self.frame.pack(padx=10, pady=10)

        # Server Frame
        self.server_frame = tk.Frame(self.frame, bg="#e0f7fa", bd=2, relief=tk.GROOVE)
        self.server_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(self.server_frame, text="Server Announcements", bg="#e0f7fa",
                 font=("Helvetica", 12, "bold")).pack(pady=5)
        self.server_entry = tk.Entry(self.server_frame, width=30, font=("Helvetica", 12))
        self.server_entry.pack(pady=5)
        self.server_entry.bind("<Return>", lambda e: self.send_announcement())
        self.server_btn = tk.Button(self.server_frame, text="Send Announcement", command=self.send_announcement,
                                    bg="#4CAF50", fg="white")
        self.server_btn.pack(pady=5)

        # Client Frame
        self.client_frame = tk.Frame(self.frame, bg="#fff3e0", bd=2, relief=tk.GROOVE)
        self.client_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        tk.Label(self.client_frame, text="Client Messages", bg="#fff3e0",
                 font=("Helvetica", 12, "bold")).pack(pady=5)
        self.chat_area = scrolledtext.ScrolledText(self.client_frame, width=40, height=20,
                                                   font=("Helvetica", 12))
        self.chat_area.pack(pady=5)
        self.chat_area.config(state="disabled")

        # Setup client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_announcement(self):
        msg = self.server_entry.get().strip()
        if not msg:
            return
        try:
            server.broadcast_queue.put(msg.encode())
            self.server_entry.delete(0, tk.END)
        except Exception as e:
            self.display_message(f"Server not running: {e}\n")

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.display_message(data.decode() + "\n")
            except Exception as e:
                print(f"Error receiving messages: {e}")
                break

    def display_message(self, msg):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, msg)
        self.chat_area.yview(tk.END)
        self.chat_area.config(state="disabled")

if __name__ == "__main__":
    server = ChatServer()

    root = tk.Tk()
    gui = ChatClientGUI(root)
    root.mainloop()
