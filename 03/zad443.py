number = int(input('Enter number: '))
quantity = 0
sum = number
mean = number/1
while number != 0:
    number = int(input('Enter number: '))
    quantity+=1
    sum+=number
    mean=sum/quantity
print(f'RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}')
    


    
