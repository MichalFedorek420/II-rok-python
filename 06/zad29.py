arr1 = [2,4,4,2,4,6,4,2,1,4,5,6,88]
arr2 = [4,5,4,2,15,7,89,4,2]
arrays_og_elements = []
for i in range(len(arr1)):
    if arr1[i] not in arr2:
        arrays_og_elements.append(str(arr1[i]))
print(",".join(arrays_og_elements))

