def f(dice):
    max_count = 0
    most_common_digit = None

    current_digit = None
    current_count = 0

    for digit in dice:
        if digit == current_digit:
            current_count += 1
        else:
            current_digit = digit
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            most_common_digit = current_digit

    return int(most_common_digit) if most_common_digit is not None else None

# Test cases
print(f("5233165554211"))  # Wynik: 5 (5 powtórzyło się najczęściej)
print(f("2133"))  # Wynik: 3 (3 powtórzyło się najczęściej)

