#Defining a module level variable
#someString = "Module String"
global someGlobalString
someGlobalString = "Global String"
#someString = 10

#Creating a function to demonstrate funciton scope (encapsulated)
def someFunction():
    #someString = "Function String"
    someFunctionString = "LocalString"
    global someGlobalString
    someGlobalString = "New value from inside my function."
    #print("Printing inside of someFunction:", someFunctionString)
    print("Printing inside of someFunction: ", someString)
    #print("Printing my not so global string:", someGlobalString)

print("Printing outside of functoins: ", someString)
print("Printing global string before my function: ", someGlobalString)
someFunction()
print("Printing global string after my function: ", someGlobalString)
#print("Printing outside of fucntions: ", someString)
#print("Printing outside of someFunction:", someFunctionString)
