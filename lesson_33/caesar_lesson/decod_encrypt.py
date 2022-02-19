import string
import operator


ALPHABET: str = ''.join([
    string.ascii_lowercase,
    string.ascii_uppercase,
    ])

#обьединить decode-crypto??? через operator из парсера математического выражения из 30 parse tree

def to_proccess(key: int, data_to_decode: str, is_decode: bool = False)->str:
    ciphered_data_as_list: list[str] = []
    if is_decode:
        action = operator.sub
    else:
        action = operator.add
    for char in data_to_decode:
        try:
            index = ALPHABET.index(char)
        except ValueError:
            new_char = char
        else:
            index_of_new_char = action(index, key)%len(ALPHABET)
            new_char = ALPHABET[index_of_new_char]

        ciphered_data_as_list.append(new_char)
    return ''.join(ciphered_data_as_list)


if __name__ == '__main__':
    print(to_proccess(1, 'areE!', True))