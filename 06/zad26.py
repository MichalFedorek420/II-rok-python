arr = ["Michał","Piotrek","Bartek","KurwaPoziomka"]
len_of_names = []

for i in arr:
    len_of_names.append(len(i))

max_index = len_of_names.index(max(len_of_names))

print(arr[max_index])
