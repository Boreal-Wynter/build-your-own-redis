import socket  # noqa: F401
import threading


def pong_client(connection):
    while connection:
        # Wait for 'Ping'
        ping = connection.recv(1024)
        # get ECHO command
        print(f"ping information: {ping}")
        decoded_ping = str(ping)
        ping_list = decoded_ping.split("\\r\\n")
        print(f"list: {ping_list[-2]}")
        pong = "+" + ping_list[-2] + "\\r\\n"
        encoded_pong = pong.encode('utf-8')
        # Send a 'Pong' Response
        connection.sendall(encoded_pong)


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
