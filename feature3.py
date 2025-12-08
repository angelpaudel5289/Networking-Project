import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, font

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

class ChatClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Broadcast Chat - Feature 3 GUI")
        master.configure(bg="#f0f0f0")  # light gray background

        # Main frame
        self.main_frame = tk.Frame(master, bg="#f0f0f0")
        self.main_frame.pack(padx=10, pady=10)

        # Label above chat area
        self.label_messages = tk.Label(
            self.main_frame, text="Messages", bg="#f0f0f0",
            fg="black", font=("Helvetica", 12, "bold")
        )
        self.label_messages.pack(pady=(0, 5))  # small space below label

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(
            self.main_frame, wrap=tk.WORD, width=50, height=20,
            bg="white", fg="black", font=("Helvetica", 12)
        )
        self.chat_area.pack(pady=(0, 10))  # some space below chat_area
        self.chat_area.config(state="disabled")

        # Frame for Send button above input field
        self.input_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.input_frame.pack()

        # Send button at top
        self.send_btn = tk.Button(
            self.input_frame, text="Send", command=self.send_message,
            bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), padx=10, pady=5
        )
        self.send_btn.pack(side=tk.TOP, fill=tk.X, pady=(0, 8))

        # Entry field below the send button
        self.entry_msg = tk.Entry(self.input_frame, width=40, font=("Helvetica", 12))
        self.entry_msg.pack(side=tk.TOP)
        self.entry_msg.focus()  # focus on entry by default

        # Bind Enter key to send message
        self.entry_msg.bind("<Return>", lambda event: self.send_message())

        # Setup socket connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

        # Start thread to receive messages
        recv_thread = threading.Thread(target=self.receive_messages)
        recv_thread.daemon = True
        recv_thread.start()

    def send_message(self):
        """Send message to server when user clicks Send or presses Enter"""
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
