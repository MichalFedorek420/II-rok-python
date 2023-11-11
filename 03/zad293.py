shoes = 20
underwear = 70
jacket = 40
rinse = 15
spin = 9
full_time = 0
if input(f'Chciałbyś kupić dodatkowe 15 min? ') == "tak":
    full_time+=rinse 
if input(f'Chciałbyś kupić dodatkowe 9 min? ') == "tak":
    full_time+=spin
x = input(f'co chcialabys uprac? ')
if x == "buty":
    full_time+=shoes
if x == "bielizne":
    full_time+=underwear
if x == "kurtke":
    full_time+=jacket
print(f"Total washing time: {full_time} minutes")


