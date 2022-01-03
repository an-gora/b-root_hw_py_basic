def make_country(name: str, capital: str) -> {}:
    coutries = {}
    coutries['name'] = name
    coutries['capital'] = capital
    return coutries


def print_my_dict(my_dict: dict):
    print(my_dict)


if __name__ == '__main__':
    print_my_dict(make_country('poland', 'warsaw'))
