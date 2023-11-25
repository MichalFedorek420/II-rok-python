def f(name):
    
    name_list = [j for j in name]
    main_list = []
    for i in range(len(name_list)):
        if name_list[0] not in main_list:
            main_list.append(name_list[0])
        elif name_list[i] == " ":
            main_list.append(name_list[int(i) + 1])
        else:
            None
    return "".join(main_list)
print(f('Internet Of Things'))

            