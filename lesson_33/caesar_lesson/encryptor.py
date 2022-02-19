import string
from decoder import to_decode

ALPHABET: str = ''.join([
    string.ascii_lowercase,
    string.ascii_uppercase,
    ])


def to_encrypt(key: int, data_for_cipher: str)->str:
    ciphered_data_as_list: list[str] = []
    for char in data_for_cipher:
        try:
            index = ALPHABET.index(char)
        except ValueError:
            new_char = char
        else:
            index_of_new_char = (index+key)%len(ALPHABET)
            new_char = ALPHABET[index_of_new_char]

        ciphered_data_as_list.append(new_char)
    return ''.join(ciphered_data_as_list)


if __name__ == '__main__':
    key = 2
    message = 'treE!'
    print(message == to_decode(key, to_encrypt(key, message)))
