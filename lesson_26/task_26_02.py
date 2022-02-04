def check_braces(sentence_to_check: str):
    stack = []
    is_good = True
    for item in sentence_to_check:
        if item in '({[':
            stack.append(item)
        elif item in ')}]':
            if not stack:
                is_good = False
                break
            open_bracket = stack.pop()
            if open_bracket == '(' and item == ')':
                continue
            if open_bracket == '{' and item == '}':
                continue
            if open_bracket == '[' and item == ']':
                continue
            is_good = False
            break
    if is_good and len(stack) == 0:
        return True
    else:
        return False


print(check_braces('({[)})'))
