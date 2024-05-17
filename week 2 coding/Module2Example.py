#this returns function name
def randomFunctionModule2():
    return "randomFunctionModule2 in Module 2"

#This returns function name
def randomFunction2():
    return "randomFunction2 in Module 2"

#This prints the name of the module
def printMyModuleName():
    return __name__

#print ("Stray code in module 2.")

#Checking if this module is main
if __name__ == '__main__':
    print("My random print statment.")
    print("Module 2:", printMyModuleName())