def make_country(name: str, capital: str) -> {}:
    coutries = {}
    coutries['name'] = name
    coutries['capital'] = capital
    return coutries


if __name__ == '__main__':
    print(make_country('poland', 'warsaw'))
