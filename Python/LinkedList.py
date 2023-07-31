import unittest
from Nodes import SinglyNode
from collections.abc import Iterable

"""Singly Linked List is a linked list that uses singly nodes to store a list.
This means that each node of the linked list will have only its own value and pointer to the next node in the list.
The linked list itself contains only the pointer to the head node of the linked list where the list starts."""
class SinglyLinkedList():

    head = None

    def __init__(self, head=None):
        # Using type of head value passed in to see how linked list should be initialized.
        if isinstance(head, Iterable):
            # If head is a list of values add them all one by one and create a linked list.
            previousElement = None
            # Go over each element from the input value and append them all one by one to the current linked list
            for element in head:
                currentElement = None
                # If the input value is a list of pre-made nodes, we just use those nodes directly. If not, we make nodes out of them and append them to this linked list.
                if type(element) == SinglyNode:
                    currentElement = element
                else:
                    currentElement = SinglyNode(element)
                # When going through first element from the input list, the head will be empty so use current element as head. After that, append current element at the end of the list.
                if self.head is None:
                    self.head = currentElement
                else:
                    previousElement.next = currentElement
                # Move the pointer for end of the list to currently added last element
                previousElement = currentElement
        elif type(head) == SinglyNode or head is None:
            # If head is an already made SinglyNode object, use that as a head.
            # If head is None, we want self.head to be None that will indicate us that the linked list was initiated without a value
            self.head = head
        else:
            # If head is anything else, create a SinglyNode out of it and use that as a head.
            self.head = SinglyNode(head)

    """Get a stringified version of the linked list"""
    def __str__(self):
        """Represent linked list with all nodes stringified and joined by a ` --> ` in between."""
        result = ""
        if self.head:
            currentNode = self.head
            while currentNode:
                result = result + str(currentNode)
                currentNode = currentNode.next
        return result

    """Append an element at the back of the linked list"""
    def append(self, next):
        targetNode = None
        # Based on the type of incoming value, target node will be either the incoming SinglyNode object or a SinglyNode object created from incoming value.
        if type(next) == SinglyNode:
            targetNode = next
        else:
            targetNode = SinglyNode(next)
        if self.head is None:
            # If self.head is None that means the linked list was initialized without an element. Make the target node the head.
            self.head = targetNode
        else:
            # If not, traverse the linked list to the last element and append target node next to it.
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = targetNode

    """Iterate over each element from the linked list"""
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

    """Reverse the order of linked list elements"""
    def reverse(self):
        # If self.head is not present, the linked list is initialized without any value. Hence nothing to be done to reverse it.
        if self.head:
            current = self.head
            previous = None
            # Go through each element reversing the pointers of nodes till end.
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            # At the end of linked list pointer reversals, the current node will be None. Hence, previous is the node used to be the last node. Make that the new head.
            self.head = previous


class SinglyLinkedListTest(unittest.TestCase):
    def test_createList_singleValues(self):
        linkedList = SinglyLinkedList(SinglyNode(0))
        for idx in range(1, 6):
            linkedList.append(SinglyNode(idx))
        linkedList.append(6)
        self.assertEqual(" --> ".join([str(idx) for idx in range(7)]), str(linkedList))

    def test_createList_fromIterable(self):
        linkedList = SinglyLinkedList([0,1,2,3,4,5])
        self.assertEqual(" --> ".join([str(idx) for idx in range(6)]), str(linkedList))
        linkedList2 = SinglyLinkedList([SinglyNode(idx) for idx in range(6)])
        self.assertEqual(str(linkedList), str(linkedList2))

    def test_iterate(self):
        linkedList = SinglyLinkedList([0,1,2,3,4,5])
        for idx, node in enumerate(linkedList):
            self.assertEqual(SinglyNode, type(node))
            self.assertEqual(idx, node.value)

    def test_reverse(self):
        linkedList = SinglyLinkedList([0,1,2,3,4,5])
        linkedList.reverse()
        linkedList2 = SinglyLinkedList([5,4,3,2,1,0])
        self.assertEqual(str(linkedList), str(linkedList2))



if __name__ == "__main__":
    unittest.main()

    