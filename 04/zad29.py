def f(amount_to_pay):
    amount_of_fives = amount_to_pay // 5
    amount_of_two = (amount_to_pay % 5) // 2
    amount_of_one = amount_to_pay - amount_of_two * 2 - amount_of_fives * 5

    return amount_of_two + amount_of_fives + amount_of_one
print(f(0))
