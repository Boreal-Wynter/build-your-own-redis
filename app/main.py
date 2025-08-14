import socket  # noqa: F401
import threading


def test(server_socket):
    # Wait for a client connection
    connection, _ = server_socket.accept()
    while connection:
        # Wait for 'Ping'
        connection.recv(1024)


def main():
    # Create a server
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    thread1 = threading.Thread(target=test, args=server_socket).start()
    thread2 = threading.Thread(target=test, args=server_socket).start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
