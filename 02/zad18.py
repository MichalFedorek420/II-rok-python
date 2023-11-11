x = int(input('Podaj liczbe'))
def numbers(n):
    x=[]
    for i in range(1,n+1):
        x.append(str(i))
    return " ".join(x)
print(f'Numbers <1,{x}>: {numbers(x)}')

