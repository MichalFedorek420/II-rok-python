def f(a,b):
    if a > b:
        return f"{a}-{b}={a-b}"
    else:
        return f"{a}+{b}={a+b}"

print(f(20,7))