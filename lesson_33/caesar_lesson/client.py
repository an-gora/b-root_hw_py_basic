import socket
from common_data import HOST, PORT, FLAG_TO_CIPHER, FLAG_TO_DECODE

#вынести функционал запроса данных и тд из клиента и сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    # key = input('give me key: ')
    key = 5
    # data_for_cipher = input('give me data for cipher: ')
    data_for_cipher = 'tree!A'
    all_data_for_cipher = f'{FLAG_TO_CIPHER} {key} {data_for_cipher}'
    client.sendall(all_data_for_cipher.encode('utf-8'))
    data = client.recv(1024).decode('utf-8')

    all_data_for_decode = f'{FLAG_TO_DECODE} {key} {data}'
    client.sendall(all_data_for_decode.encode('utf-8'))
    data_after_decode = client.recv(1024).decode('utf-8')


print(f'ciphered data: {data}')
print(f'decoded data: {data_after_decode}')