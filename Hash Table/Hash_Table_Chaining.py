""" Engr. Mark Godwin C. Baguio
    July 21, 2022

    This Hash Table utilizes chaining method for handling(Attaching an array of tuples
    on each of the index.) collisions.
    
    Basically, this is an implementation of Python dictionary with each of the elements being an array of tuples."""


class HashTable:
    def __init__(self, MAXARRSIZE=100):
        self.MAXARRSIZE = MAXARRSIZE
        self.array = [[] for i in range(self.MAXARRSIZE)]
        # line 8 makes each of the indices of the array an array which will contain tuples later.

    def get_hash(self, key):
        """This function converts the given key into a hash code/value which is used to index the Hash Table."""
        total = 0
        for char in key:
            total += ord(char)
        return total % self.MAXARRSIZE

    def __setitem__(self, key, value):
        """ This function inserts a value into the Hash Table.
            This handles collision by utilizing chaining.
            It adds an array of tuples which contains key-value pairs in the Hash Table.
            Syntax: object[key] = value"""
        value_key = self.get_hash(key)
        found = False

        # (for loop): if the key already exist this will insert a new tuple which contains the new key-value pair.
        for indx, element in enumerate(self.array[value_key]):
            if len(element) == 2 and element[0] == key:
                self.array[value_key][indx] = (key, value)
                found = True
                break

        if not found:  # this line will be executed if the given key does not exist.
            self.array[value_key].append((key, value))

    def __getitem__(self, key):
        """ This function returns the value of the given key.
            Syntax: object[key]"""
        value_key = self.get_hash(key)

        for kvElement in self.array[value_key]:
            if kvElement[0] == key:
                return kvElement[1]

    def __delitem__(self, key):
        """ This function deletes the value assigned to the given key.
            Syntax: del object[key]"""
        value_key = self.get_hash(key)
        found = False

        for indx, kvElement in enumerate(self.array[value_key]):
            if kvElement[0] == key:
                del self.array[value_key][indx]
                found = True

        if not found:
            raise Exception("Key does not exist in the Hash Table.")


if __name__ == "__main__":
    ht = HashTable(10)
    ht["1998"] = "Raccoon City"
    ht["Ada"] = "Mark"
    ht["march 6"] = 1000
    ht["march 17"] = 500
    ht["march 20"] = 20000
    ht["Mark Baguio"] = "Ada Wong"
    ht["0"] = "Rebecca Chambers"
    del ht["march 6"]
    print(ht["march 17"])
    print(ht.array)
