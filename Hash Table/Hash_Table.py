class HashTable:
    def __init__(self, MAXARRSIZE=100):
        """This function initializes the class."""
        """The defaul size of the Hash Table is 100. However, it can be
        set to any number."""
        self.MAXARRSIZE = MAXARRSIZE
        self.array = [None for i in range(self.MAXARRSIZE)]
        # this list technique is called list comprehension,
        # it's just a more concise way of creating and/or operating(doing something with) your list.

    def get_hash(self, key):
        """This function returns the hash value of a given key."""
        total = 0
        for char in key:
            total += ord(char)
        return total % self.MAXARRSIZE

    # def add_value(self, key, value): instead of calling the add_value function every time,
    # the __setitem__ allows for a more concise way of adding value into the Hash Table
    def __setitem__(self, key, value):
        """This function adds value into the Hash Table.
            Syntax: object[key] = value"""
        k = self.get_hash(key)
        self.array[k] = value

    # def get_value(self, key): instead of calling the get_value function every time,
    # the __getitem__ allows for a more concise way of retrieving value in the Hash Table
    # by using its assigned key.
    def __getitem__(self, key):
        """This function returns the value of the given key.
            Syntax: object[key]"""
        """This is a simple get function."""
        # for element in self.array:
        #     if self.get_hash(key):
        #         return self.array[self.get_hash(key)]
        value_key = self.get_hash(key)
        return self.array[value_key]


if __name__ == "__main__":
    HT = HashTable()
    # HT.add_value("Mark Baguio", "Ada Wong")
    # HT.add_value("mark", "Rebecca Chambers")
    # HT.add_value("september 12", 20000000)
    # print(HT.get_value("Mark Baguio"))
    # print(HT.get_value("september 12"))
    HT["Mark Baguio"] = "Ada Wong"
    HT["mark"] = "Rebecca Chambers"
    HT["september 12"] = 20000000
    print(HT["Mark Baguio"])
    # print(HT.array, end=" ")
