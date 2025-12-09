Team: Akshay_Shishir_Angel
Class: CSE 3461 Computer Networking

This project implements a multi-feature chat application using TCP sockets and Python threading. 
The application supports:



Feature 1 — Broadcast Chat
A server that relays each message to all connected clients.



Feature 2 — One-to-One Private Messaging
These clients can directly message one specific user using the format:
@username message



Feature 3 — GUI Chat Client (Tkinter)
A graphical chat interface (GUI) using the python library Tkinter for an improved user experience.

All features were tested in:

Simulation mode (localhost)

Over-the-air mode (LAN)




Feature 1 — Broadcast Chat
A TCP server accepts multiple clients. When any client sends a message, the server broadcasts it to all other active clients.

Key Behaviors

-Server maintains a list of connected clients.

-Each client runs a background thread to receive messages.

-Messages are forwarded to all connected clients.

# feature1.py
# Simple helper file describing how to run Feature 1 (Broadcast Chat)


Instructions:

def print_instructions():
    print("Feature 1: Broadcast Chat (Algorithm 1 & Algorithm 2)")
    print("This feature implements a basic multi-client chat system")
    print("where every message from one client is broadcast to all")
    print("other connected clients in real time.")
    print("1. Start the server (Algorithm 1):")
    print("   python3 feature1Alg1.py")
    print("   You may optionally specify a port inside the file.")
    print("2. Start clients (Algorithm 2) on the same or different machines:")
    print("   python3 feature1Alg2.py <server_ip> <server_port>")
    print("")
    print("   Examples:")
    print("   Localhost:")
    print("       python3 feature1Alg2.py 127.0.0.1 5050")
    print("   Over-the-air (LAN):")
    print("       python3 feature1Alg2.py <server LAN IP> 5050")
    print("3. After connecting, simply type messages to broadcast.")
    print("   All other clients will see them instantly.")
    print("4. To disconnect a client, type:")
    print("   /quit")


if __name__ == "__main__":
    print_instructions()

Files:

feature1Alg1.py

feature1Alg2.py




Feature 2 — One-to-One Private Messaging
Implements private messaging between clients using the format:

@target_username message text

Key Behaviors

-Server stores a dictionary: { username → socket }

-These clients register their username when they connect.

-Server routes messages ONLY to the specified user.

Instructions for feature 2:
# feature2.py
# Simple helper file describing how to run Feature 2 (one-to-one chat)

def print_instructions():
    print("Feature 2: One-to-One Chat / Private Messaging")
    print("")
    print("1. Start the server (Algorithm 3):")
    print("   python3 feature2Alg3.py <server_port>")
    print("   Example:")
    print("   python3 feature2Alg3.py 12000")
    print("")
    print("2. Start clients (Algorithm 4) on same or different machines:")
    print("   python3 feature2Alg4.py <server_ip> <server_port>")
    print("   Example (localhost):")
    print("   python3 feature2Alg4.py 127.0.0.1 12000")
    print("")
    print("3. When prompted, enter a username for each client.")
    print("4. To send a private message, use the format:")
    print("   @target_username your message here")
    print("")
    print("5. To quit a client, type:")
    print("   /quit")
    print("")


if __name__ == "__main__":
    print_instructions()

Files:

feature2Alg3.py

feature2Alg4.py



Feature 3 — GUI Chat Interface (Tkinter)
Description

A graphical chat client that connects to the broadcast server (Feature-1) and supports:

Scrollable chat window

Message typing box

Send button

Automatic real-time display of incoming messages


Instructions:
# feature3.py
# Simple helper file describing how to run Feature 3 (GUI Chat Client)

def print_instructions():
    print("Feature 3: Tkinter GUI Chat Client")
    print("This feature extends Feature 1 by providing a graphical")
    print("chat interface built with tkinter. Messages are still sent")
    print("using the Feature 1 broadcast server.")
    print("1. Start the broadcast server (Feature 1 / Algorithm 1):")
    print("   python3 feature1Alg1.py")
    print("   The GUI requires the broadcast server running in background.")
    print("2. Start the GUI Chat Client:")
    print("   python3 feature3_gui.py <server_ip> <server_port>")
    print("   Examples:")
    print("   Localhost:")
    print("       python3 feature3_gui.py 127.0.0.1 5050")
    print("   Over-the-air (LAN):")
    print("       python3 feature3_gui.py <server LAN IP> 5050")
    print("3. Features Included:")
    print("   Scrollable chat window")
    print("   Input text box + send button")
    print("   Threaded receiver to prevent GUI freezing")
    print("   Real-time broadcast chat from all clients")
    print("4. Closing the GUI window automatically disconnects the client.")
    print("Notes:")
    print("Tkinter is part of Python's standard library — no install needed.")
    print("Must connect to the Feature 1 server ONLY.")
    print("Can run multiple GUI windows at once for testing.")


if __name__ == "__main__":
    print_instructions()

File

feature3_gui_client.py