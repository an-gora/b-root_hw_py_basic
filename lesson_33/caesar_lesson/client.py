import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

#вынести функционал запроса данных и тд из клиента и сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    # key = input('give me key: ')
    key = 5
    # data_for_cipher = input('give me data for cipher: ')
    data_for_cipher = 'tree!A'
    all_data_for_cipher = f'i_want_to_cipher {key} {data_for_cipher}'
    client.sendall(all_data_for_cipher.encode('utf-8'))
    data = client.recv(1024).decode('utf-8')

    all_data_for_decode = f'i_want_to_decode {key} {data}'
    client.sendall(all_data_for_decode.encode('utf-8'))
    data_after_decode = client.recv(1024).decode('utf-8')




print(f'Received: {data}')
print(f'Received: {data_after_decode}')