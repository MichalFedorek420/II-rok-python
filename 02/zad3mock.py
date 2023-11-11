def f(n):
    conteiner = {i for i in n}
    if len(conteiner)>=6:
        return True
    else: 
        return False
print(f('abcd5'))