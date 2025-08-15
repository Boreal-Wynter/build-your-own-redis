import socket  # noqa: F401
import threading


def pong_client(connection, address):
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
        conn, addr = server_socket.accept()
        c_thread = threading.Thread(target=pong_client, args=(conn, addr))
        c_thread.start()


if __name__ == "__main__":
    main()
