def f(n):
    if int(n) == 1:
        return "*"
    else:
        return ("*"+"/")*int(n-1)+"*"
print(f(4))
        