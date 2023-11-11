# for i in range(1,50):
    # if i % 7 == 0:
    #     print(i, end=" ")
    # else:
    #     print(i)
def generate_lottery_coupon():
    for row in range(7):
        for col in range(7):

            
        
            number = col * 7 + row + 1
            print(f"{number:2d}", end=" ")
        

generate_lottery_coupon()

