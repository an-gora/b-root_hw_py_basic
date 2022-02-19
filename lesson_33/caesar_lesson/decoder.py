import string


ALPHABET: str = ''.join([
    string.ascii_lowercase,
    string.ascii_uppercase,
    ])

#обьединить decode-crypto??? через operator из парсера математического выражения

def to_decode(key: int, data_to_decode: str)->str:
    ciphered_data_as_list: list[str] = []
    for char in data_to_decode:
        try:
            index = ALPHABET.index(char)
        except ValueError:
            new_char = char
        else:
            index_of_new_char = (index-key)%len(ALPHABET)
            new_char = ALPHABET[index_of_new_char]

        ciphered_data_as_list.append(new_char)
    return ''.join(ciphered_data_as_list)


if __name__ == '__main__':
    print(to_decode(1, 'treE!'))