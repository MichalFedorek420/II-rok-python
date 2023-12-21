lista = ["a", "-", "b", "-", "c", "d", "-", "e", "f"]

result_list = []
temp_list = []

for element in lista:
    if element == "-":
        if temp_list:  # Sprawdź, czy temp_list nie jest pusty
            result_list.append("".join(temp_list))
            temp_list = []  # Wyczyść temp_list po dodaniu do result_list
    else:
        temp_list.append(element)

# Dodaj ostatnią grupę elementów, jeśli lista zakończyła się myślnikiem
if temp_list:
    result_list.append("".join(temp_list))

print(result_list)
