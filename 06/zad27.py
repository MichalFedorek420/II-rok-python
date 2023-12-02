def star(n):

    result = ''
    for i in n:
        result += f"{i}:{int(i) * '*'}\n"
    return result

print(star([12,6,4,9,10]))