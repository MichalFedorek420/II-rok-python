x = int(input('Enter decimal number: '))
if x < 0:
    print("Liczba musi być nieujemna.")
else:
    while x > 0:
        y = x % 2
        print(y)
        x = x // 2 
