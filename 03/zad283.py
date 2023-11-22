x = input('podaj numer EAN-13: ')
result = 'Zły numer' if (len(x) != 13 or not x.isdigit()) else 'Dobry numer'
country_check = 'Produkt stworzony w Polsce' if x.startswith('590') else None
print(result)
print(country_check)