def make_country(name, capital):
    coutries = {}
    coutries['name'] = name
    coutries['capital'] = capital
    return coutries


new_county = make_country('poland', 'warsaw')
print(new_county)