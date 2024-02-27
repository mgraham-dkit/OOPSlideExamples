import socket

# Establish SERVER'S address information - this includes IP and port
HOST = "127.0.0.1"
PORT = 7878

# Create an IPv4 stream-based socket to communicate with the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Request a connection with the server
    client_socket.connect((HOST, PORT))

    # Take in the message to send
    msg = input("Enter a message to be sent: ")
    # Send the message (must be sent as a bytestring)
    # We use sendall to ensure all data is sent - send() will only send as much as it can fit into the socket's buffer
    client_socket.sendall(bytes(msg, "utf-8"))
    print("Data sent.")

    # Receive the response message from the server (setting 1024 bytes as the max allowable size)
    data = client_socket.recv(1024)
    # Display the received message (need to convert it from a bytestring to a standard string)
    print(f"Received: {data.decode('utf-8')}")
    # Alternative approach to converting from bytestring to string:
    # print(f"Received: {str(data, 'utf-8')}")

print("Connection terminated.")
