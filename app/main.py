import socket  # noqa: F401


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # WAIT FOR A CLIENT CONNECTION
    '''
    socket.connect() returns (CONN, ADDRESS).
        CONN: Socket object that sends/recieves data on the connection.
        ADDRESS: the address bound to the socket of the client.
    '''
    connection, _ = server_socket.accept()
    # SEND A 'PONG' RESPONSE
    '''
    * Send data to the socket
    * Data is sent from bytes until all is sent or error occurs.
        * Return 'None' on success
        * Exception is raised on error
    bytes-like object: Object that supports buffer protocol and can export C-contiguous buffer.
        * bytes
        * bytearray
        * array.array
    '''
    connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
