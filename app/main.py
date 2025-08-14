import socket  # noqa: F401


def main():
    # Create a server
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, _ = server_socket.accept()
    connection.listen(5)

    # Wait for a client connection
    connection, _ = server_socket.accept()
    while connection:
        # Wait for 'Ping'
        connection.recv(1024)
        # Send a 'Pong' Response
        connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
