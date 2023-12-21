def f(x):
    counter = 0
    for i in x:
        if i == "+":
            counter +=1
        if i == "-":
            counter -=1
    return counter
print(f("+-+++-+---"))
