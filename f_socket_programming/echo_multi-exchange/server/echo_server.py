import socket

HOST = "127.0.0.1"
PORT = 7878

# Create an IPv4 stream-based socket to listen for incoming connection requests
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the server to the specified port at the specified IP address
    server_socket.bind((HOST, PORT))
    # Set the server to listen for incoming connection requests
    server_socket.listen()
    # Accept the next connection request
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
        session_established = True
        while session_established:
            # Read in the next message from the client's connection
            # 1024 is the max size for the incoming message
            data = conn.recv(1024)

            # If the incoming message is blank (i.e. it was a call to close the connection)
            if not data:
                session_established = False
                print(f"{addr} disconnected.")
            else:
                print(f"Message received: {data.decode('utf-8')}")
                conn.sendall(data)

        print(f"Client {addr} session terminated")
    print(f"Client {addr} connection terminated")
print("Server has ceased listening for connections")