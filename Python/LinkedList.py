import unittest
from collections.abc import Iterable

from Nodes import SinglyNode
from TestUtility import TestUtility


class SinglyLinkedList():
    """Singly Linked List is a linked list that uses singly nodes to store a list.
    This means that each node of the linked list will have only its own value and pointer to the next node in the list.
    The linked list itself contains only the pointer to the head node of the linked list where the list starts."""

    def __init__(self, head=None):
        self.head = None
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

    def __str__(self):
        """Get a stringified version of the linked list"""
        # Represent linked list with all nodes stringified.
        result = ""
        if self.head:
            currentNode = self.head
            while currentNode:
                result = result + str(currentNode)
                currentNode = currentNode.next
        return result

    def __iter__(self):
        """Iterate over each element from the linked list"""
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

    def append(self, next):
        """Append an element at the back of the linked list"""
        # Based on the type of incoming value, target node will be either the incoming SinglyNode object or a LinkedList or a SinglyNode object created from incoming value.
        if type(next) == SinglyNode:
            targetNode = next
        elif type(next) == SinglyLinkedList:
            targetNode = next.head
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

    def prepend(self, first):
        """Prepend an element at the front of the linked list"""
        # Based on the type of incoming value, target node will be either the incoming SinglyNode object or a LinkedList or a SinglyNode object created from incoming value.
        if type(first) == SinglyNode:
            targetNode = newHead = first
        elif type(first) == SinglyLinkedList:
            currentNode = newHead = first.head
            while currentNode.next:
                currentNode = currentNode.next
            targetNode = currentNode
        else:
            targetNode = newHead = SinglyNode(first)
        targetNode.next = self.head
        self.head = newHead

    def reverse(self):
        """Reverse the order of linked list elements"""
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

    def removeNth(self, integerPosition):
        """Remove nth node from list."""
        if integerPosition is None:
            raise Exception("Invalid Input")
        if self.head is None:
            raise Exception("Invalid State")
        if integerPosition == 0:
            self.head = self.head.next
        else:
            # Use dummy node to always be on metaphorically `previous` node to what we want to remove
            # This will work because we've already taken care of removing first node if asked.
            currentNode = SinglyNode(None, self.head)
            while currentNode.next and integerPosition:
                currentNode = currentNode.next
                integerPosition -= 1
            deleteNode = currentNode.next
            currentNode.next = currentNode.next.next
            del deleteNode


class SinglyLinkedListTest(unittest.TestCase):
    def test_createList_singleValues(self):
        linkedList = SinglyLinkedList(SinglyNode(0))
        for idx in range(1, 6):
            linkedList.append(SinglyNode(idx))
        linkedList.append(6)
        self.assertEqual(str(linkedList), " --> ".join(TestUtility.stringRange(7)))

    def test_createList_fromIterable(self):
        linkedList = SinglyLinkedList([0, 1, 2, 3, 4, 5])
        self.assertEqual(str(linkedList), " --> ".join(TestUtility.stringRange(6)))
        linkedList2 = SinglyLinkedList([SinglyNode(idx) for idx in range(6)])
        self.assertEqual(str(linkedList), str(linkedList2))

    def test_iterate(self):
        linkedList = SinglyLinkedList([0, 1, 2, 3, 4, 5])
        for idx, node in enumerate(linkedList):
            self.assertEqual(type(node), SinglyNode)
            self.assertEqual(node.value, idx)

    def test_reverse(self):
        linkedList = SinglyLinkedList([0, 1, 2, 3, 4, 5])
        linkedList.reverse()
        linkedList2 = SinglyLinkedList([5, 4, 3, 2, 1, 0])
        self.assertEqual(str(linkedList), str(linkedList2))

    def test_append(self):
        linkedList = SinglyLinkedList([0, 1, 2, 3, 4, 5])
        linkedList.append(SinglyNode(6))
        linkedList.append(7)
        linkedList.append(SinglyLinkedList(SinglyNode(8, SinglyNode(9, SinglyNode(10)))))
        self.assertEqual(str(linkedList), " --> ".join(TestUtility.stringRange(11)))

    def test_prepend(self):
        linkedList = SinglyLinkedList([6, 7, 8, 9, 10])
        linkedList.prepend(SinglyNode(5))
        linkedList.prepend(4)
        linkedList.prepend(SinglyLinkedList(SinglyNode(1, SinglyNode(2, SinglyNode(3)))))
        self.assertEqual(str(linkedList), " --> ".join(TestUtility.stringRange(1, 11)))

    def test_removeNth(self):
        linkedList = SinglyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        linkedList.removeNth(5)
        self.assertEqual(str(linkedList), " --> ".join(TestUtility.stringRange(1, 6) + TestUtility.stringRange(7, 11)))
        self.assertRaises(Exception, linkedList.removeNth)
        self.assertRaises(Exception, SinglyLinkedList().removeNth, 1)
        linkedList2 = SinglyLinkedList([0, 1, 2, 3, 4])
        linkedList2.removeNth(0)
        self.assertEqual(str(linkedList2), " --> ".join(TestUtility.stringRange(1, 5)))


if __name__ == "__main__":
    unittest.main()
