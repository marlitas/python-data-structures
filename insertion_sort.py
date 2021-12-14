# Start with second item in list, compare to item before. 
#then next item, compare to item before.
# keep comparing until it's not less than, then insert. 

def insertion_sort(my_list):
    for loop_num in range(1, len(my_list) - 1):
        for index in range(loop_num, 1, -1):
            if my_list[index] < my_list[index - 1]:
                temp = my_list[index]
                my_list[index] = my_list[index - 1]
                my_list[index - 1] = temp
    return my_list

# because the lesson function uses a while loop that only runs if the element is less than the one before it it's time complexity for mostly sorted inputs is much less O(n)

# Not using a while loop decreases the efficiency for those certain use cases. 

def insertion_sort_lesson(my_list):
    for index in range(1, len(my_list)):
        temp = my_list[index]
        before = index - 1
        while temp < my_list[before] and before > -1:
            my_list[before + 1] = my_list[before]
            my_list[before] = temp
            before -= 1
    return my_list

#loop_num = 5
#index = 5
#my_list[5] = 3
#my_list[4] = 6
#temp = 1
#[1,2,4,5,6,3]

print(insertion_sort([4, 2, 6, 5, 1, 3]))

