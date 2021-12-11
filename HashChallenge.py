# You have two lists.
# Must determine if the lists have an item in common. 
    # Naive approach would create nested for loops

def common_item(list1, list2):
    dict = {}
    for item in list1:
        dict[item] = False
    for item in list2:
        if item in dict:
            return True
    return False

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(common_item(list1, list2))