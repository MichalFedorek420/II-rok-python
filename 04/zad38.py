def f(palindrome):
    characters = []
    for i in palindrome:
        characters.append(i)
    if characters == characters[::-1]:
        return True
    else:
        return False
print(f("radar"))