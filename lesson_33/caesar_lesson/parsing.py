def to_parse(data):
    flag, key, data_for_proccesing = data.decode('utf-8').split(' ', maxsplit=2)
    # flag, key, data_for_proccesing = data.split(' ', maxsplit=2)
    return flag, int(key), data_for_proccesing

# print(to_parse('i_want_to_cipher 3 tree'))
