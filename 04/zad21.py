import random
def generate_number():
    random_number = random.randrange(1,10)
    return random_number

def main():
    computer_digit = generate_number()
    user_guess = int(input("Jak myślisz jaką liczbę wybrał komputer? "))
    if user_guess == computer_digit:
        print("Wygrałeś!")
    else:
        print(f"Przegrałeś, liczba komputera to: ",computer_digit)

main()


