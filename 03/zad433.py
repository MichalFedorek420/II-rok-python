def Fibonacci(number):
    x = 0
    y = 1
    for i in range(number):
        fib_chain = x + y
        x = y
        y = fib_chain
        print(fib_chain, end= " ")
print(Fibonacci(20))

