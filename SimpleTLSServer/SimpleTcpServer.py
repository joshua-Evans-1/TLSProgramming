import socket

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
    serverPort = 12000

    # Create a TCP/IP socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the server address and port
    serverSocket.bind(('', serverPort))

    # Listen for incoming connections
    serverSocket.listen(1)

    print("The server is ready to receive")

    while True:
        # Accept a new connection
        connectionSocket, addr = serverSocket.accept()
        print(f"Connection established with {addr}")

        # Handle client interaction
        handle_client(connectionSocket)

        # Close the connection
        connectionSocket.close()
        print(f"Connection with {addr} closed")

if __name__ == "__main__":
    main()
