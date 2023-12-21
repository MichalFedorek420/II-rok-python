def f(x):
    counter = 0
    for i in x:
        if i == "A" or i == "K" or i == "Q" or i == "J":
            counter += 10
        else:
            counter += int(i)
    return counter
print(f('234AJ7'))