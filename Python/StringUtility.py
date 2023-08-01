import unittest

class StringUtility:
    """Given a string s, find the length of the longest substring without repeating characters.
    A substring is a contiguous non-empty sequence of characters within a string."""
    @staticmethod
    def longestSubstringWithoutRepeatingCharactersFrom(inputString):
        """Brute Force:
        Run through the inputString with two loops iterating over with a start and an end pointer finding all the possible substrings.
        Filter out the substrings that have repeating characters.
        Find the longest of the remaining substrings. Return its length.
        Runtime: O(n^3) Space: O(1)
        Optimized:
        Use two pointers to form a sliding window that will slide over the inputString and box in the substring with no repeating character.
        Save a counter of the elements that are inside the sliding window in a hashset.
        While adding a character to sliding window, check the character against the hashset.
        If the set contains the character, iterate over to given character's slide over the left pointer of sliding window over till repeating character is eliminated.
        Update hashset accordingly.
        While doing this, keep track of every valid sliding window's length and update the max.
        Return max length at the end when right pointer to sliding window reaches the end of the inputString.
        Runtime: O(n) Space: O(n)"""
        # If the inputString is None, return None since we cannot operate on the input.
        if inputString is None:
            return None
        # Initialize the max length for substring and left and right pointers for the sliding window.
        slidingWindowMaxLength, left, right = 0, 0, 0
        # Initialize the sliding window inventory that will keep track of elements inside the sliding window.
        slidingWindowInventory = set()
        # We want to keep moving the sliding window to right until we reach the end.
        while right < len(inputString):
            # If the right edge of sliding window is in inventory already, means that we have encountered it previously and it's in our sliding window already.
            if inputString[right] in slidingWindowInventory:
                # In that case, until we find the character on right edge of window inside the window, move left pointer to that.
                # Also remove the elements that we are moving the sliding window over from the sliding window inventory.
                while inputString[left] != inputString[right]:
                    slidingWindowInventory.remove(inputString[left])
                    left += 1
                # When we find the other occurrance of the character on right edge of window inside the window, we also want to remove that character and move the left edge of window once to the right.
                slidingWindowInventory.remove(inputString[left])
                left += 1
            # Now, we are sure that if the element on right edge of sliding window was present anywhere else in sliding window, we have removed it by shrinking our window from left side.
            # Add character on the right edge of sliding window to the inventory.
            slidingWindowInventory.add(inputString[right])
            # Since we have removed the duplicate of given character before adding another occurrance of it, at this point, our sliding window will be valid. So find it's length and update max length.
            # Valid sliding window is where we have the left and right pointers in such a place where substring contained between them doesn't contain duplicates.
            slidingWindowMaxLength = max(slidingWindowMaxLength, right - left + 1)
            # Move right pointer over to next element for next iteration.
            right = right + 1
        return slidingWindowMaxLength


class StringUtilityTest(unittest.TestCase):
    def test_longestSubstringWithoutRepeatingCharactersFrom_happyCase(self):
        self.assertEqual(3, StringUtility.longestSubstringWithoutRepeatingCharactersFrom("abcabcbb"))
        self.assertEqual(1, StringUtility.longestSubstringWithoutRepeatingCharactersFrom("bbbbb"))
        self.assertEqual(3, StringUtility.longestSubstringWithoutRepeatingCharactersFrom("pwwkew"))

    def test_longestSubstringWithoutRepeatingCharactersFrom_emptyInput(self):
        self.assertEqual(0, StringUtility.longestSubstringWithoutRepeatingCharactersFrom(""))
        self.assertEqual(None, StringUtility.longestSubstringWithoutRepeatingCharactersFrom(None))


if __name__ == "__main__":
    unittest.main()