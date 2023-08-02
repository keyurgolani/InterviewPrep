import unittest

class StringUtility:
    """Given a string s, find the length of the longest substring without repeating characters.
    A substring is a contiguous non-empty sequence of characters within a string.
    https://leetcode.com/problems/longest-substring-without-repeating-characters/"""
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
        
    """Given a string s, return the longest palindromic substring in s.
    Palindromic - A string is palindromic if it reads the same forward and backward.
    Substring - A substring is a contiguous non-empty sequence of characters within a string.
    https://leetcode.com/problems/longest-palindromic-substring/"""
    @staticmethod
    def longestPalindromicSubstringIn(inputString):
        """Brute Force:
        Use two pointers to point to a starting and an ending position within the inputString that would denote a substring.
        Go through each value for pointer such that we iterate over all possible substrings of given inputString.
        While iterating over each possible substring, identify if the substring is palindromic.
        To identify if the substring is palindromic, start traversing the substring character by character, match characters from front of the substring and back.
        If all characters from front and back are the same until comparison reaches mid point of substring, we identify that the substring is palindromic.
        If the substring that we are iterating over, is palindromic, check its length. If it's larger than previously seen maximum length palindromic substring, update the saved result.
        At the end after checking all the palindromic substrings, return the final value of the saved max length palindromic substring.
        Runtime: O(n^3) Space: O(1)
        Optimized:
        Because in previous approach, we are using start and end indices as our bases, many of the palindromic substring checking work is duplicated.
        For example, if the inputString was `abba`, we will check substring `bb` to be palindromic 4 times within each 3 or more length substring of the inputString.
        Instead, one optimization could be, iterating through each character in inputString, expanding outside from the character as center of palindromic substring.
        This way, we go as far as we can go with given character as the center of palindrome, and if it's larger length than one we've seen before, we update the max length we've seen so far.
        After doing this with each character of the inputString, we look at another possibility that the palindromic substring might be of even length.
        Here, the two center characters will be a duplicate pair.
        So we iterate through each character in the inputString again finding a pair of duplicate characters next to eachother.
        We expand from there on each side to see how long a palindromic substring with those characters at the center could be, again updating the max length we've seen so far if we find one.
        At the end after the iteration is done, return the final value of the saved max length palindromic substring we've seen so far.
        Runtime: O(n^2) Space: O(1)"""
        # Cannot process None input. Return None.
        if inputString is None:
            return None
        # Initiate an empty string as longest palindromic substring since if inputString is empty, this will be returned as it is.
        longestPalindromicSubstringSoFar = ""
        # Iterate over each index looking for longest palindromic substring we can form with character at given index at the center.
        for idx in range(len(inputString)):
            # When thinking of current character at the center of palindromic substring, the current index itself will make the smallest palindromic substring possible already.
            currentPalindromicSubstring = inputString[idx]
            # Since the current character is already assigned as the current palindromic substring, we will start looking one index around the center character.
            lookaroundWindowLength = 1
            # Ensure that while expanding lookaround window, we don't go out of bounds.
            while (idx + lookaroundWindowLength) < len(inputString) and (idx - lookaroundWindowLength) >= 0:
                # Initialize left and right pointers for the lookaround window to use them easily
                leftLookupIndex = idx - lookaroundWindowLength
                rightLookupIndex = idx + lookaroundWindowLength
                # If the characters at left lookup and right lookup are not the same, break out of this loop.
                # This is because a character being different will make all larger substrings with current character as center, will be non-palindromic.
                if inputString[leftLookupIndex] != inputString[rightLookupIndex]:
                    break
                # If characters at left lookup and right lookup are the same, update palindromic substring seen so far with current character at the center.
                currentPalindromicSubstring = inputString[leftLookupIndex:rightLookupIndex+1]
                # Increase the lookup window length for next iteration.
                lookaroundWindowLength += 1
            # We are breaking before updating current palindromic substring when encountering different characters at both lookup indices.
            # Hence, we can be sure that at the end of while loop, current palindromic substring will be longest one with current character in center.
            # So, compare it with the longest palindromic substring seen so far and update if needed.
            longestPalindromicSubstringSoFar = max(longestPalindromicSubstringSoFar, currentPalindromicSubstring, key=len)
        # We need to repeat the same thing we've done above only with current character (the character at the center of palindromic substring), being a pair of duplicate characters next to eachother.
        # This is to identify the palindromic substrings of even lengths.
        # Hence go over each index in string. We want to start from 1 here since we will be able to compare the character pair idx, idx - 1 for duplicate characters.
        for idx in range(1, len(inputString)):
            # Only if the characters at idx and idx - 1 are the same, we can have palindromic substring with these two characters as their center.
            if inputString[idx] == inputString[idx - 1]:
                # Instead of initializing current palindromic substring as character at idx (current character), we will initialize it as the pair of characters that we know are equal (idx, idx - 1)
                currentPalindromicSubstring = inputString[idx-1:idx+1]
                # Same lookaround window, the same idea as previous occurrance.
                lookaroundWindowLength = 1
                # This time we will subtract 1 from left lookup index because we are already working with a center pair that's idx and idx - 1 characters.
                while (idx + lookaroundWindowLength) < len(inputString) and (idx - 1 - lookaroundWindowLength) >= 0:
                    leftLookupIndex = idx - 1 - lookaroundWindowLength
                    rightLookupIndex = idx + lookaroundWindowLength
                    # Same execution as before.
                    if inputString[leftLookupIndex] != inputString[rightLookupIndex]:
                        break
                    # Same execution as before.
                    currentPalindromicSubstring = inputString[leftLookupIndex:rightLookupIndex+1]
                    # Same idea as before.
                    lookaroundWindowLength += 1
                # Same idea as before.
                longestPalindromicSubstringSoFar = max(longestPalindromicSubstringSoFar, currentPalindromicSubstring, key=len)
        # After running through all possible palindromic substrings with one character at the center and updating the longest one we find.
        # And running through all possible palindromic substrings with a pair of duplicate characters at the center and updating longest one we find.
        # We can simply return the longest palindromic substring so far because we've checked all possible palindromic substrings for given inputString.
        return longestPalindromicSubstringSoFar


