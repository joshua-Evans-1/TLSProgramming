import socket
import ssl

def start_server(port):
    """Start the file transfer server.
    
    Args:
        port (int): Port on which the server should listen.
    """

    # Assert port is a valid value
    assert 1024 <= port <= 65535, "Port number should be between 1024 and 65535."

    # Create the server socket using IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(5)  # Listen with a backlog of 5 connections

    # Set up the SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='../../certs/cert.pem', keyfile='../../certs/key.pem')
    print(f"Server listening on port {port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Wrap the socket to secure it using TLS
        secureConnection = context.wrap_socket(client_socket, server_side=True)

        # First, receive the 4-byte file name length
        file_name_length = int.from_bytes(secureConnection.recv(4), byteorder='big')

        try:
            # Now, receive the actual file name
            file_name = secureConnection.recv(file_name_length).decode()
            print(f"Receiving file named: {file_name}\n" + "*" * 80)

            # Receive the file content and save it
            with open(file_name, 'wb') as file:
                while True:
                    data = secureConnection.recv(1024)
                    if not data:
                        break
                    file.write(data)
                    
            print(f"Received file {file_name}")

        except Exception as e:
            print(f"Error: {e}")

        secureConnection.close()
        print(f"Connection with {client_address} closed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: server.py <PORT>")
        sys.exit(1)

    try:
        port = int(sys.argv[1])
        start_server(port)
    except ValueError:
        print("Port should be a number.")

