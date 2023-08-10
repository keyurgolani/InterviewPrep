class TestUtility:
    @staticmethod
    def stringRange(inputOne, inputTwo=None, inputThree=None):
        if inputTwo is None and inputThree is None and type(inputOne) == int:
            integerStart, integerEnd, step = 0, inputOne, 1
        elif type(inputOne) == int and type(inputTwo) == int and inputThree is None:
            integerStart, integerEnd, step = inputOne, inputTwo, 1
        elif type(inputOne) == int and type(inputTwo) == int and type(inputThree) is int:
            integerStart, integerEnd, step = inputOne, inputTwo, inputThree
        else:
            raise Exception("Invalid Input")
        return [str(idx) for idx in range(integerStart, integerEnd, step)]