import unittest
from LinkedList import SinglyLinkedList
from Nodes import SinglyNode

class NumberUtility:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    https://leetcode.com/problems/two-sum/"""
    @staticmethod
    def findTwoElementsFrom(inputNumbers, sumToTarget):
        """Brute Force:
        Simply iterate over the inputNumbers once.
        For every number, iterate over all the inputNumbers to it's right once more.
        Within each iteration, sum the two numbers that each loop points to.
        If the sum of these two numbers amount to sumToTarget, return the index of both these numbers.
        After iterating over all the elements in outermost loop, if you don't find any number pair summing to sumToTarget, raise Error.
        Runtime: O(n^2) Space: O(1)
        Optimized:
        Here we trade off space and gain runtime.
        Use a memory where we will store the numbers from inputNumbers that we've already seen while iterating through inputNumbers.
        Visit number at each index once. For each number, check if we have added this number to memory before.
        If not, add the difference between sumToTarget and current number to the memory. Also store the index of current number next to it on the memory.
        This means in another iteration, if we see (sumToTarget - current number) in the inputNumbers we know that we've seen it's pair already.
        If we have the current number in memory, return the index obtained from memory and index of current number.
        Runtime: O(n) Space: O(1)"""
        if inputNumbers is None:
            raise Exception("InvalidInputError")
        # Initialize memory used to remember the elements that we've seen in previous iterations
        memory = {}
        # Iterate through each number in inputNumbers
        for idx in range(len(inputNumbers)):
            # Check if given number is a compliment of another number we've seen in previous iterations
            # Here, compliment of a number is the difference between sumToTarget and the number
            if inputNumbers[idx] in memory.keys():
                # If so, return indices of the current iteration and the iteration that the compliment was seen.
                return [idx, memory[inputNumbers[idx]]]
            else:
                # If not, remember the compliment of current number and index it was seen at
                memory[sumToTarget - inputNumbers[idx]] = idx
        else:
            # If at the end of all iterations, we didn't find a complementing pair, raise Error
            raise Exception("InvalidInputError")

    """You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list. 
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    https://leetcode.com/problems/add-two-numbers/
    
    Note: Let's do a slight modification of this problem that is more commonly known.
    Here, numbers are represented by linked lists. Not in reverse order but in forward order.
    Example, 342 will be represented by 3 --> 4 --> 2 and 465 will be represented by 4 --> 6 --> 5."""
    @staticmethod
    def addTwoNumbersRepresentedBy(linkedListOne, linkedListTwo):
        """Brute Force: 
        Convert both the linked list representations of numbers into integers.
        Add them. And convert the result into a linked list representation.
        This may overflow the int capacity since linkedlist could represent very very large numbers very easily.
        Runtime: O(n) Space: O(1)
        Optimized:
        Traverse both the linked list representations of numbers separately. Add each element into a stack each.
        Initialize a carry value and until any of the stacks have an element, pop one element from both the stacks at a time.
        When one stack doesn't have an element and the other stacks does, we assume that the empty stack is giving an element with value 0.
        Each time elements from the stacks are popped, add values of them both. Add carry, if any, to the result.
        Use the ones position digit from the result to append to answer and save 10s position digit as carry.
        To append the digits to answer, create linked list nodes with given value, mark that node as head and point its next to previous head.
        Return the final head element.
        Runtime: O(n) Space: O(n)
        More Optimized:
        Reverse both the linked lists representing numbers. Initialize a variable to save carries.
        Traverse both the linked lists together one node at a time. If one of the linked lists ends, assume that it's giving nodes with value 0.
        Add values from both the nodes. Add carry to the result if any.
        Use the ones position digit from the result to append to answer and save 10s position digit as carry.
        To append the digits to answer, create linked list nodes with given value, append them to the result linked list.
        Reverse the final result and return the final head element or the linked list object.
        Runtime: O(n) Space: O(1)"""
        # If any input is None, we cannot process them. So return None.
        if linkedListOne is None or linkedListTwo is None:
            return None
        # If both inputs are empty, effectively means input numbers are 0. Return any one of them representing 0 result.
        if not linkedListOne and not linkedListTwo:
            return linkedListOne
        # Initialize the carry to be 0 in the beginning.
        currentCarry = 0
        # Reverse both the linked lists since digit by digit addition is done from least significant digit to most significant digit.
        linkedListOne.reverse()
        linkedListTwo.reverse()
        # Start traversal of both the lists together from head of both the lists.
        currentOne, currentTwo = linkedListOne.head, linkedListTwo.head
        # Initialize result to be empty linked list at the beginning.
        result = SinglyLinkedList()
        # Iterate over lists while at least one of the lists have elements left to iterate over.
        while currentOne or currentTwo:
            # If one of the lists had no elements left, assume that it gave an element with value 0.
            currentOneValue = currentOne.value if currentOne else 0
            currentTwoValue = currentTwo.value if currentTwo else 0
            # Sum values of elements from both the lists and add the value of current carry to it.
            sum = currentOneValue + currentTwoValue + currentCarry
            # Ones digit will go to the result and tens digit will become current carry.
            onesPlaceDigit = sum % 10
            tensPlaceDigit = sum // 10
            currentResultNode = SinglyNode(onesPlaceDigit)
            result.append(currentResultNode)
            currentCarry = tensPlaceDigit
            # Move pointers for iteration over to next nodes in each list
            currentOne, currentTwo = currentOne.next if currentOne else None, currentTwo.next if currentTwo else None
        # At the end of processing both the lists, if a carry was leftover, it will add another significant digit to the result. Append it to result.
        if currentCarry:
            result.append(SinglyNode(currentCarry))
        # Reverse the answer to represent the answer in correct order
        result.reverse()
        return result




class NumberUtilityTest(unittest.TestCase):
    def test_findTwoElementsFrom_happyCase(self):
        self.assertEqual(set([0,1]), set(NumberUtility.findTwoElementsFrom([2,7,11,15], 9)))
        self.assertEqual(set([1,2]), set(NumberUtility.findTwoElementsFrom([3,2,4], 6)))
        self.assertEqual(set([0,1]), set(NumberUtility.findTwoElementsFrom([3,3], 6)))

    def test_findTwoElementsFrom_emptyInput(self):
        self.assertRaises(Exception, NumberUtility.findTwoElementsFrom, [], 9)
        self.assertRaises(Exception, NumberUtility.findTwoElementsFrom, None, 9)

    def test_addTwoNumbersRepresentedBy_happyCase(self):
        self.assertEqual("8 --> 0 --> 7", str(NumberUtility().addTwoNumbersRepresentedBy(SinglyLinkedList([3,4,2]), SinglyLinkedList([4,6,5]))))
        self.assertEqual("0", str(NumberUtility().addTwoNumbersRepresentedBy(SinglyLinkedList([0]), SinglyLinkedList([0]))))
        self.assertEqual("1 --> 0 --> 0 --> 0 --> 9 --> 9 --> 9 --> 8", str(NumberUtility().addTwoNumbersRepresentedBy(SinglyLinkedList([9,9,9,9,9,9,9]), SinglyLinkedList([9,9,9,9]))))

    def test_addTwoNumbersRepresentedBy_emptyValues(self):
        self.assertEqual("None", str(NumberUtility().addTwoNumbersRepresentedBy(None, SinglyLinkedList([]))))
        self.assertEqual("", str(NumberUtility().addTwoNumbersRepresentedBy(SinglyLinkedList([]), SinglyLinkedList([]))))

if __name__ == "__main__":
    unittest.main()