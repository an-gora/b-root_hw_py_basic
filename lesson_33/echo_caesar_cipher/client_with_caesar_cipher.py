import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65428  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(input('give me key to caesar cipher: ').encode('utf-8'))
    data = client.recv(1024)

    #как передать 2+ строки ?????????????????????????????????????????

print('Received cipher', repr(data))
