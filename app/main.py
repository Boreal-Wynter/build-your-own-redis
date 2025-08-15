import socket  # noqa: F401
import threading


def pong_client(connection):
    while connection:
        # Wait for 'Ping'
        ping = connection.recv(1024)
        # get ECHO command
        ping_list = list(ping)
        start_index = ping_list.index("$")
        echo_ping_list = ping_list[(start_index):]
        message = "+" + echo_ping_list
        bytes_object = bytes(message, 'utf-8')
        # Send a 'Pong' Response
        connection.sendall(bytes_object)


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
