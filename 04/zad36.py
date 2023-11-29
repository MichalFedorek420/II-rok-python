def f(detector):
    counter = 0
    for i in detector:
        if i == "+":
            counter +=1
        elif i == "-":
            counter -=1
        if counter == 3:
            return True
    else:
        return False
print(f("+-++-+++---"))
