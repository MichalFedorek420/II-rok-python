def different(n1,n2,n3):
    if n1==n2==n3:
        return f"{n1},{n2} and {n3} are the same"
    else:
        return f"{n1},{n2} and {n3} are different"
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))
print(different(x,y,z))