ptl = '( ( 10 + 5 ) * 3 )'
print(type(ptl.split()))
print(ptl.split())

s = "((10    +5)*3       )"


fplist = []
number = ''
for symbol in s:
        if symbol != ' ':
            if symbol not in ['(', '+', '-', '*', '/', ')']:
                if number == '':
                    number = symbol
                else:
                    number = number + symbol
            else:
                if number != '':
                    fplist.append(number)
                fplist.append(symbol)
                number = ''
        else:
            # symbol=''
            continue

print(type(fplist))
print(fplist)