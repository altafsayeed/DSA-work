class HashTable:
    def __init__ (self, size = 7):
        self.data_map = [None] * size

    def __hash (self, key):         # Hash method
        my_hash = 0
        for letter in key:          # Loop through the letters in the key that we pass
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)     # ord gets the ascii number for each letter as we loop through
        return my_hash                                                      # multiply by 23 (or any prime number) then modulo the size which is 7
                                                                            # modulo returns the remainder, so we will always get back 0 thru 6
                                                                            # which is what we need

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):                         
        index = self.__hash(key)                        # Call hash function to get the index where data will be stored
        if self.data_map[index] == None:                # If there is no existing list at the index, then create one
            self.data_map[index] = []
        self.data_map[index].append([key, value])       # Add the key,value pair to the index using append

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)


my_hash_table.print_table()