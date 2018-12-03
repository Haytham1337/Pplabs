list1 = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

list2 = []

def remove_funct(temp_list):
    for ele in temp_list:
        if type(ele) == list:
            remove_funct(ele)
        else:
            list2.append(ele)


remove_funct(list1)
print(list1)
print(list2)
