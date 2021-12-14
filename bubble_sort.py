# If first item larger than second, switch
# second item with third
# and so on. 
# Bubble up largest item. 
def bubble_sort(my_list):
    for loop in range(len(my_list) - 1, 0, -1):
        for index in range(loop):
            if my_list[index] > my_list[index + 1]:
                bubble = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = bubble
    return my_list

print(bubble_sort([4, 2, 6, 5, 1, 3]))