class StringUtilityTest(unittest.TestCase):
    def test_longestSubstringWithoutRepeatingCharactersFrom_happyCase(self):
        self.assertEqual(3, StringUtility.longestSubstringWithoutRepeatingCharactersFrom("abcabcbb"))
        self.assertEqual(1, StringUtility.longestSubstringWithoutRepeatingCharactersFrom("bbbbb"))
        self.assertEqual(3, StringUtility.longestSubstringWithoutRepeatingCharactersFrom("pwwkew"))

    def test_longestSubstringWithoutRepeatingCharactersFrom_emptyInput(self):
        self.assertEqual(0, StringUtility.longestSubstringWithoutRepeatingCharactersFrom(""))
        self.assertEqual(None, StringUtility.longestSubstringWithoutRepeatingCharactersFrom(None))

    def test_longestPalindromicSubstringIn_happyCase(self):
        self.assertEqual("abcba", StringUtility.longestPalindromicSubstringIn("abcba"))
        # Since this reveals that python unittest prefers `seen` value as first parameter and `actual` parameter as second value, we will do a refactor changing the order of arguments in all the asserts in next commit.
        self.assertIn(StringUtility.longestPalindromicSubstringIn("babad"), ["aba", "bab"])
        self.assertEqual("bb", StringUtility.longestPalindromicSubstringIn("cbbd"))

    def test_longestPalindromicSubstringIn_emptyInput(self):
        self.assertEqual("", StringUtility.longestPalindromicSubstringIn(""))
        self.assertEqual(None, StringUtility.longestPalindromicSubstringIn(None))


if __name__ == "__main__":
    unittest.main()