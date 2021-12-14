# breaks the list apart until they only have one element left.
# merges two lists with item sorted. 

# merge is a helper function. 
#Takes two sorted lists, and combines them until sorted. 

#compares I & J
#whichever is lowest gets added to the new combined list
# Keep going through until list is empty.
# loop through remaining list and add to combined. 

def merge(list_1, list_2):
    merged_list = []
    index_1 = 0
    index_2 = 0
    while index_1 < len(list_1) and index_2 < len(list_2):
        if list_1[index_1] > list_2[index_2]:
            merged_list.append(list_2[index_2])
            index_2 += 1
        else:
            merged_list.append(list_1[index_1])
            index_1 += 1
    while index_1 < len(list_1):
        merged_list.append(list_1[index_1])
        index_1 += 1
    while index_2 < len(list_2):
        merged_list.append(list_2[index_2])
        index_2 += 1
    return merged_list

def merge_sort(list):
    if len(list) == 1:
        return list
    middle = int(len(list)/2)
    list_1 = merge_sort(list[:middle])
    list_2 = merge_sort(list[middle:])
    return merge(list_1, list_2)

print(merge_sort([6,4,2,3,1,5,7]))
#print(merge([1,2,7,8], [3,4,5,6]))

#Big O = O(n * log n)

