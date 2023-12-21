def elfs_game(elfs_string):


    numbers = []
    list_of_words = [char for char in elfs_string.split()]
    
    for char in list_of_words:

        if char == "Game":
            numbers.append(char)

        if char.isdigit():
            indeksik = list_of_words.index(char)
            numbers.append(int(char))
            numbers.append(list_of_words[indeksik+1])

    return numbers

def key_word(list1,key_wor):

    numbers2 = []
    podlista = []
    for element in list1:
        if element == key_wor:
            if podlista:
                numbers2.append(podlista)
                podlista = []
        else:
            podlista.append(element)
    if podlista:
        numbers2.append(podlista)
    return numbers2

def elf_quastion(listek):
    red = 12
    green = 13
    blue = 14
    counter_main = 0
    counter = 0
    counter3 = 0
    listekj =[]
    listeki = []
    flag1,flag2,flag3 = True,True,True

    for i in listek:
        listeki.append(i)

        for j in i:
            listekj.append(j)
            
    return listekj
            
    # for i in listek:
    #     for j in i:
    #         if isinstance(j, str):

    #             if j.startswith("red"):
    #                 if int(listekj[counter-1]) <= red:
    #                     flag1 = True
    #                 else:
    #                     flag1 = False
    #             elif j.startswith("green"):
    #                 if int(listekj[counter-1]) <= green:
    #                     flag2 = True
    #                 else:
    #                     flag2 = False
    #             elif j.startswith("blue"):
    #                 if int(listekj[counter-1]) <= blue:
    #                     flag3 = True
    #                 else:
    #                     flag3 = False
    #             else:
    #                 continue
    #             counter += 1

    #         else:
    #             continue

    #     if flag1 and flag2 and flag3:
    #         counter_main += counter3

    #     counter3 += 1

    # return counter_main

with open("2_day.txt", "r", encoding="utf-8") as file:
    results = file.read()

lista_one = elfs_game(results)
lista_two = key_word(lista_one,"Game")
final_int = elf_quastion(lista_two)
print(final_int)

