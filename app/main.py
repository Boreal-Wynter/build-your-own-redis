import socket  # noqa: F401


def accept_client(connection):
    while connection:
        # Wait for 'Ping'
        connection.recv(1024)
        # Send a 'Pong' Response
        connection.sendall(b"+PONG\r\n")


def main():
    # Create a server
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        # Wait for a client connection
        connection, _ = server_socket.accept()
        accept_client(connection)


if __name__ == "__main__":
    main()
