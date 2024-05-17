#This returns function name
def randomFunction1():
    return "randomFunction1 in Module 3"

#This returns function name
def randomFunction2():
    return "randomFunction2 Module 3"

#This prints the name of the module
def printMyModuleName():
    return __name__

#Checking if this module is main
if __name__ == '__main__':
    print("Module 3:", printMyModuleName())