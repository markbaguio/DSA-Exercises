""" Implement hash table where collisions are handled using linear probing.
We learnt about linear probing in the video tutorial. Take the hash table
implementation that uses chaining andmodify methods to use linear probing.
Keep MAX size of arr in hashtable as 10."""


from asyncio.windows_events import NULL
from numpy import empty


class HashTable:
    def __init__(self, maxArrSize=10):
        self.maxArrSize = maxArrSize
        self.array = [None for i in range(self.maxArrSize)]

    def get_hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.maxArrSize

    def __setitem__(self, key, value):
        """ This function inserts a value into the Hash Table.
            This can handle collision by utilizing linear probing.
            Syntax: object[key] = value"""
        value_key = self.get_hash(key)  # this line generates the index.

        if self.array[value_key] is None:
            self.array[value_key] = (key, value)

        else:  # if the slot is already populated.
            print("Hash Collision Detected.")
            done = False
            count = 1
            while not done:
                # new_index serves as the index that will traverse through the Hash Table.
                # this handles index errors by ensuring that the new_index will never exceed the size of the Hash Table.
                new_index = (value_key + count) % self.maxArrSize

                # validation: check if the Hash Table is full
                if new_index == value_key:
                    raise ValueError("The Hash Table is full.")
                if self.array[new_index] is None:
                    # inserting a tuple for easy s
                    self.array[new_index] = (key, value)
                    done = True
                else:
                    count += 1

    def __getitem__(self, key):
        """This is wrong."""
        value_key = self.get_hash(key)


if __name__ == "__main__":
    ht = HashTable()
    ht["march 9"] = "Mark Baguio"  # 2
    ht["march 29"] = "Ada Wong"  # 2
    ht["march 38"] = "Rebecca Chambers"  # 2
    ht["1998"] = "Helena Harper"  # 9
    ht["september 5"] = "Sherry"  # 2
    print(ht.array)
