def f(n):
    x = 0
    y = 1
    for i in range (n-2):
        fibonacci = x+y
        x = y
        y = fibonacci
    return fibonacci
print(f(9))


        
