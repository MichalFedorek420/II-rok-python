def f(password):
    set_of_characters = {i for i in password}
    if len(set_of_characters) >= 6:
        return True
    else:
        return False

print(f('qwerty'))