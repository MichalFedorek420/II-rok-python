def f(number):
#     this_dict = {}
#     klucz = 0

#     for i in str(number):
#         this_dict[i] = 0

#     for j in str(number):
#         if j in this_dict.keys():
#             this_dict[j]+=1

#     max_value = max(this_dict.values())

#     for key in this_dict.keys():
#         if int(key) == max_value:
#             klucz += int(key)


#     return klucz * max_value
# print(f(230335))
    sum = 0
    a = set()
    num_str = str(number)
    for i in num_str:
        if num_str.count(i)>1:
            a.add(i)
            sum+=int(i)
    return sum
print(f(2303355))


# źle zrobione

    