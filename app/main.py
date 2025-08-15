import socket  # noqa: F401
import threading


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
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    threads = []
    for _ in range(2):
        t = threading.Thread(target=accept_client, args=server_socket).start()
        threads.append(t)
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
