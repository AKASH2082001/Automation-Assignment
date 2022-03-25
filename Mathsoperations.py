import unittest

def Addition(x,y,z):
    return x+y
    return x+y+z
    return x-y
    return x*y
    return x/y

class Mathsoperationsapp(unittest.TestCase):

    def test_case_Additionof2numbers(self):
        a= 10
        b= 10
        c = a+b
        self.assertEqual(a+b,c)

    def test_case_Additionof3number(self):
        a=10
        b=5
        c=5
        d= a+b+c
        self.assertEqual(a+b+c,d)

    def test_case_suboftwonumber(self):
        a=10
        b=5
        c=a-b
        self.assertEqual(a-b,c)

    def test_case_muloftwonumber(self):
        a=5
        b=2
        c=a*b
        self.assertEqual(a*b,c)

    def test_case_divoftwonumber(self):
        a=10
        b=5
        c=a/b
        self.assertEqual(a/b,c)

if __name__ == "__main__":
    unittest.main()