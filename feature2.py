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
