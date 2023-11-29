def f(binar_number):
    flag = True
    try:
        for i in binar_number:
            if int(i) != 0 and int(i) != 1:
                flag = False
        return flag
    except ValueError:
        flag = False
        return flag

print(f("0101011"))