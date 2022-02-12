math_exp = '((TRUE AND FALSE) OR TRUE )'


tokens_list = []
char: str = ''
for sign in math_exp:
    if not sign.isspace():
        if sign not in ['(', ')']:
            if char == '':
                char = sign
            else:
                if char.title() in ['True', 'False']:
                    tokens_list.append(char.title())
                    char = ''
                    char+= sign
                if char.lower() in ['and', 'or', 'not']:
                    tokens_list.append(char.lower())
                    char = ''
                    char+= sign
                else:
                    char = char + sign
        else:
            if char.title() in ['True', 'False']:
                tokens_list.append(char.title())
            if char.lower() in ['and', 'or', 'not']:
                tokens_list.append(char.lower())
            tokens_list.append(sign)
            char = ''
    else:
        if char.title() in ['True', 'False']:
            tokens_list.append(char.title())
            char = ''
        if char.lower() in ['and', 'or', 'not']:
            tokens_list.append(char.lower())
            char = ''
        char = ''

print(tokens_list)