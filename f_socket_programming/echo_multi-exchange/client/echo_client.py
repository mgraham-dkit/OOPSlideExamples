import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 7878  # The port used by the server
keep_running = True

# Create an IPv4 stream-based socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Request a connection to a server running on a specific IP and port
    client_socket.connect((HOST, PORT))
    # While we want to continue the session with the server
    while keep_running:
        # Ask the user for data to be sent (or if they want to end)
        msg = input("Enter a message to be sent (-1 to end): ")
        # If they want to end the session
        if msg != "-1":
            # Send the message (must be sent as a bytestring)
            # sendall will repeat the send action until all data is transmitted
            # This covers larger payloads
            client_socket.sendall(bytes(msg, "utf-8"))
            print("Data sent.")

            # Receive the incoming message - message can be up to 1024 bytes in size and will be a bytestring
            # Receiving is a BLOCKING action - the program will wait here until it receives something
            data = client_socket.recv(1024)
            # Convert from a bytestring to standard string for display
            print(f"Received: {data.decode('utf-8')}")
            # Alternative approach to converting from bytestring to string:
            # print(f"Received: {str(data, 'utf-8')}")
        else:
            keep_running = False

print("Connection terminated.")
