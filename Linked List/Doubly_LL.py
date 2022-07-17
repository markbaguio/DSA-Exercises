class DoublyLinkedListNode:
    """This DoublyLinkedList class create a Doubly Linked List Node
    that has previous pointer(prev), value(data), and next pointer(next)."""

    def __init__(self, prevNode=None, data=None, nextNode=None):
        self.prevNode = prevNode
        self.data = data
        self.nextNode = nextNode


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, data):
        """This function appends a data into the doubly linked list."""
        if self.head is None:
            node = DoublyLinkedListNode(None, data, self.head)
            self.head = node
        else:
            tailNode = self.get_dll_tail()
            node = DoublyLinkedListNode(tailNode, data, None)
            tailNode.nextNode = node

    def insert_at_beginning(self, data):
        """This function replaces the head node with new data."""
        if self.head is None:
            node = DoublyLinkedListNode(None, data, self.head)
            self.head = node
        else:
            node = DoublyLinkedListNode(None, data, self.head)
            self.head.prevNode = node
            self.head = node

    def print_forward(self):
        """This function prints the contents of the doubly linked list in
         forward direction"""
        currentNode = self.head

        if currentNode is None:
            raise Exception("Doubly Linked List is empty.")

        while currentNode is not None:
            print(currentNode.data, "->", end=" ")
            currentNode = currentNode.nextNode

    def print_backward(self):
        tailNode = self.get_dll_tail()

        # validation: if doubly linked list is empty, raise an exception
        if self.head is None:
            raise Exception("Doubly Linked List is empty.")

        while tailNode is not None:
            print(tailNode.data, "->", end=" ")
            tailNode = tailNode.prevNode

    def get_dll_length(self):
        """This function returns the length of the doubly linked list."""
        currentNode = self.head

        count = 0
        while currentNode is not None:
            count += 1
            currentNode = currentNode.nextNode

        return count

    def get_dll_tail(self):
        """This function returns sa tail node of the doubly linked list."""
        currentNode = self.head
        if currentNode is None:
            raise Exception("Doubly Linked List is empty.")

        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        return currentNode

    def insert_at_index(self, index, data):
        """This function inserts data into the given index."""
        # validation
        if index > self.get_dll_length() or index < 0:
            raise Exception("Invalid index.")

        if index == 0:
            self.insert_at_beginning(data)

        currentNode = self.head
        count = 0
        while currentNode is not None:
            if count == index - 1:
                node = DoublyLinkedListNode(
                    currentNode, data, currentNode.nextNode)
                currentNode.nextNode = node
                if currentNode.nextNode:
                    """the previous pointer of node next(right) to the newly
                    inserted data, points to newly inserted data(new node) itelf."""
                    node.nextNode.prevNode = node
            currentNode = currentNode.nextNode
            count += 1

    def insert_new_values(self, data_list):
        """This function inserts a list into the doubly linked list."""
        # this makes sure that the doubly linked list is empty.
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def append_values(self, data_list):
        """This function appends a list into the doubly linked list."""
        for data in data_list:
            self.insert_at_end(data)

    def delete_index(self, index):
        """This function deletes the node at the given index."""
        """This function works for the forward traversal. However, when you perform a
        backward traversal the supposed to be deleted data is still printed."""
        # validation
        currentNode = self.head
        tailNode = self.get_dll_tail()
        if index < 0 or index > self.get_dll_length():
            raise Exception("Index is invalid.")
        if index == 0:
            self.head = currentNode.nextNode
            # line 127 ensures that the backward traversal is properly printed.
            self.head.prevNode = None
            return  # this return statement is important.

        currentNode = self.head
        count = 0
        while currentNode is not None:
            if index == count:
                currentNode.prevNode.nextNode = currentNode.nextNode
                # the condition shoud be currentNode.nextNode to delete the tail node.
                if currentNode.nextNode:
                    """This handles the backward traversal. This deletes the given index and it ensures
                        that the backward traversal is printed properly."""
                    currentNode.nextNode.prevNode = currentNode.prevNode
            currentNode = currentNode.nextNode
            count += 1

    def delete_value(self, data_to_delete):
        """This function deletes the specified data."""
        currentNode = self.head
        # validation
        if self.head is None:
            raise Exception("The doubly linked list is empty.")
        if data_to_delete == self.head.data:
            self.head = currentNode.nextNode
            self.head.prevNode = None
            return

        while currentNode is not None:
            if data_to_delete == currentNode.data:
                currentNode.prevNode.nextNode = currentNode.nextNode
                if currentNode.nextNode:
                    """This ensures that the backward traversal is printed properly."""
                    currentNode.nextNode.prevNode = currentNode.prevNode
            currentNode = currentNode.nextNode


if __name__ == "__main__":
    dll = DoublyLinkedList()
    # dll.insert_at_beginning("Ada Wong")
    # dll.insert_at_beginning("Mark Baguio")
    # dll.insert_at_beginning("Rebecca Chambers")
    # dll.insert_at_beginning("Raccoon City")
    # dll.insert_at_end(1)
    # dll.insert_at_end(100)
    # dll.insert_at_index(2, "Miau")
    dll.insert_new_values(["0 Raccoon City", "1 1998",
                          "2 Ada Wong", "3 Mark Baguio", "4 Rebecca Chambers"])
    dll.delete_value("1 1998")
    print("length: {}".format(dll.get_dll_length()))
    # print(dll.get_dll_tail())
    # dll.print_forward()
    print("Forward traversal print: ")
    dll.print_forward()
    print("\n")
    print("Backward traversal print: ")
    dll.print_backward()
    # dll.print_backward()
