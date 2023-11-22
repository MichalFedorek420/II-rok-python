def generate_lottery_coupon():
    for row in range(7):
        for col in range(7):
            number = col * 7 + row + 1
            print(f"{number:2d}", end=" ")
        print()

generate_lottery_coupon()

