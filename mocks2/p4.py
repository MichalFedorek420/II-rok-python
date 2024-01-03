def f(lista):
    wystepujace_raz = []
    licznik = {}

    # Przechodzimy przez listę i zliczamy wystąpienia każdej cyfry
    for cyfra in lista:
        if cyfra in licznik:
            licznik[cyfra] += 1
        else:
            licznik[cyfra] = 1
    

    # Dodajemy cyfry, które występują dokładnie jeden raz do listy wynikowej
    for cyfra, ilosc in licznik.items():
        if ilosc == 1:
            wystepujace_raz.append(cyfra)

    return len(wystepujace_raz)

print(f([11,22,33,11]))
