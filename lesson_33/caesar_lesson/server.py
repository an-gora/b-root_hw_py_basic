import socket
import string
from parsing import to_parse
from cryptographer import to_encrypt
from decoder import to_decode

# Create a TCP/IP socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
server.bind(server_address)

# Listen for incoming connections
server.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = server.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                flag, key, data_for_cipher = to_parse(data)
                if flag == 'i_want_to_cipher'
                    ciphered_data = to_encrypt(key, data_for_cipher)
                    print('sending data back to the client')
                    connection.sendall(ciphered_data.encode('utf-8'))
                elif:
                    ciphered_data = to_encrypt(key, data_for_cipher)
                    print('sending data back to the client')
                    connection.sendall(ciphered_data.encode('utf-8'))

            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()