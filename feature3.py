import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

class ChatClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Broadcast Chat - Feature 3 GUI")

        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state="disabled")

        self.entry_msg = tk.Entry(master, width=40)
        self.entry_msg.pack(side=tk.LEFT, padx=10, pady=10)

        self.send_btn = tk.Button(master, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.LEFT)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

        recv_thread = threading.Thread(target=self.receive_messages)
        recv_thread.daemon = True
        recv_thread.start()

    def send_message(self):
        """Send message to server when user clicks Send"""
        msg = self.entry_msg.get()
        if msg.strip() == "":
            return
        try:
            self.client_socket.send(msg.encode())
            self.entry_msg.delete(0, tk.END)
        except:
            self.display_message("Connection lost.\n")

    def receive_messages(self):
        """Background thread to receive incoming messages"""
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    self.display_message("Server disconnected.\n")
                    break
                self.display_message(data.decode() + "\n")
            except:
                break

    def display_message(self, msg):
        """Safely update GUI text area"""
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, msg)
        self.chat_area.yview(tk.END)
        self.chat_area.config(state="disabled")


def main():
    root = tk.Tk()
    gui = ChatClientGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
