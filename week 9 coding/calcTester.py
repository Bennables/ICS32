#import the unit test library
import unittest

#input the calculator class
import calcclass as cc

#class that will include our test cases and inherit the unit test test case
#functionality from the unittest library
class calcTester(unittest.TestCase):
    testCaseNumber = 1
    myCalc = cc.Calculator()

    #providing code to setup test cases\
    def setUp(self):
        print("Starting test case", str(self.testCaseNumber)+ '.')

    #providing code to wrap up a test case
    def tearDown(self) -> None:
        print("completed executing test case", str(self.testCaseNumber), '.\n')
        calcTester.testCaseNumber = calcTester.testCaseNumber

    
    #TEST_ required

    def test_OnePlusOne(self):
        self.myCalc.addNumbers(1,1)
        self.assertEqual(self.myCalc.getResult(), 2)
        print("I am in test case ", calcTester.testCaseNumber)
        self.assertEqual(self.myCalc.getResult(),1)

    def test_DivideByZero(self):
        with self.assertRaises(cc.DivideByZeroError):
            self.myCalc.divNumbers(1,0)


if __name__ == '__main__':
    #run the tests
    unittest.main()