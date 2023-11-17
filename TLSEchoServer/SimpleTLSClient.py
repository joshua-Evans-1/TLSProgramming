import socket
import ssl

def handle_client(connection):
    """
    Handle the interaction with a connected client until they send 'exit'.
    """
    while True:
        try:
            sentence = connection.recv(1024).decode().strip()
            print(sentance)
            inp = input()
            connection.send(inp.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    server_ip = 'localhost'
    server_port = 12002
    # Set up the SSL context
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations("../certs/cert.pem")

    print("The server is ready to receive")

    while True:
        # Wrap the socket to secure it using TLS
        secureConnection = context.wrap_socket( client_socket, server_hostname=server_ip)
        secureConnection.connect((server_ip, server_port))
        # Handle client interaction
        handle_client(secureConnection)

        # Close the secure connection
        secureConnection.close()

if __name__ == "__main__":
    main()
