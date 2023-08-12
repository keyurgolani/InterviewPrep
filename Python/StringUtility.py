import unittest


class StringUtility:
    """Contains methods that operate on strings."""

    @staticmethod
    def longestSubstringWithoutRepeatingCharactersFrom(inputString):
        """Problem:
        Given a string s, find the length of the longest substring without repeating characters.
        A substring is a contiguous non-empty sequence of characters within a string.
        Https://leetcode.com/problems/longest-substring-without-repeating-characters/

        Brute Force Solution:
        Run through the inputString with two loops iterating over with a start and an end pointer finding all the possible substrings.
        Filter out the substrings that have repeating characters.
        Find the longest of the remaining substrings. Return its length.
        Runtime: O(n^3) Space: O(1)

        Optimized Solution:
        Use two pointers to form a sliding window that will slide over the inputString and box in the substring with no repeating character.
        Save a counter of the elements that are inside the sliding window in a hashset.
        While adding a character to the sliding window, check the character against the hashset.
        If the set contains the character, iterate over to given character's slide over the left pointer of the sliding window over till repeating character is eliminated.
        Update hashset accordingly.
        While doing this, keep track of every valid sliding window's length and update the max.
        Return max length at the end when the right pointer to the sliding window reaches the end of the inputString.
        Runtime: O(n) Space: O(n)"""
        # If the inputString is None, return None since we cannot operate on the input.
        if inputString is None:
            return None
        # Initialize the max length for substring and left and right pointers for the sliding window.
        slidingWindowMaxLength, left, right = 0, 0, 0
        # Initialize the sliding window inventory that will keep track of elements inside the sliding window.
        slidingWindowInventory = set()
        # We want to keep moving the sliding window to the right until we reach the end.
        while right < len(inputString):
            # If the right edge of the sliding window is in inventory already, means that we have encountered it previously, and it's in our sliding window already.
            if inputString[right] in slidingWindowInventory:
                # In that case, until we find the character on the right edge of the window inside the window, move the left pointer to that.
                # Also remove the elements that we are moving the sliding window over from the sliding window inventory.
                while inputString[left] != inputString[right]:
                    slidingWindowInventory.remove(inputString[left])
                    left += 1
                # When we find the other occurrence of the character on the right edge of the window inside the window, we also want to remove that character and move the left edge of the window once to the right.
                slidingWindowInventory.remove(inputString[left])
                left += 1
            # Now, we are sure that if the element on the right edge of the sliding window was present anywhere else in the sliding window, we have removed it by shrinking our window from the left side.
            # Add character on the right edge of the sliding window to the inventory.
            slidingWindowInventory.add(inputString[right])
            # Since we have removed the duplicate of given character before adding another occurrence of it, at this point, our sliding window will be valid.
            # So find its length and update max length.
            # Valid sliding window is where we have the left and right pointers in such a place where substring contained between them doesn't contain duplicates.
            slidingWindowMaxLength = max(
                slidingWindowMaxLength, right - left + 1)
            # Move the right pointer over to next element for next iteration.
            right = right + 1
        return slidingWindowMaxLength

    @staticmethod
    def longestPalindromicSubstringIn(inputString):
        """Problem:
        Given a string s, return the longest palindromic substring in s.
        Palindromic - A string is palindromic if it reads the same forward and backward.
        Substring - A substring is a contiguous non-empty sequence of characters within a string.
        https://leetcode.com/problems/longest-palindromic-substring/

        Brute Force Solution:
        Use two pointers to point to a starting and an ending position within the inputString that would denote a substring.
        Go through each value for the pointer such that we iterate over all possible substrings of given inputString.
        While iterating over each possible substring, identify if the substring is palindromic.
        To identify if the substring is palindromic, start traversing the substring character by character, match characters from front of the substring and back.
        If all characters from front and back are the same until comparison reaches mid-point of substring, we identify that the substring is palindromic.
        If the substring that we are iterating over is palindromic, check its length.
        If it's larger than previously seen maximum length palindromic substring, update the saved result.
        In the end, after checking all the palindromic substrings, return the final value of the saved max length palindromic substring.
        Runtime: O(n^3) Space: O(1)

        Optimized Solution:
        Because in previous approach, we are using start and end indices as our bases, much of the palindromic substring checking work is duplicated.
        For example, if the inputString was `abba`, we will check substring `bb` to be palindromic four times within each 3 or more lengths substring of the inputString.
        Instead, one optimization could be, iterating through each character in inputString, expanding outside from the character as the center of palindromic substring.
        This way, we go as far as we can go with given character as the center of palindrome, and if it's a larger length than one we've seen before, we update the max length we've seen so far.
        After doing this with each character of the inputString, we look at another possibility that the palindromic substring might be of even length.
        Here, the two-center characters will be a duplicate pair.
        So we iterate through each character in the inputString again finding a pair of duplicate characters next to each other.
        We expand from there on each side to see how long the palindromic substring with those characters at the center could be, again updating the max length we've seen so far if we find one.
        In the end, after the iteration is done, return the final value of the saved max length palindromic substring we've seen so far.
        Runtime: O(n^2) Space: O(1)"""
        # Cannot process None input. Return None.
        if inputString is None:
            return None
        # Initiate an empty string as the longest palindromic substring since if inputString is empty, this will be returned as it is.
        longestPalindromicSubstringSoFar = ""
        # Iterate over each index looking for the longest palindromic substring we can form with character at given index at the center.
        for idx in range(len(inputString)):
            # When thinking of the current character at the center of palindromic substring, the current index itself will make the smallest palindromic substring possible already.
            currentPalindromicSubstring = inputString[idx]
            # Since the current character is already assigned as the current palindromic substring, we will start looking one index around the center character.
            lookaroundWindowLength = 1
            # Ensure that while expanding the lookaround window, we don't go out of bounds.
            while (idx + lookaroundWindowLength) < len(inputString) and (idx - lookaroundWindowLength) >= 0:
                # Initialize left and right pointers for the lookaround window to use them easily
                leftLookupIndex = idx - lookaroundWindowLength
                rightLookupIndex = idx + lookaroundWindowLength
                # If the characters at left lookup and right lookup are not the same, break out of this loop.
                # This is because a character being different will make all larger substrings with current character as the center, will be non-palindromic.
                if inputString[leftLookupIndex] != inputString[rightLookupIndex]:
                    break
                # If characters at left lookup and right lookup are the same, update palindromic substring seen so far with current character at the center.
                currentPalindromicSubstring = inputString[leftLookupIndex:rightLookupIndex + 1]
                # Increase the lookup window length for the next iteration.
                lookaroundWindowLength += 1
            # We are breaking before updating current palindromic substring when encountering different characters at both lookup indices.
            # Hence, we can be sure that at the end of the 'while' loop, current palindromic substring will be the longest one with current character in center.
            # So, compare it with the longest palindromic substring seen so far and update if needed.
            longestPalindromicSubstringSoFar = max(longestPalindromicSubstringSoFar, currentPalindromicSubstring, key=len)
        # We need to repeat the same thing we've done above only with the current character (the character at the center of palindromic substring), being a pair of duplicate characters next to each-other.
        # This is to identify the palindromic substrings of even lengths.
        # Hence, go over each index in string. We want to start from one here since we will be able to compare the character pair idx, idx - 1 for duplicate characters.
        for idx in range(1, len(inputString)):
            # Only if the characters at idx and idx - 1 are the same, we can have palindromic substring with these two characters as their center.
            if inputString[idx] == inputString[idx - 1]:
                # Instead of initializing current palindromic substring as character at idx (current character), we will initialize it as the pair of characters that we know are equal (idx, idx - 1)
                currentPalindromicSubstring = inputString[idx - 1:idx + 1]
                # Same lookaround window, the same idea as previous occurrence.
                lookaroundWindowLength = 1
                # This time we will subtract 1 from left lookup index because we are already working with a center pair that's idx and idx - 1 characters.
                while (idx + lookaroundWindowLength) < len(inputString) and (idx - 1 - lookaroundWindowLength) >= 0:
                    leftLookupIndex = idx - 1 - lookaroundWindowLength
                    rightLookupIndex = idx + lookaroundWindowLength
                    # Same execution as before.
                    if inputString[leftLookupIndex] != inputString[rightLookupIndex]:
                        break
                    # Same execution as before.
                    currentPalindromicSubstring = inputString[leftLookupIndex:rightLookupIndex + 1]
                    # Same idea as before.
                    lookaroundWindowLength += 1
                # Same idea as before.
                longestPalindromicSubstringSoFar = max(
                    longestPalindromicSubstringSoFar, currentPalindromicSubstring, key=len)
        # After running through all possible palindromic substrings with one character at the center and updating the longest one we find.
        # And running through all possible palindromic substrings with a pair of duplicate characters at the center and updating the longest one we find.
        # We can simply return the longest palindromic substring so far because we've checked all possible palindromic substrings for given inputString.
        return longestPalindromicSubstringSoFar

    @staticmethod
    def zigzagEncodingOf(inputString, inRowCount):
        """Problem:
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"
        Write the code that will take a string and make this conversion given a number of rows.
        Https://leetcode.com/problems/zigzag-conversion

        Brute Force Solution:
        Zigzag pattern given in the problem description, gives us a great way of approaching a solution.
        We start with iterating over each character from the string.
        For each character, we move to another row in output and append the character to that row.
        To decide which row we move to, start in an increasing pattern from zero and invert the pattern to a decreasing pattern when we reach the end row.
        Vice versa for the first row where we'd invert back the pattern-increasing pattern.
        After creating output rows, join them into a string and return.
        Runtime: O(n) Space: O(n)

        Optimized Solution:
        To approach this problem, we can realize that this is a very niche mathematical problem where for every index in output, we need to figure out the formula to what character from input will go there.
        We can find out the number of characters that will go in one repetition of the pattern.
        Here, a pattern is one combination of zig and zag that includes one vertical column and one diagonal column.
        We can also realize from different combinations of input size and row counts that the first and last row will have one character per pattern and other rows will have two characters per pattern.
        Since output will have characters appended row by row for given row count, we will iterate through each row's index, identify characters from inputString with math for vertical column characters and diagonal column characters and move on."""
        # If there's no row count, we cannot for the output so return None
        if not inRowCount:
            return None
        # If input needs to be transformed in one row, it will stay the same.
        # If input needs to be transformed in rows equal to the length of input string, it will stay the same too.
        if inRowCount == 1 or inRowCount >= len(inputString):
            return inputString
        # Initialize an empty answer.
        answer = ""
        # On each pattern of zig + zag this many characters will appear.
        charactersInOnePattern = (2 * inRowCount) - 2
        # On a row that's not first or last, diagonal elements will appear in addition to vertical elements.
        # Find out how many elements to jump from a vertical element in the same row to the next diagonal element in the same row.
        diagonalCharacterJump = charactersInOnePattern
        # Initialize the pointer that will be used to find characters from input string.
        inputPointer = 0
        # Sometimes we'll have to keep track of the main pointer and use a backup pointer where we populate the diagonal character appearing in the same row. So initialize that too.
        backupPointer = 0
        # Go through each row and append it to answer.
        for idx in range(inRowCount):
            # Start pointer with the row index since each row will start from row index character from inputString
            inputPointer = idx
            # While the pointer doesn't point outside the string, keep going
            while inputPointer < len(inputString):
                # Append the character that inputPointer points to the answer.
                answer += inputString[inputPointer]
                # If currently being processed row is a row other than first and last rows, we have to do extra work to append the diagonal characters.
                if idx != 0 and idx != inRowCount - 1:
                    # To reach diagonal character in a row from vertical column character in the same row, we have to jump the number of characters below both of these characters in both the columns.
                    # Total characters in both these columns are charactersInOnePattern.
                    # However, if you're at idx row, the characters above given character in each column will element idx number of characters from jump.
                    # So we need to jump charactersInOnePattern - (2 * idx) characters to find a diagonal character in the same row from a vertical column character.
                    diagonalCharacterJump = charactersInOnePattern - (2 * idx)
                    # Use the backup pointer to find diagonal character.
                    backupPointer = inputPointer + diagonalCharacterJump
                    # Diagonal character can be absent if we're processing last zig + zag pattern where we ran out of inputString before creating the zag pattern.
                    # So if the diagonal character exists, append to answer.
                    if backupPointer < len(inputString):
                        answer += inputString[backupPointer]
                # Since we didn't use the primary pointer for diagonal character, the primary pointer is at the same place where the last vertical column character for given row was found.
                # Hence, for the next vertical column character in given row, jump the charactersInOnePattern.
                inputPointer += charactersInOnePattern
        return answer

    @staticmethod
    def stringToInteger(inputString):
        """Problem:
        Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
        The algorithm for myAtoi(string s) is as follows:
        Read in and ignore any leading white-space.
        Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
        Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
        Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
        If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
        Return the integer as the final result.

        Note:
        Only the space character ' ' is considered a white-space character.
        Do not ignore any characters other than the leading white-space or the rest of the string after the digits.
        https://leetcode.com/problems/string-to-integer-atoi

        Brute Force Solution:
        As instructed, we will start with the first character iterating through each character of the input string.
        We will have a logic for handling each type of character encountered.
        For white-space, we will keep a flag that indicates if we've already encountered any digit.
        If we have, space, just like any other character, will break the conversion and return answer.
        If we haven't, space will be ignored because it's a leading white-space.
        Similarly, + or - will only be entertained if it's encountered before encountering the first digit.
        Otherwise, they will stop the conversion and return answer.
        Encountering any other character, we will stop the conversion and return answer.
        Runtime: O(n) Space: O(1)"""
        # Initialize flags for 
        # weather we've already encountered a digit
        # weather we've encountered a + / - sign or not
        # weather the sign encountered was negative or not.
        digitEncountered = False
        signEncountered = False
        isNegative = False
        # Initialize output as 0
        output = 0
        # Go over each character and if the character is eligible, adding to output before moving to next.
        for character in inputString:
            # If the character encountered is + / - sign, we only want to entertain it if we've not seen a sign or digit before.
            if character in ['+', '-'] and not digitEncountered and not signEncountered:
                # Set flag for the sign of the integer encountered and the fact that a sign was encountered
                isNegative = character == '-'
                signEncountered = True
            # If there was any invalid character arrangement encountered, we would exit before moving to the next character.
            # Hence, if the character encountered was a digit, it will always be valid, and we will always entertain it.
            elif character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                # Use the digit character to update the output
                output = (output * 10) + int(character)
                # Now that we've encountered a digit, set that flag.
                digitEncountered = True
            # If a character other than space, digit or + / - sign characters is encountered before space, we would've already fallen in `else` part and exited.
            # Hence, if the character encountered was a white-space, we will only entertain it if we've not seen a sign or a digit before.
            # We are alright if we've seen white-spaces before.
            # This means those, including current character, were leading white-spaces.
            elif character == ' ' and (not signEncountered and not digitEncountered):
                continue
            # If we encounter a character that doesn't fulfil any of the above pattern, we need to stop conversion and return whatever output we've formed so far.
            else:
                return output
        # At last, if we had encountered a sign, depending on the sign flag, update the result before returning
        return output * (-1 if isNegative else 1)

    @staticmethod
    def regexMatching(inputString, pattern):
        """Problem:
        Given an input string s and a pattern p, implement regular expression matching with support for '.' And '*' where:
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
        Https://leetcode.com/problems/regular-expression-matching

        Brute Force Solution:
        Since one character from the pattern can match multiple characters from inputString, we will start by enumerating each character from the pattern.
        We will also have a pointer that will point to the current character to be matched on inputString.
        For each character that's not a special character, we will match the character from pattern to the inputString as it is.
        Whenever we encounter a '.' Character, we will match any character with it from inputString.
        Whenever we encounter a '*' character, we will remember what the previous character in the pattern was and use that logic to match character in inputString.
        Remember, when using a combination of, '.*', we might end up matching the whole string which is not what we want.
        Hence, we will also keep track of the next character in the pattern. If we encounter that character, we move on to it in the pattern abandoning matching effort for '.*'.
        Runtime: O(n) Space: O(1) --> where n is the length of inputString"""
        # Initialize pointers for the pattern and inputString for matching
        inputStringPointer, patternPointer = 0, 0
        # Keep looping till we run out of either the pattern or the inputString
        while patternPointer < len(pattern) and inputStringPointer < len(inputString):
            # Initialize current character from pattern, previous character from pattern and next character from the pattern for easy access.
            currentCharacter = pattern[patternPointer]
            nextCharacter = pattern[patternPointer + 1] if patternPointer + 1 < len(pattern) else None
            previousCharacter = pattern[patternPointer - 1] if patternPointer > 0 else None
            if currentCharacter == '*':
                # If we are on a '*' character, we see if the next character from pattern matches the current inputString character.
                # If so, we want to eliminate matching of '*' and move on.
                if nextCharacter == inputString[inputStringPointer]:
                    patternPointer += 1
                # If not, we want to match the previous character (the one prefixed to the `*` character) with the current inputString character
                else:
                    if previousCharacter != inputString[inputStringPointer] and previousCharacter != '.':
                        return False
                    # We only want to move forward with inputString since the current character '*' can match more characters from inputString.
                    inputStringPointer += 1
            # If we are not on a '*' character, special logic is essentially very limited.
            else:
                # We just say the pattern didn't match if either pattern's current character is not a '.' or if the pattern and inputString characters didn't match.
                if currentCharacter != inputString[inputStringPointer] and currentCharacter != '.':
                    return False
                # Otherwise, we say we found a match, and in this case the pattern characters won't be able to match more characters from inputString. So move forward in both pattern and inputString.
                inputStringPointer += 1
                patternPointer += 1
        # At the end, we want to ensure that the pattern matched the whole of the string. So if we reach the end of inputString at the end, return True otherwise return False.
        return inputStringPointer == len(inputString)

    @staticmethod
    def longestCommonPrefix(stringArray):
        """Problem:
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        https://leetcode.com/problems/longest-common-prefix

        Brute Force Solution:
        To find the longest common prefix to all the strings in array, we will have to go through each string from the array
        comparing the characters one by one and determining the longest common prefix based on if the characters match for all strings or not.
        Here, one way to put in a small optimization would be to realize that the longest common prefix possible is the shortest string in the array.
        Hence, we will find out the smallest string at the beginning.
        Go through each character on that string and ensure that this character appears in the same position for all other strings in the array too.
        If they do, we identify this character a part of common prefix for the array of strings, and we move on to the next character in the smallest string.
        If they don't, it means the common prefix ended at this character.
        Hence, the prefix we've found so far will be the longest common prefix.
        Hence, we return this prefix.
        If we reach the end of the shortest string while comparing, the whole shortest string is the common prefix for the array.
        Hence, we return the whole thing.
        Runtime: O(m*n) Space: O(1) --> where m is length of the smallest string in the array and n is total number of strings in the array"""
        # Initialize the longest common prefix empty.
        longestCommonPrefix = ""
        # If the stringArray is empty, the longest common prefix will stay empty.
        if not stringArray:
            return longestCommonPrefix
        # If there's only one string in stringArray, return that string since it's the prefix itself.
        if len(stringArray) == 1:
            return stringArray[0]
        # Find the shortest string among all strings in stringArray
        shortestString = min(stringArray, key=len)
        # Enumerate over all characters of the shortest string
        for idx, character in enumerate(shortestString):
            # Compare each character in the shortest string with the characters at the same index in all the strings in stringArray
            if all([character == currentString[idx] for currentString in stringArray]):
                # If all of them match, we add that character to the longest common prefix
                longestCommonPrefix += character
            else:
                # Whenever there's a mismatch, the common prefix cannot go on, so we break and stop comparing.
                break
        # Whatever we've found so far, is the longest the common prefix can be. So return that.
        return longestCommonPrefix


