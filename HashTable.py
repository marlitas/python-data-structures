#Hash a way to encrypt something... gives it an address. Hash is a verb. 
# Dictionaries, the key is hashed (given an address) and the key value pair are then stored at that address. 
# Collision happens when there are multiple ke/value pairs at the same address. 
    # Exist within the same list at that address
    # ^^^ called seperate chaining
#Linear Probing
    # Keep moving down until you find an empty spot (when there is a collision)
    # A form of Open Addressing
#Seperate Chaining
    # Can have a linked list instead of regular list, if you want. 

#Always have a prime number of addresses to increase random assigning of address. 

# Setting and getting in a hash table is considered O(1) because distribution across addresses is generally incredibly efficient and collisions are rare. 

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for pairs in self.data_map[index]:
                if pairs[0] == key:
                    return pairs[1]
        return None

    def keys(self):
        key_list = []
        for index in self.data_map:
            if index:
                for pairs in index:
                    key_list.append(pairs[0])
        return key_list

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.get_item('bolts'))

print(my_hash_table.keys())
# my_hash_table.print_table()
