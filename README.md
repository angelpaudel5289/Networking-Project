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

File

feature3_gui_client.py