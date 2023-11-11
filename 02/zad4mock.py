def f(text):
    result = ''
    for i, char in enumerate(text):
        if i % 2 == 0:
            result += char + '+'
        else:
            result += char + '-'
    return result

print(f("hahdhd"))
