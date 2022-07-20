"""July 7, 2022
    Mark Godwin C. Baguio

This function is for testing purposes only."""


def get_hash(key):
    total = 0
    for char in key:
        total += ord(char)
    return total % 100


if __name__ == "__main__":
    print("The hash value is: {}".format(get_hash("september 12")))
