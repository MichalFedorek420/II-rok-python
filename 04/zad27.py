def f(card_number):
    lista = [i for i in card_number]
    tuple = (2,3,4,5,6,7,8,9,10,11)
    for i in tuple:
        lista[i] = "*"
    return "".join(lista)
        
print(f('1234567890123456'))