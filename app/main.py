import socket  # noqa: F401


HOST = "localhost"
PORT = 6379


def accept_client(server_socket):
    # Wait for a client connection
    connection, _ = server_socket.accept()
    while connection:
        # Wait for 'Ping'
        connection.recv(1024)
        # Send a 'Pong' Response
        connection.sendall(b"+PONG\r\n")


def main():
    # Create a server
    with socket.create_server(("localhost", 6379), reuse_port=True) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        # Wait for a client connection
        connection, _ = server_socket.accept()
        while connection:
            # Wait for 'Ping'
            connection.recv(1024)
            # Send a 'Pong' Response
            connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
