def compare(arr1,arr2):
    flag = False
    if len(arr1) == len(arr2):

        for i in range(len(arr1)):

            if arr1[i] == arr2[i]:
                flag = True
            else:
                flag = False
        
    return flag
    
    
print(compare([True,False],[True,False]))
