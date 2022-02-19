import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65428  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print('server is listeting and ready to cipher')
    conn, addr = server.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            data_to_cipher = 'tree'
            alphabet = ' abcdefghijklmnopqrstuvwxyz'
            res = ''
            for char in data_to_cipher:
                # res += alphabet[(alphabet.index(char) + 4) % len(alphabet)]
                res += alphabet[(alphabet.index(char) + int.from_bytes(data, byteorder='big', signed=True)) % len(alphabet)]
            if not data:
                break
            conn.sendall(res.encode('utf-8'))
