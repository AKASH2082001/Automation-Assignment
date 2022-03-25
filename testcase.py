import unittest

def EvenorOdd(x):
    if x%2 == 0:
        return "even"
    else:
        return "odd"

def Divisibleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False

def PrimeorNot(x):
    if x > 1:
        for i in range(2, int(x / 2) + 1):
            if (x % i) == 0:
                break
        else:
            return True
    else:
        return False

class testcasesapp(unittest.TestCase):

    def test_case_evenorodd(self):
        result = EvenorOdd(2)
        self.assertEqual("even", result)

    def test_case_evenorodd1(self):
        result = EvenorOdd(15)
        self.assertNotEqual("odd", result)

    def test_case_divisibleby7_1(self):
        result = Divisibleby7(14)
        self.assertTrue(result)

    def test_case_divisibleby7_2(self):
        result = Divisibleby7(4)
        self.assertFalse(result)

    def test_case_primeorNot(self):
        result = PrimeorNot(2)
        self.assertTrue(result)

    def test_case_primeorNot2(self):
        result = PrimeorNot(1)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()