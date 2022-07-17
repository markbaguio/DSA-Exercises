class LinkedListNode:
    """This is a basic implementation of the Linked List data structure.
        The purpose of this practice is to get familiarized with the 
        (singly) Linked List data structure 
        Example: 1->2->3"""

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


if __name__ == "__main__":
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)
    node4 = LinkedListNode(100)

    """this line sets the pointer of the head node(node1) to the next node(node2).
        This creates this: node1 -> node2 -> node3 or 1 -> 2 -> 3"""
    node1.nextNode = node2
    node2.nextNode = node3
    node3.nextNode = node4

    # printing the linked list
    currentNode = node1  # this is the head node.
    while True:
        print(currentNode.data, "->", end=" ")
        # validation: check if the next node is the tail node which points to NULL
        if currentNode.nextNode is None:
            print("NULL")
            break
        currentNode = currentNode.nextNode