class StringUtilityTest(unittest.TestCase):
    def test_longestSubstringWithoutRepeatingCharactersFrom_happyCase(self):
        self.assertEqual(StringUtility.longestSubstringWithoutRepeatingCharactersFrom("abcabcbb"), 3)
        self.assertEqual(StringUtility.longestSubstringWithoutRepeatingCharactersFrom("bbbbb"), 1)
        self.assertEqual(StringUtility.longestSubstringWithoutRepeatingCharactersFrom("pwwkew"), 3)

    def test_longestSubstringWithoutRepeatingCharactersFrom_emptyInput(self):
        self.assertEqual(StringUtility.longestSubstringWithoutRepeatingCharactersFrom(""), 0)
        self.assertEqual(StringUtility.longestSubstringWithoutRepeatingCharactersFrom(None), None)

    def test_longestPalindromicSubstringIn_happyCase(self):
        self.assertEqual(StringUtility.longestPalindromicSubstringIn("abcba"), "abcba")
        self.assertIn(StringUtility.longestPalindromicSubstringIn("babad"), ["aba", "bab"])
        self.assertEqual(StringUtility.longestPalindromicSubstringIn("cbbd"), "bb")

    def test_longestPalindromicSubstringIn_emptyInput(self):
        self.assertEqual(StringUtility.longestPalindromicSubstringIn(""), "")
        self.assertEqual(StringUtility.longestPalindromicSubstringIn(None), None)

    def test_zigzagEncodingOf_emptyInput(self):
        self.assertEqual(StringUtility.zigzagEncodingOf("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(StringUtility.zigzagEncodingOf("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(StringUtility.zigzagEncodingOf("A", 1), "A")

    def test_stringToInteger_happyCase(self):
        self.assertEqual(StringUtility.stringToInteger("42"), 42)
        self.assertEqual(StringUtility.stringToInteger("   -42"), -42)
        self.assertEqual(StringUtility.stringToInteger("4193 with words"), 4193)

    def test_stringToInteger_noNumber(self):
        self.assertEqual(StringUtility.stringToInteger("a42"), 0)
        self.assertEqual(StringUtility.stringToInteger("   - -42"), 0)
        self.assertEqual(StringUtility.stringToInteger("0   -42"), 0)
        self.assertEqual(StringUtility.stringToInteger("   --42"), 0)
        self.assertEqual(StringUtility.stringToInteger("0 with words"), 0)
        self.assertEqual(StringUtility.stringToInteger("+     123"), 0)
        self.assertEqual(StringUtility.stringToInteger("+0 1 2 3"), 0)

    def test_regexMatching_happyCase(self):
        self.assertFalse(StringUtility.regexMatching("aa", "a"))
        self.assertTrue(StringUtility.regexMatching("aa", "a*"))
        self.assertTrue(StringUtility.regexMatching("ab", ".*"))
        self.assertTrue(StringUtility.regexMatching("This is a full sentense. Will contain many many letters, white-spaces and punctuations!", "This is a full sentense. Will contain many many letters, white-spaces and punctuations!"))

    def test_regexMatching_edgeCases(self):
        self.assertTrue(StringUtility.regexMatching("", ""))
        self.assertFalse(StringUtility.regexMatching("aa", "."))
        self.assertFalse(StringUtility.regexMatching("aa", "*"))
        self.assertTrue(StringUtility.regexMatching("This is a full sentense. Will contain many many letters, white-spaces and punctuations!", ".*"))

    def test_longestCommonPrefix(self):
        self.assertEqual(StringUtility.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(StringUtility.longestCommonPrefix(["flower", "flow", "flowering"]), "flow")
        self.assertEqual(StringUtility.longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(StringUtility.longestCommonPrefix([]), "")
        self.assertEqual(StringUtility.longestCommonPrefix(None), "")


if __name__ == "__main__":
    unittest.main()
