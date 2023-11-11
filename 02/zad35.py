def f(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        return "Invalid operator"

# Test cases
result1 = f(5, 3, '+')
result2 = f(5, 3, '-')
result3 = f(5, 3, '*')
result4 = f(5, 3, '%')
result5 = f(5, 3, '**')
result6 = f(5, 3, '/')  # Invalid operator

print("Result1:", result1)
print("Result2:", result2)
print("Result3:", result3)
print("Result4:", result4)
print("Result5:", result5)
print("Result6:", result6)
