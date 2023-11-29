def f(n1, n2, n3):
    if n3 == "+":
        return n1 + n2
    elif n3 == "-":
        return n1 - n2
    elif n3 == "*":
        return n1 * n2
    elif n3 == "/":
        return n1 / n2
    elif n3 == "%":
        return n1 % n2
    elif n3 == "**":
        return n1 ** n2
    else:
        return "Nieobsługiwany operator"

# Przykłady użycia
print(f(5, 3, "+"))   # Dodawanie: 8
print(f(5, 3, "-"))   # Odejmowanie: 2
print(f(5, 3, "*"))   # Mnożenie: 15
print(f(10, 2, "/"))  # Dzielenie: 5.0
print(f(7, 3, "%"))   # Reszta z dzielenia: 1
print(f(2, 3, "**"))  # Potęgowanie: 8
print(f(2, 3, "&"))   # Nieobsługiwany operator
