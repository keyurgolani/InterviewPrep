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


    """Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    https://leetcode.com/problems/median-of-two-sorted-arrays"""
    @staticmethod
    def medianOf(sortedArrayOne, sortedArrayTwo):
        """Brute Force:
        Merge both the arrays. Find median by finding the middle element of array.
        If the merged array has even elements, find the two middle elements and take their average.
        Runtime: O(m+n) Space: O(m+n)
        Optimized:
        Find the total size of merged array without actually merging the arrays (Just a sum of lengths of both the arrays).
        Figure out what element of the array will give us median of final array. Start merging two arrays from the beginning in merge sort method. 
        To do this, evaluate the smallest element on each array, pop the smallest of both and count it merged to the merged array (Again, do not actually merge the array).
        Upon reaching the element of array that will give us median, use those elements to find median and return.
        More Optimized:
        A median is the number that divides the resulting combined array into two equal halves.
        Hence, we can use binary search to split two parts of that array and find the index of such an element 
        that will give us half of the elements from resulting array less than the element and other half more than the element.
        
        Note: This is a leetcode hard problem. Not easy to explain in comments like this. A relatively much more detailed and easier to understand explaination is given here.
        https://leetcode.com/problems/median-of-two-sorted-arrays/editorial/"""
        # If no array has any value, return None.
        if not sortedArrayOne and not sortedArrayTwo:
            return None
        # We want to binary search on smaller array. So before assuming that first array will be smaller in length, if the counter is true, change that.
        if len(sortedArrayOne) > len(sortedArrayTwo):
            return NumberUtility.medianOf(sortedArrayTwo, sortedArrayOne)
        # After this point, we can assume that sortedArrayOne will always be smaller in length
        lengthOne, lengthTwo = len(sortedArrayOne), len(sortedArrayTwo)
        left, right = 0, lengthOne

        # Keep going until we shrink left and right side of the window together.
        while left <= right:
            # Find pivot for both the arrays
            pivotOne = (left + right) // 2
            pivotTwo = (lengthOne + lengthTwo + 1) // 2 - pivotOne

            # Find the elements around both these pivots
            maxLeftOne = float('-inf') if pivotOne == 0 else sortedArrayOne[pivotOne - 1]
            minRightOne = float('inf') if pivotOne == lengthOne else sortedArrayOne[pivotOne]
            maxLeftTwo = float('-inf') if pivotTwo == 0 else sortedArrayTwo[pivotTwo - 1]
            minRightTwo = float('inf') if pivotTwo == lengthTwo else sortedArrayTwo[pivotTwo]

            # If max value in left half of first array is less than or equal to min value in right half of second array
            # And max value in left half of second array is less than or equal to min value in right half of first array
            # Find median from inner edge elements from all four halves (elements around both pivots).
            if maxLeftOne <= minRightTwo and maxLeftTwo <= minRightOne:
                if (lengthOne + lengthTwo) % 2 == 0:
                    return (max(maxLeftOne, maxLeftTwo) + min(minRightOne, minRightTwo)) / 2
                else:
                    return max(maxLeftOne, maxLeftTwo)
            # If max value in left half of first array is grater than min value in right half of second array, we can eleminate right half of the first array.
            elif maxLeftOne > minRightTwo:
                right = pivotOne - 1
            # Else eleminate the left half of the first element
            else:
                left = pivotOne + 1


    """Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    https://leetcode.com/problems/reverse-integer"""
    @staticmethod
    def reverse(inputInteger):
        """Brute Force:
        To reverse an integer, identify that we are going to have to take least significant digits from inputInteger and put it on the most significant digit place in output.
        So we simply start with 0 as output. Until inputNumber is 0, repeat below process.
        Take the least significant digit from inputInteger using % 10. Multiply output with 10 and add obtained least significant digit to output.
        Finally, return output.
        To handle negative input, we will set a flag at the beginning of execution that will decide if the output is positive or negative.
        Note: To restrict this from returning outputs larger than 32-bit signed integers, we can add a size check before updating output at the last line of while loop. And return 0 if the output exceeds max signed 32-bit integer size.
        Runtime: O(log(n)) Space: O(1)"""
        # Remember if the input was negative.
        negativeInput = inputInteger < 0
        # If input was negative, make it positive. Otherwise, keep it as it is.
        inputInteger = inputInteger * (-1 if negativeInput else 1)
        # Start with 0 output.
        output = 0
        # Until all the input digits have been translated to output, keep going.
        while inputInteger != 0:
            # Find least significant digit from current inputInteger value
            targetDigit = inputInteger % 10
            # Remove the least significant digit from current inputInteger value
            inputInteger = inputInteger // 10
            # Append the found target digit to output increasing significance of all previously added digits.
            output = (output * 10) + targetDigit
        # Finally return output if input was positive, else return a negative version of output.
        return output if not negativeInput else output * -1





class NumberUtilityTest(unittest.TestCase):
    def test_findTwoElementsFrom_happyCase(self):
        self.assertEqual(set(NumberUtility.findTwoElementsFrom([2,7,11,15], 9)), set([0,1]))
        self.assertEqual(set(NumberUtility.findTwoElementsFrom([3,2,4], 6)), set([1,2]))
        self.assertEqual(set(NumberUtility.findTwoElementsFrom([3,3], 6)), set([0,1]))

    def test_findTwoElementsFrom_emptyInput(self):
        self.assertRaises(Exception, NumberUtility.findTwoElementsFrom, [], 9)
        self.assertRaises(Exception, NumberUtility.findTwoElementsFrom, None, 9)

    def test_addTwoNumbersRepresentedBy_happyCase(self):
        self.assertEqual(str(NumberUtility.addTwoNumbersRepresentedBy(SinglyLinkedList([3,4,2]), SinglyLinkedList([4,6,5]))), "8 --> 0 --> 7")
        self.assertEqual(str(NumberUtility.addTwoNumbersRepresentedBy(SinglyLinkedList([0]), SinglyLinkedList([0]))), "0")
        self.assertEqual(str(NumberUtility().addTwoNumbersRepresentedBy(SinglyLinkedList([9,9,9,9,9,9,9]), SinglyLinkedList([9,9,9,9]))), "1 --> 0 --> 0 --> 0 --> 9 --> 9 --> 9 --> 8")

    def test_addTwoNumbersRepresentedBy_emptyValues(self):
        self.assertEqual(str(NumberUtility.addTwoNumbersRepresentedBy(None, SinglyLinkedList([]))), "None")
        self.assertEqual(str(NumberUtility.addTwoNumbersRepresentedBy(SinglyLinkedList([]), SinglyLinkedList([]))), "")

    def test_medianOf_happyCase(self):
        self.assertEqual(NumberUtility.medianOf([1,3], [2]), 2)
        self.assertEqual(NumberUtility.medianOf([1,2], [3,4]), 2.5)

    def test_medianOf_emptyInput(self):
        self.assertEqual(NumberUtility.medianOf([1,3], []), 2)
        self.assertEqual(NumberUtility.medianOf([], [3,4]), 3.5)
        self.assertEqual(NumberUtility.medianOf([], []), None)

    def test_reverse(self):
        self.assertEqual(NumberUtility.reverse(123), 321)
        self.assertEqual(NumberUtility.reverse(-123), -321)
        self.assertEqual(NumberUtility.reverse(120), 21)
        self.assertEqual(NumberUtility.reverse(0), 0)

if __name__ == "__main__":
    unittest.main()