#creating a class for a simple/basic calculator
class Calculator:
    #define class variable
    __calcResult__ = 0

    #definte constructor for calculator class
    def __init__(self):
        #initialize class vars as part of constructor
        self.__calcResult__ = 0

    #def getter for result
    def getResult(self):
        return self.__calcResult__
    
    #define setting/mutator method for setting the result value
    def setResult(self, result):
        self.__calcResult__ = result
    
    #define function that performs addition
    def addNumbers(self,num1, num2):
        self.setResult(num1 + num2)
    
    def subNumbers(self,num1,num2):
        self.setResult(num1-num2)

    #define the moethod that performs the multiplication
    def multNumber(self,num1,num2):
        self.setResult(num1*num2)

    def divNumbers(self,num1,num2):
        self.setResult(num1/num2)

    #define the method taht performs the correct operation
    def checkOpearation(self,opearation,num1,num2):
        if(opearation == '+'):
            self.addNumbers(num1,num2)
        elif opearation == '-':
            self.subNumbers(num1,num2)
        elif opearation == '*':
            self.multNumber(num1,num2)
        else:
            self.divNumbers(num1,num2)

if __name__ == '__main__':
    testCalc = Calculator()
    print(testCalc.getResult())
    testCalc.checkOpearation('+',5,4)
    print(testCalc.getResult())
    testCalc.checkOpearation('-',5,4)
    print(testCalc.getResult())
    testCalc.checkOpearation('*',5,4)
    print(testCalc.getResult())
    testCalc.checkOpearation('',5,4)
    print(testCalc.getResult())
