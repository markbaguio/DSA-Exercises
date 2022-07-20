class HashTable:
    def __init__(self):
        self.MAXARRSIZE = 100
        self.array = [None for i in range(self.MAXARRSIZE)]

    def get_hash(self, key):
        """This function returns the hash value of a given key."""
        total = 0
        for char in key:
            total += ord(char)
        return total % self.MAXARRSIZE

    def add_value(self, key, value):
        """This function adds value into the Hash Table."""
        k = self.get_hash(key)
        self.array[k] = value

    def get_value(self, key):
        """This function returns the value of the given key."""
        """This is a simple get function."""
        # for element in self.array:
        #     if self.get_hash(key):
        #         return self.array[self.get_hash(key)]
        value_key = self.get_hash(key)
        return self.array[value_key]


if __name__ == "__main__":
    HT = HashTable()
    HT.add_value("Mark Baguio", "Ada Wong")
    HT.add_value("mark", "Rebecca Chambers")
    print(HT.get_value("Mark Baguio"))
    # print(HT.array, end=" ")
