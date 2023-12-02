def bubblesort(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    return array

print(bubblesort([4,3,26,45,11,2,69,22]))
# chujowe nie dziala jebac to