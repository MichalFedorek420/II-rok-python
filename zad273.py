licznik = 0
x = {'fb':True,'tw':True,'ig':True}

for key in x:
    if x[key]== True:
        licznik+=1
print(licznik)
if licznik >= 2:
    print('ziomek to influpedał')