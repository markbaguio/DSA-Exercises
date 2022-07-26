""" Implement hash table where collisions are handled using linear probing.
We learnt about linear probing in the video tutorial. Take the hash table
implementation that uses chaining andmodify methods to use linear probing.
Keep MAX size of arr in hashtable as 10."""


class HashTable:
    def __init__(self, maxArrSize=10):
        self.maxArrSize = maxArrSize
        self.array = [[] for i in range(self.maxArrSize)]

    def get_hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.maxArrSize

    def __setitem__(self, key, value):
        """ This function inserts a key-value pair into the Hash Table.
            Syntax: object[key]=value"""
        value_key = self.get_hash(key)
        found = False

        if self.array[value_key] == []:
            self.array[value_key] = [key, value]

        else:
            print("Hash Collision Detected.")
            found = True
            running = True
            count = 1
            while running:
                new_index = (value_key + count) % self.maxArrSize

                if self.array[new_index] == []:
                    self.array[new_index] = [key, value]
                    running = False
                else:
                    count += 1

    def __getitem__(self, key):
        value_key = self.get_hash(key)
        running = True
        count = 0
        while running:
            new_index = ((value_key + count) % self.maxArrSize)
            if self.array[new_index][0] == key:
                return self.array[new_index][1]
            else:
                count += 1

    def update_value(self, key, value):
        """ This function updates the value of the given key.
            Syntax: object.update_value(key, value)"""
        value_key = self.get_hash(key)
        running = True
        count = 0
        while running:
            new_index = ((value_key + count) % self.maxArrSize)
            if self.array[new_index][0] == key:
                self.array[new_index][1] = value
                running = False
            else:
                count += 1

    def __delitem__(self, key):
        pass


if __name__ == "__main__":
    ht = HashTable()
    ht["march 9"] = "Mark Baguio"  # 2
    ht["march 29"] = "Ada Wong"  # 2
    ht["march 38"] = "Rebecca Chambers"  # 2
    ht["1998"] = "Helena Harper"  # 9
    ht["september 5"] = "Sherry"  # 2
    print(ht["1998"])
    print(ht.array)
