def f(product_code):
    numbers = [int(number) for number in product_code]
    if numbers[0]+numbers[1]+numbers[2] % 7 == numbers[3]:
        return True
    else:
        return False
print(f("1082"))