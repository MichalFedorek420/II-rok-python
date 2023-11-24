def f(expression):
    list_of_expression = [i for i in expression]
    for i in range(len(list_of_expression)):
        if list_of_expression[i] == "+":
            return int(list_of_expression[i-1]) + int(list_of_expression[i+1])
        elif list_of_expression[i] == "-":
            return int(list_of_expression[i-1]) - int(list_of_expression[i+1])
print(f("2+3"))