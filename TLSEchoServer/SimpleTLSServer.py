import socket
import ssl

def handle_client(connection):
    """
    Handle the interaction with a connected client until they send 'exit'.
    """
    while True:
        try:
            sentence = connection.recv(1024).decode().strip()
            if sentence.lower() == 'exit':
                print("Client requested to exit.")
                break
            capitalizedSentence = sentence.upper()
            connection.send(capitalizedSentence.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    serverPort = 12002

    # Create a TCP/IP socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    serverSocket.bind(('', serverPort))

    # Listen for incoming connections
    serverSocket.listen(1)

    # Set up the SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='../certs/cert.pem', keyfile='../certs/key.pem')

    print("The server is ready to receive")

    while True:
        # Accept a new connection
        connectionSocket, addr = serverSocket.accept()
        print(f"Connection established with {addr}")

        # Wrap the socket to secure it using TLS
        secureConnection = context.wrap_socket(connectionSocket, server_side=True)

        # Handle client interaction
        handle_client(secureConnection)

        # Close the secure connection
        secureConnection.close()
        print(f"Connection with {addr} closed")

if __name__ == "__main__":
    main()
