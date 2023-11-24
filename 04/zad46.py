def f(x,y):
    numbers_sum = 0
    for i in range(x,y+1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            numbers_sum += i
        else:
            None
    return numbers_sum
print(f(10,30))
