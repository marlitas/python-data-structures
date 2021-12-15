# Works with a pivot point.
# start with first item. 
    #compare each item to the first and sort into less than and greater than
# swap first with last item of the less than. 

#run same thing on less than items
    #until base case of one item
#run same thing on greater than items
    #until base case of one item

#starts with pivot helper function. 
    # pivot will return less/greater than separation & swap as well as end index of pivot item. 

def pivot(list, pivot, end):
    swap = pivot
    for index in range(pivot + 1, end + 1):
        if list[index] < list[pivot]:
            swap += 1
            temp = list[index]
            list[index] = list[swap]
            list[swap] = temp
    temp = list[swap]
    list[swap] = list[pivot]
    list[pivot] = temp
    return swap

def quick_sort_helper(list, left, right):
    if left < right:
        pivot_index = pivot(list, left, right)
        quick_sort_helper(list, left, pivot_index-1)
        quick_sort_helper(list, pivot_index+1, right)
    return list

def quick_sort(list):
    return quick_sort_helper(list, 0, len(list) - 1)

#left = 0
#right = 6
#pivot_index = 3
    #left = 0
    #right = 2
    #pivot_index = 1
        #left = 0
        #right = 0
    #return [1,2,3,4,6,7,5]

[1, 2, 3]
[1, 3, 2, 4, 6, 7, 5]
my_list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(my_list))
            