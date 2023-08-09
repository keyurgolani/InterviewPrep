import unittest

class RomanNumberUtility:

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
    
    """Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    
    Given an integer, convert it to a roman numeral.
    https://leetcode.com/problems/integer-to-roman"""
    @staticmethod
    def integerToRoman(integerNumber):
        """Brute Force:
        Numbers in roman are represented with above described logic.
        Hence, to identify roman representation for an input integer number, we can create a mapping of what integer number has a readily available roman value representing it.
        For all the other values, we will use a combination of lesser value roman representations to represent it.
        Here, since our map is of constant, limited size, we iterate over the map and identify if input integer number will use given mapped roman representation for it.
        Since the roman representation will have number representations in order of largest to smallest, we can simply start from largest value and keep appending the representations that we use to an answer.
        When we identify that one roman number representation will be used in the answer, we reduce the value of input integer number by that much and keep looking.
        At the end, when input integer number is 0, that means we've converted the whole number to roman representation and we return the answer."""
        # Start with an empty answer. Equivelant to 0 integer number.
        answer = ""
        # If integer number is not present, empty answer is good enough.
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
        # After last iteration, we would've made sure that integer number is less than 1 (last value that can directly be represented in roman).
        # Meaning it will be 0. Hence, return the answer.
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


if __name__ == "__main__":
    unittest.main()