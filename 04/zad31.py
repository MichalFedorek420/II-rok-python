def f(x,y):
    counter = 0
    for i in range(x,0):
        if abs(i) % 2 == 0:
            counter += 1
    return counter
print(f(-1,11))
