import socket  # noqa: F401
import threading


def pong_client(connection):
    while connection:
        # Wait for 'Ping'
        message = connection.recv(1024)
        print(f"info: {message}")
        # Send a 'Pong' Response
        connection.sendall(b"+PONG\r\n")


def main():
    # Create a server
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # Actively listen for clients
    while True:
        # Wait and creates a client connection
        conn, _ = server_socket.accept()
        # Create thread for client
        c_thread = threading.Thread(target=pong_client, args=(conn,))
        # Start client thread
        c_thread.start()


if __name__ == "__main__":
    main()


'''
$<length>\r\n<data>\r\n

'''
