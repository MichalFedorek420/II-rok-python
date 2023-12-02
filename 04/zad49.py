def najczestsza_cyfra(liczba):
    # Zamiana liczby na listę cyfr
    cyfry = [int(cyfra) for cyfra in str(liczba)]

    # Inicjalizacja słownika do zliczania wystąpień każdej cyfry
    licznik = {}

    # Śledzenie wystąpień każdej cyfry
    for cyfra in cyfry:
        if cyfra in licznik:
            licznik[cyfra] += 1
        else:
            licznik[cyfra] = 1

    # Znalezienie cyfry, która występuje najczęściej
    najczestsza = max(licznik, key=licznik.get)

    return najczestsza
print(najczestsza_cyfra("2343654"))


