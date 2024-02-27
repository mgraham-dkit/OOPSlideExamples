import socket

# Step 1: Establish location information for service - SERVER'S location
HOST = "127.0.0.1"
PORT = 7878

# Step 2: Set up an IPv4 stream-based socket to listen for incoming connection requests
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Step 3: Bind the connection socket to the specified port at the specified IP address
    server_socket.bind((HOST, PORT))
    # Step 4: Set the server to listen for incoming connection requests
    server_socket.listen()
    # Step 5: Accept the next connection request
    '''
        accept will return two values:
            conn: the connection to be used
            addr: the address of the client currently connecting
    '''
    conn, addr = server_socket.accept()
    # Mark the following block as using the connection to the new client
    # This will ensure the connection is closed (on the server's side) when the block ends
    with conn:
        # Display where the connection came from
        print(f"Connection request from {addr} accepted")

        # Read in the message from the client's connection
        # 1024 bytes is the max size for the incoming message
        data = conn.recv(1024)
        # Display the message so we know what was received
        print(f"Message received: {data.decode('utf-8')}")
        # Send the echoed message back to the client
        conn.sendall(data)

    # The current client has disconnected and their connection has closed
    print(f"{addr} disconnected.")

# As the server is designed for a single exchange,
# the program will cease to listen for messages after one has been processed
print("Server terminating")