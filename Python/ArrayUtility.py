import unittest

class ArrayUtility:
    """A team of analysts at needs to analyze the stock prices of a company over a period of several months.
    A group of consecutively chosen months is said to be maximum profitable if the price in its first or last month is the maximum for the group.
    More formally, a group of consecutive months [l, r] (1 ≤ l ≤ r ≤ n) is said to be maximum profitable if either:
    stockPrice[l] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r]) 
    or, stockPrice[r] = max(stockPrice[l], stockPrice[l + 1], ..., stockPrice[r])  
    Given prices over n consecutive months, find the number of maximum profitable groups which can be formed. Note that the months chosen must be consecutive, i.e., you must choose a subarray of the given array.
    
    Example,
    Consider there are n = 3 months of data, stockPrice = [2, 3, 2]. 
    All possible groups are shown in the leftmost column.
    | Possible Grouping | Stock Price of first month | Stock Price of last month | Maximum stock price in group | is Maximum Profitable? |
    | ----------------- | -------------------------- | ------------------------- | ---------------------------- | ---------------------- |
    | [2]               | 2                          | 2                         | 2                            | Yes                    |
    | [2, 3]            | 2                          | 3                         | 3                            | Yes                    |
    | [2, 3, 2]         | 2                          | 2                         | 3                            | No                     |
    | [3]               | 3                          | 3                         | 3                            | Yes                    |
    | [3, 2]            | 3                          | 2                         | 3                            | Yes                    |
    | [2]               | 2                          | 2                         | 2                            | Yes                    |
    
    All 5 groups other than prices [2, 3, 2] are maximum profitable. In [2, 3, 2], the maximum value 3 is neither the first nor the last element.
    Return 5."""
    @staticmethod
    def maxProfitableWindowCount(stockPrices):
        """Brute Force:
        Very basic way of achieving this result would be to iterate through the array of prices finding all possible sub-arrays.
        Go through each subarray identifying if the first or last element of given subarray is the max value i.e determining if the subarray is max profitable.
        If the subarray is max profitable, increment a global counter and move on.
        At the end, return the global counter.
        Runtime: O(n^3) Space: O(1) --> This is because we will find n^2 subarrays and to find their max we will have to iterate each of them once more.
        Optimized:
        One way to approach this, would be to realize that we can directly target counting the max profitable subarrays instead of going through all of them and identifying max profitable.
        To do this, we will identify that, any subarray that starts or ends at the max value in given array, will be max profitable.
        Also, any other array that contains the max value in given array, will not be max profitable because the start or end value can never be max.
        Hence, out of all the arrays that include max element in an array, we can count number of subarrays starting or ending in max element and ignore all other subarrays.
        After this, we can start breaking down this problem in pieces and hone in on the arrays that are created by searating main array into two from max element. Repeat the above process on both new parts of arrays and keep repeating.
        Finally, the base condition for recursion will be when the array has just one element where it will always be max profitable.
        On each iteration, we send back the max profitable window counts for the subarray we're operating on. At the end, we get desired result for the whole array.
        Runtime: O(log2(n)) Space: O(1) --> Here, recursive calls will occupy O(log2(n)) heap space but no additional space used by code"""
        # Recursive version of the method that will take the left and right bounds of original array and treat that window as the original array for given recursion.
        # Within this method, we will refer the subarray from left to right (right including) as the original array going forward.
        def findMaxProfitableWindowCount(left, right):
            # We will always have max profitable windows as the amount of elements in original array.
            # This is because all elements will have a window that either starts at given element and ends at max element in that array or starts at max element in that array and ends at given element.
            answer = (right - left + 1)
            # If left and right point to the same element, we will only return answer (only one element so answer will be 1) for this recursion.
            # However, if left and right form a window that contains more than one elements, we count more max profitable windows contained within subwindows.
            if right - left != 0:
                # We need to find the index of max element in given array to identify where to split the array from. Initialize it to None and max element to 0.
                maxElementIndex = None
                maxElement = 0
                # Iterate over all the elements in original array and figure out the max element and what its index is.
                for idx in range(left, right + 1):
                    if maxElement < stockPrices[idx]:
                        maxElement = stockPrices[idx]
                        maxElementIndex = idx
                # If we found a max element and the index was updated from original None, we split the original array into subarrays excluding max element. And add the answer from recursion to current answer.
                if maxElementIndex is not None:
                    answer += findMaxProfitableWindowCount(left, maxElementIndex - 1) + findMaxProfitableWindowCount(maxElementIndex + 1, right)
            # Once we have added all elements of answer, return answer
            return answer
        # Return answer from recursive function call over the whole array span
        return findMaxProfitableWindowCount(0, len(stockPrices) - 1)


class ArrayUtilityTest(unittest.TestCase):
    def test_maxProfitableWindowCount(self):
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([2, 3, 2]), 5)
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([1, 2, 3, 4, 3, 2, 3, 4, 5, 2, 3, 2, 1, 3, 4, 5, 2, 1, 4, 6, 3, 2]), 102)
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 55)
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([1, 2, 3, 4, 5, 4, 3, 2, 1]), 29)
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([3, 2, 3]), 6)
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([2]), 1)
        self.assertEqual(ArrayUtility.maxProfitableWindowCount([]), 0)


if __name__ == "__main__":
    unittest.main()