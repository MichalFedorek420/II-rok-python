def f(x,y):
    counter = 0
    for i in range(x,y):
        if int(i) < 0 and int(i) % 2 == 0:
            counter+=1
    return counter

print(f(-7,8))