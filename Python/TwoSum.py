import unittest

class Utility:
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
        Runtime: O(n) Space: O(1)
        """
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


class UtilityTest(unittest.TestCase):
    def test_findTwoElementsFrom_happyCase(self):
        self.assertEqual(set([0,1]), set(Utility.findTwoElementsFrom([2,7,11,15], 9)))
        self.assertEqual(set([1,2]), set(Utility.findTwoElementsFrom([3,2,4], 6)))
        self.assertEqual(set([0,1]), set(Utility.findTwoElementsFrom([3,3], 6)))

    def test_findTwoElementsFrom_emptyInput(self):
        self.assertRaises(Exception, Utility.findTwoElementsFrom, [], 9)
        self.assertRaises(Exception, Utility.findTwoElementsFrom, None, 9)

if __name__ == "__main__":
    unittest.main()