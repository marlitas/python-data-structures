# Look at first item and keep track of index of minimum item. 
#If the next item is less than the index of the previous item then save new min-Index

def selection_sort(my_list):
    for loop in range(0, len(my_list) - 1, 1):
        min_index = loop
        for index in range(loop, len(my_list)):
            if my_list[min_index] > my_list[index]:
                min_index = index
        if loop != min_index:
            temp = my_list[loop]
            my_list[loop] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

#loop = 0
#index = 0

print(selection_sort([4, 2, 6, 5, 1, 3]))