a = input('podaj pierwszą liczbe: ')
b = input('podaj drugą liczbe: ')
first_row = int(b) * "*"
print(first_row)
for i in range(int(a)-2):
    x = "*"
    y = (int(b)-4)*" "
    print(x,y,x)

print(first_row)