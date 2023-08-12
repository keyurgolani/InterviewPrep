import unittest


class SinglyNode:
    """Singly Node is the node that stores a value and a pointer to another SinglyNode.
    This is useful in creating a Singly Linked List."""
    value = None

    def __init__(self, value, nextElement=None):
        self.value = value
        self.next = nextElement

    def __str__(self):
        """Get a stringified version of the Singly Node"""
        # Stringified version of a node has a ` --> ` at the end if the pointer points to something. (I.e., not `None`).
        return str(self.value) if not self.next else str(self.value) + " --> "


class SinglyNodeTest(unittest.TestCase):
    def test_createNode(self):
        self.assertEqual(str(SinglyNode('A')), 'A')
        self.assertEqual(str(SinglyNode(1)), '1')
        self.assertEqual(str(SinglyNode(None)), 'None')
        self.assertEqual(str(SinglyNode('A', SinglyNode('B', SinglyNode('C')))), 'A --> ')


if __name__ == "__main__":
    unittest.main()
