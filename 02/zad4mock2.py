def f(card_number):
    masked_card_number = card_number[2:-4]
    x=card_number.replace(masked_card_number,"*"*len(masked_card_number))
    return x
print(f('5290312400019022'))