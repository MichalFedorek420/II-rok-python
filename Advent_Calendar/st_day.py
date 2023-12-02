inputer = input('Podaj zaszyfrowane wspolrzedne: ')
def elves_shit(info_from_elves):
    list_of_all_digits = []
    list_of_digits = []
    for i in info_from_elves.split('\n'):
        try:
            if i.isdigit():
                list_of_digits.append(int(i))
                list_of_all_digits.append(list_of_all_digits[0] + list_of_all_digits[-1])
        except ValueError:
            continue
    return list_of_all_digits

print(elves_shit(inputer))




        
    

