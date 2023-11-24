import re
def searching(n):
    users_sentence = input('Podaj tekst')
    search = re.findall(f"{n}",users_sentence)
    return len(search)

print(searching("e"))