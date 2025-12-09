import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import tkinter.simpledialog as simpledialog   


SERVER_IP = "127.0.0.1"
SERVER_PORT = 5555

class ChatClientGUI:
    def __init__(self, master, username):   
        self.master = master
        self.username = username            

        master.title("Broadcast Chat Client")
        master.configure(bg="#f0f0f0")
        
        container = tk.Frame(master, bg="#e8f4fa", bd = 3, relief=tk.GROOVE)
        container.pack(padx=20, pady=20)
        
        tk.Label(container, text = "Chat", bg="#e8f4fa", font=("Helvetica", 16, "bold")).pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(container, width =60, height = 20, font=('Helvetica', 14, "bold"), bg = "#ffffff", bd=2, relief=tk.SUNKEN)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state="disabled")

        input_frame = tk.Frame(container, bg="#e8f4fa")
        input_frame.pack(pady=5)

        self.entry = tk.Entry(input_frame, width=45, font=("Helvetica", 12))
        self.entry.grid(row=0, column=0, padx=5)
        self.entry.bind("<Return>", self.send_msg)


        send_button = tk.Button(input_frame, text = "Send", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", width = 10, command=self.send_msg)
        send_button.grid(row=0, column=1, padx =5)
       
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_msg(self, event=None):
            msg = self.entry.get().strip()
            if msg:
                full_msg = f"{self.username}: {msg}"   
                self.client_socket.send(full_msg.encode())
                self.entry.delete(0, tk.END)
        
    def receive_messages(self):
            while True:
                try:
                    data = self.client_socket.recv(1024)
                    if not data:
                        break
                    self.display_message(data.decode())
                except:
                    break
        
    def display_message(self, msg):
            self.chat_area.config(state="normal")
            self.chat_area.insert(tk.END, msg + "\n")
            self.chat_area.yview(tk.END)
            self.chat_area.config(state = "disabled")


if __name__ == "__main__":
        root = tk.Tk()
        
        username = simpledialog.askstring("Username", "Enter your username:")
        if not username:
            username = "Unknown"

        gui = ChatClientGUI(root, username)
        root.mainloop()
