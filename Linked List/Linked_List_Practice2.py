class LinkedListNode:
    """This LinkedListNode class creates a Linked List Node that has a value(data) and a pointer to the next node(nextNode)."""

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def printLL(self):
        """this function prints the Linked List."""
        currentNode = self.head
        # validation: check if the linked list is empty.
        if(currentNode is None):
            print("Linked List is empty.")

        while currentNode is not None:
            print(currentNode.data, "->", end=" ")
            currentNode = currentNode.nextNode

    def print_index(self, index=int):
        """This function prints the data of the given index."""
        if type(index) is not int:
            raise Exception("Index must be an integer.")
        if index > self.get_ll_length() or index < 0:
            raise Exception("Invalid Index.")

        currentNode = self.head
        count = 0
        to_be_printed = ""
        while currentNode is not None:
            if index == count:
                to_be_printed += currentNode.data
                break
            currentNode = currentNode.nextNode
            count += 1

        print(to_be_printed)

    def insert_at_end(self, data):
        """this functions appends a value into the linked list."""
        currentNode = self.head
        node = LinkedListNode(data)

        if self.head is None:
            self.head = node
            return

        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def insert_at_beginning(self, data):
        """this function inserts a value(data) at the beginning of the linked list.
            it replaces the current head node with a new value(new head node)."""
        # check if the linked list is empty.
        currentNode = self.head
        # node = LinkedListNode(data, currentNode)
        # if currentNode is not None:  # if the linked list is populated.
        #     # node = LinkedListNode(data, currentNode)
        #     self.head = node
        # elif currentNode is None:
        #     self.head = LinkedListNode(data)
        node = LinkedListNode(data, currentNode)
        self.head = node

    def get_ll_length(self):
        """this function prints the length of the linked list by incrementing the
            count variable while traversing the linked list."""
        currentNode = self.head
        count = 0
        while currentNode is not None:
            count += 1
            currentNode = currentNode.nextNode
        return count

    def insert_values(self, data_list):
        "this function inserts list values into the linked list."
        for data in data_list:
            self.insert_at_end(data)

    def insert_new_values(self, data_list):
        """this function inserts new list values into the linked list."""
        self.head = None  # this line deletes the whole linked list by cutting off its head node.
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_index(self, index, data):
        """This function inserts data into the given index."""
        currentNode = self.head
        if index > self.get_ll_length():
            raise Exception("Invalid index.")
        if index < 0:
            raise Exception("Invalid index.")
        # if you want to change the head node(index 0) using this function.
        if index == 0:
            # node = LinkedListNode(data, currentNode)
            # self.head = node
            self.insert_at_beginning(data)

        count = 0
        while currentNode is not None:
            if count == index - 1:
                node = LinkedListNode(data, currentNode.nextNode)
                currentNode.nextNode = node
            currentNode = currentNode.nextNode
            count += 1

    def insert_after_value(self, data_after, data):
        """This function inserts data after the data_after(chosen data)."""
        currentNode = self.head

        while currentNode is not None:
            if data_after == currentNode.data:
                node = LinkedListNode(data, currentNode.nextNode)
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def delete_value(self, data_to_delete):
        """This function deletes the given data."""
        currentNode = self.head
        if self.head is None:
            raise Exception("The linked list is empty.")

        while currentNode is not None:
            # the currentNode.nextNode.data is the node prior the value to be deleted.
            if data_to_delete == currentNode.nextNode.data:
                currentNode.nextNode = currentNode.nextNode.nextNode
                break
            currentNode = currentNode.nextNode

    def delete_index(self, index):
        """This funtion deletes the data at the given index."""
        currentNode = self.head
        if index > self.get_ll_length():
            raise Exception("Invalid Index.")
        if index < 0:
            raise Exception("Invalid Index.")
        if index == 0:
            self.head = currentNode.nextNode
        if index == self.get_ll_length():
            currentNode = None

        count = 0
        while currentNode is not None:
            if count == index - 1:
                currentNode.nextNode = currentNode.nextNode.nextNode
            currentNode = currentNode.nextNode
            count += 1


if __name__ == "__main__":
    ll1 = LinkedList()
    # ll1.insert_at_end("Ada")
    # ll1.insert_at_end("Mark")
    # ll1.insert_at_end("100")
    # ll1.insert_at_beginning(1)
    # ll1.insert_at_beginning(69)
    # ll1.insert_at_beginning(90)
    # ll1.insert_at_end("69")
    # ll1.insert_values([1, 2, 3])
    ll1.insert_new_values(["Ada Wong", "Mark Baguio", "1998", "Raccoon City"])
    ll1.insert_at_beginning("Red Dress")
    ll1.insert_at_end("Encounter")
    ll1.insert_at_index(3, "Rebecca Chambers")
    ll1.insert_after_value("1998", "Mark")
    ll1.insert_after_value("Rebecca Chambers", 69)
    ll1.print_index(3)

    print("length of the linked list: {}".format(ll1.get_ll_length()))

    ll1.printLL()
