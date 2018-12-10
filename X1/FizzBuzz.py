class FizzBuzz:

    def __init__(self):
        self._MaxRange = 100

    @property
    def MaxRange(self):
        return self._MaxRange

    def FizzBuzz(self):
        print("Welcome To Fizzbuzz!  the program will enter 'Fizz' for multiples of 3, and 'Buzz' for multiples of 5")
        self._MaxRange = int(input("What is the Max of the range?"))

    def printfizzbuzz(self):
        print("Here is Fizz(3) Buzz(5):")
        for val in range(self._MaxRange):
            toprint = ""
            if (val % 3 == 0) & (val % 5 == 0):
                toprint += "FizzBuzz"
            elif val % 3 == 0:
                toprint += "Fizz"
            elif val % 5 == 0:
                toprint += "Buzz"
            else:
                toprint += str(val)
            print(toprint)