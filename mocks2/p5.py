def f(arr2d):
    x = []
    counter = 0
    for i in  arr2d:
        for j in i:
            x.append(j)
    for j in range(len(x)-1):
        if x[j] ** 2 == x[j+1]:
            counter += 1
    return counter
print(f([[2,4],[-3,-9]]))