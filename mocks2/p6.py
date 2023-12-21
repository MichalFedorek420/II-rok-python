def f(t):
    counter = 0
    lista = []
    ziper = 0
    for i in t:
        if i.isdigit():
            while i[ziper].isdigit():
                while ziper < len(t):
                    bigdigit = i+i[ziper+1]
                    ziper += 1
                    if int(bigdigit) > 0:
                        counter += int(i)
                        lista.append(bigdigit)
                
            
            
            if int(i) > 0:
                counter += int(i)
                lista.append(i)
                ziper+=1
    return str(counter)+" #"+"+".join(lista)
print(f("11 and 4 is 15"))

