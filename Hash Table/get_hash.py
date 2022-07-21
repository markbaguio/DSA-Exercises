"""July 7, 2022
    Mark Godwin C. Baguio

This function is for testing purposes only."""


def get_hash(key):
    total = 0
    for char in key:
        total += ord(char)
    return total % 4 


lst = [1998, "Raccoon City", "Incident", "Hellfire"]

if __name__ == "__main__":
    print("The hash value is: {}".format(get_hash("march 9")))
    key = get_hash("2")

    for indx, element in enumerate(lst[key]):
        print(indx, element)
