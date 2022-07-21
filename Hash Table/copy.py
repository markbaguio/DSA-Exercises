class HashTable:
    def __init__(self, maxArrSize=100):
        self.maxArrsize = maxArrSize
        self.array = [[] for i in range(self.maxArrsize)]

    def get_hash(self, key):
        total = 0
        for char in key:
            total += ord(char)

        return total % self.maxArrsize

    def __setitem__(self, key, value):
        value_key = self.get_hash(key)
        found = False

        for indx, element in enumerate(self.array[value_key]):
            if len(element) == 2 and element[0] == key:
                self.array[value_key][indx] = (key, value)
                found = True
                break

        if not found:
            self.array[value_key].append((key, value))

    def __getitem__(self, key):
        value_key = self.get_hash(key)

        for kvElement in self.array[value_key]:
            if kvElement[0] == key:
                return kvElement[1]

    def __delitem__(self, key):
        value_key = self.get_hash(key)
        found = False

        for indx, kvElement in enumerate(self.array[value_key]):
            if kvElement[0] == key:
                del self.array[value_key][indx]
                found = True

        if not found:
            raise Exception(
                "The key-value pair you are trying to delete does not exist in the Hash Table.")


if __name__ == "__main__":
    ht = HashTable(10)
    ht["march 6"] = "ada"
    ht["march 17"] = "Ada Wong"
    ht["Mark Baguio"] = "Ada Wong"
    print(ht["march 17"])
    del ht["march 6"]
    print(ht.array)
