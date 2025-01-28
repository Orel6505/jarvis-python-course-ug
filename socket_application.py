import socket

def start_chat(role, host, port, partner_ip=None, partner_port=None):
    """
    Starts a chat where two users take turns sending and receiving messages.

    :param role: 'server' or 'client'
    :param host: Local host IP for the server or client
    :param port: Port for the server or client
    :param partner_ip: IP of the other user (for client role only)
    :param partner_port: Port of the other user (for client role only)
    """
    if role == 'server':
        # Set up as a server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(1)
        print(f"Server listening on {host}:{port}")
        conn, addr = sock.accept()
        print(f"Connection established with {addr}")

        while True:
            # Wait for the client's message
            message = conn.recv(1024).decode('utf-8')
            print(f"Client: {message}")

            # Get server's response
            response = input("You (Server): ")
            conn.send(response.encode('utf-8'))

    elif role == 'client':
        # Set up as a client
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((partner_ip, partner_port))
        print(f"Connected to server at {partner_ip}:{partner_port}")

        while True:
            # Send message to the server
            message = input("You (Client): ")
            sock.send(message.encode('utf-8'))

            # Wait for the server's response
            response = sock.recv(1024).decode('utf-8')
            print(f"Server: {response}")
    else:
        print("Invalid role. Please choose 'server' or 'client'.")

if __name__ == "__main__":
    role = input("Start as [S]erver or [C]lient? ").strip().lower()

    if role == 's':
        host = socket.gethostbyname(socket.gethostname())  # Get local IP
        port = int(input("Enter port to host the server on (e.g., 12345): "))
        start_chat('server', host, port)

    elif role == 'c':
        partner_ip = input("Enter server IP to connect to: ").strip()
        partner_port = int(input("Enter server port: "))
        start_chat('client', None, None, partner_ip, partner_port)

    else:
        print("Invalid input. Please restart and choose [S]erver or [C]lient.")



#with concurrency:
#         import socket
# import threading

# def receive_messages(sock):
#     """Thread function to continuously receive messages from the other user."""
#     while True:
#         try:
#             message = sock.recv(1024).decode('utf-8')
#             if message:
#                 print(f"\nReceived: {message}")
#             else:
#                 break  # Connection closed
#         except Exception as e:
#             print(f"Error receiving message: {e}")
#             break

# def start_chat(role, port, partner_ip=None, partner_port=None):
#     """
#     Starts a chat with multithreaded message receiving.

#     :param role: 'server' or 'client'
#     :param port: Port for the server or client
#     :param partner_ip: IP of the other user (for client role only)
#     :param partner_port: Port of the other user (for client role only)
#     """
#     if role == 'server':
#         # Automatically fetch the local IP
#         host = get_server_ip()
#         print(f"Server is running on IP: {host}, Port: {port}")

#         # Set up as a server
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.bind((host, port))
#         sock.listen(1)
#         print("Waiting for a connection...")
#         conn, addr = sock.accept()
#         print(f"Connection established with {addr}")

#         # Start a thread for receiving messages
#         threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

#         # Main thread handles sending messages
#         while True:
#             message = input("You (Server): ")
#             conn.send(message.encode('utf-8'))

#     elif role == 'client':
#         # Connect to the server
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((partner_ip, partner_port))
#         print(f"Connected to server at {partner_ip}:{partner_port}")

#         # Start a thread for receiving messages
#         threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

#         # Main thread handles sending messages
#         while True:
#             message = input("You (Client): ")
#             sock.send(message.encode('utf-8'))

# def get_server_ip():
#     """Returns the local machine's IP address."""
#     hostname = socket.gethostname()  # Get the local machine's hostname
#     local_ip = socket.gethostbyname(hostname)  # Resolve hostname to IP
#     return local_ip

# if __name__ == "__main__":
#     role = input("Start as [S]erver or [C]lient? ").strip().lower()

#     if role == 's':
#         port = int(input("Enter port to host the server on (e.g., 12345): "))
#         start_chat('server', port)

#     elif role == 'c':
#         partner_ip = input("Enter server IP to connect to: ").strip()
#         partner_port = int(input("Enter server port: "))
#         start_chat('client', None, partner_ip, partner_port)

#     else:
#         print("Invalid input. Please restart and choose [S]erver or [C]lient.")