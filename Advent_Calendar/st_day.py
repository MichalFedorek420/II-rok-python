def elves_shit(info_from_elves):

    list_of_all_digits = []
    list_of_digits = []
    help_list = []
    sum = 0

    for i in info_from_elves.split():
        for j in i:

            if j.isdigit():
                list_of_digits.append(j)
                

            else:
                continue
        list_of_digits.append("|")

    for i in list_of_digits:
        if i == "|":
            if help_list:
                list_of_all_digits.append("".join(help_list))
                help_list = []
        else:
            help_list.append(i)

    for i in list_of_all_digits:
        small_list = [_ for _ in i]
        git = small_list[0] + small_list[-1]
        sum += int(git)
    
    return sum



with open("1_day.txt", "r", encoding="utf-8") as file:
    results = file.read()
print(elves_shit(results))




        
    

