def calculate_expression(expression):
    elements = expression.split('+')
    result = 0

    for element in elements:
        if '-' in element:
            sub_elements = element.split('-')
            sub_result = int(sub_elements[0])
            for sub_element in sub_elements[1:]:
                sub_result -= int(sub_element)
            result += sub_result
        else:
            result += int(element)

    return result

# Przykład użycia
expression = "2+4+4-3-1"
result = calculate_expression(expression)
print(result)
