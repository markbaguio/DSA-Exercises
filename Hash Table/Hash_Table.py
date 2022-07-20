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
        pass


if __name__ == "__main__":
    HT = HashTable()
    HT.add_value("Mark Baguio", "Ada Wong")
    print(HT.get_value("Mark Baguio"))
    # print(HT.array, end=" ")
