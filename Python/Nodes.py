import unittest

"""Singly Node is the node that stores a value and a pointer to another SinglyNode.
This is useful in creating a Singly Linked List."""
class SinglyNode:

    value = None

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    """Get a stringified version of the Singly Node"""
    def __str__(self):
        # Stringified version of a node has a ` --> ` at the end if the pointer does not point to nothing (i.e `None`).
        return str(self.value) if not self.next else str(self.value) + " --> "


class SinglyNodeTest(unittest.TestCase):
    def test_createNode(self):
        self.assertEqual('A', str(SinglyNode('A')))
        self.assertEqual('1', str(SinglyNode(1)))
        self.assertEqual('None', str(SinglyNode(None)))
        self.assertEqual('A --> ', str(SinglyNode('A', SinglyNode('B', SinglyNode('C')))))


if __name__ == "__main__":
    unittest.main()