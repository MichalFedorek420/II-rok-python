def f(a,b):
    x=[]
    for i in range(a,b):
        if int(i) % 2 == 0:
            x.append(str(i))
    return ",".join(x)
print(f(3,11))