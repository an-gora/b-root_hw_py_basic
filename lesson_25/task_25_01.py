def to_power(x, exp: int):
    if exp < 0:
        raise ValueError('This function works only with exp > 0')
    if x == 0 or exp == 0:
        return 1
    return to_power(x, exp - 1) * x


print(to_power(2, 3))
