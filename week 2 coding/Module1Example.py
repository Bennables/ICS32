#IMport hte entire module2exampe into module1example
import Module2Example as m2
from Module3Example import randomFunction1, randomFunction2

#This prints the name of the module
def printMyModuleName():
    return __name__

#This returns function name
def randomFunction2():
    return "randomFunction2 in Module 1"

#Using a function from the import Module2Example
def usingModule2():
    return m2.randomFunctionModule2()

#using a fucntion from the import Module3 Example
def usingModule3():
    randomFunction1()
    return ModuleNotFoundErro. randomFunction2()

#checking if this module is main
if __name__ == '__main__':
    print("Module1:", printMyModuleName())
    print(usingModule2())
    print(usingModule3())
    #print(Module2Example.printMyModuleName)