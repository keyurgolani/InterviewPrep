import unittest


class RomanNumberUtility:
    """Contains methods that operate on roman numbers."""

    # Lookup to help find directly corresponding integer value from roman representation
    romanToIntegerLookup = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    # Lookup to help find directly corresponding roman representation from an integer value
    integerToRomanLookup = dict([(value, key) for key, value in romanToIntegerLookup.items()])

    @staticmethod
    def integerToRoman(integerNumber):
        """Problem:
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two ones added together.
        12 is written as XII, which is simply X + II.
        The number 27 is written as XXVII, which is XX + V + II.
        Roman numerals are usually written largest to smallest from left to right.
        However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
        The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.

        Given an integer, convert it to a roman numeral.
        Https://leetcode.com/problems/integer-to-roman

        Brute Force Solution:
        Numbers in roman are represented with above-described logic.
        Hence, to identify roman representation for an input integer number, we can create a mapping of what integer number has a readily available roman value representing it.
        For all the other values, we will use a combination of lesser value roman representations to represent it.
        Here, since our map is of constant, limited size, we iterate over the map and identify if input integer number will use given mapped roman representation for it.
        Since the roman representation will have number representations in order of largest to smallest, we can simply start from the largest value and keep appending the representations that we use to an answer.
        When we identify that one roman number representation will be used in the answer, we reduce the value of input integer number by that much and keep looking.
        In the end, when input integer number is 0, that means we've converted the whole number to roman representation, and we return the answer.
        Runtime: O(n) Space: O(1) --> This is because all inputs lesser than 1000 will be converted in constant time.
        But for all values above 1000, we will do linearly one more iteration per 1000 value increase.
        Which is still linear."""
        # Start with an empty answer. Equivalent to the integer number zero.
        answer = ""
        # If the integer number is not present, empty answer is good enough.
        if not integerNumber:
            return answer
        # Iterate over all possible direct roman representations of integer numbers in decreasing order.
        for symbol, value in sorted(RomanNumberUtility.romanToIntegerLookup.items(), key=lambda item: item[1], reverse=True):
            # Until the input number is larger than the value that can be represented directly in roman, 
            while integerNumber >= value:
                # keep appending that representation to answer
                answer = answer + symbol
                # Keep decreasing the integer number by the value that was already added to answer in roman representation
                integerNumber -= value
        # After the last iteration, we would've made sure that integer number is less than 1 (last value that can directly be represented in roman).
        # Meaning it will be 0. Hence, return the answer.
        return answer

    @staticmethod
    def romanToInteger(romanRepresentationNumber):
        """Problem:
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        For example, 2 is written as II in the Roman numeral, just two ones added together.
        12 is written as XII, which is simply X + II.
        The number 27 is written as XXVII, which is XX + V + II.
        Roman numerals are usually written largest to smallest from left to right.
        However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
        The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.

        Given a roman numeral, convert it to an integer.
        Https://leetcode.com/problems/roman-to-integer

        Brute Force Solution:
        Since we have converted integer to roman now, we know that at the beginning, we will always see grater value representations in roman number.
        The simplest way would be to iterate through the mapping again and expect the values from largest to smallest.
        Whenever we find our expectations met, we add corresponding direct integer value to the answer.
        In the end, after iterating through the whole string, we return the answer.
        Runtime: O(n) Space: O(1)"""
        # Start with the answer zero.
        answer = 0
        # If input is empty, the answer zero is good enough. Return it.
        if not romanRepresentationNumber:
            return answer
        # Iterate over all possible direct roman representations of integer numbers in decreasing order.
        for symbol, value in sorted(RomanNumberUtility.romanToIntegerLookup.items(), key=lambda item: item[1], reverse=True):
            # While the symbol we are evaluating, appears at the beginning of the roman representation,
            while romanRepresentationNumber.startswith(symbol):
                # Add its directly corresponding number value to the answer
                answer += value
                # Remove the first occurrence of given roman symbol from the whole number's representation.
                romanRepresentationNumber = romanRepresentationNumber.replace(symbol, '', 1)
        # At the end, we will go over the smallest value in the map, 1.
        # Hence, in the end, roman string should be empty. Return answer.
        # Note: We could probably add a validation if the roman string became empty at this point. If we were to add roman string validations at other places too, this would be one place that would help.
        return answer


class RomanNumberUtilityTest(unittest.TestCase):
    def test_integerToRoman_happyCase(self):
        self.assertEqual(RomanNumberUtility.integerToRoman(2), "II")
        self.assertEqual(RomanNumberUtility.integerToRoman(12), "XII")
        self.assertEqual(RomanNumberUtility.integerToRoman(27), "XXVII")
        self.assertEqual(RomanNumberUtility.integerToRoman(3), "III")
        self.assertEqual(RomanNumberUtility.integerToRoman(58), "LVIII")
        self.assertEqual(RomanNumberUtility.integerToRoman(1994), "MCMXCIV")

    def test_integerToRoman_zeroValue(self):
        self.assertEqual(RomanNumberUtility.integerToRoman(0), "")
        self.assertEqual(RomanNumberUtility.integerToRoman(None), "")

    def test_romanToInteger_happyCase(self):
        self.assertEqual(RomanNumberUtility.romanToInteger("II"), 2)
        self.assertEqual(RomanNumberUtility.romanToInteger("XII"), 12)
        self.assertEqual(RomanNumberUtility.romanToInteger("XXVII"), 27)
        self.assertEqual(RomanNumberUtility.romanToInteger("III"), 3)
        self.assertEqual(RomanNumberUtility.romanToInteger("LVIII"), 58)
        self.assertEqual(RomanNumberUtility.romanToInteger("MCMXCIV"), 1994)

    def test_romanToInteger_zeroValue(self):
        self.assertEqual(RomanNumberUtility.romanToInteger(""), 0)
        self.assertEqual(RomanNumberUtility.romanToInteger(None), 0)


if __name__ == "__main__":
    unittest.main()
