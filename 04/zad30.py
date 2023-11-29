def f(number, even):
    counter = 0
    if even:
        for i in str(number):
            if int(i) % 2 == 0:
                counter += int(i)
    else:
        for i in str(number):
            if int(i) % 2 != 0:
                counter += int(i)
    return counter
print(f(20576,True))

