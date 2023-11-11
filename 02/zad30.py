def f(number,even):
    x = 0
    if even == True:
        for i in str(number):
            if int(i) % 2 == 0:
                x+=int(i)
            else:
                None 
    else:
        if int(i) % 2 != 0:
            x+=int(i)
        else:
            None
    return x
print(f(3124,True))


