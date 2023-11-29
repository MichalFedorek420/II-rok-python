def f(n):
    x = []
    for i in range(1,n + 1):
        x.append(str(i))
    return "".join(x)
print(f(4))
