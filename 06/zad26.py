arr = ["Michał","Piotrek","Bartek","KurwaPoziomka"]
len_of_names = []
for i in arr:
    len_of_names.append(len(i))
max_index = len_of_names.index(max(len_of_names))
    # for indeks, value in enumerate(len_of_names):
    #     ind = max(len_of_names)[indeks]
print(arr[max_index])
