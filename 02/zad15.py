def phone_keyboard():
    keyboard = ""
    for i in range(1, 10):
        if i % 3 == 0:
            keyboard += str(i) + "\n"
        else:
            keyboard += str(i)+ ' '
    return keyboard

print(phone_keyboard())

