def sum_of_digits(digit_string: str) -> int:
    if digit_as_int := int(digit_string) <= 9:
        return digit_as_int
    return (int(digit_string)) % 10 + sum_of_digits((str(int(digit_string) // 10)))

#проверку на не число - райзнуть эксепшин, пустая строка - это 0 или не позволительно? 0 из реализации марии
print(sum_of_digits('12'))
