import socket  # noqa: F401


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
        server_socket.bind(("localhost", 6379))
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
