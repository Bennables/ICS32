class MyCustomException():
    """ Some new exception"""

def someFunc():
    """ Some new func"""

def divide_numbers(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise MyCustomException

def multiply_numbers(num1,num2):
    return num1 * num2

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1,num2):
    return num1 - num2
    
def run_calculator(num1,num2,operator):
    if (operator == '/'):
        try:
            return divide_numbers(num1, num2)
        except MyCustomException:
            print("My custom exception")
        except Exception:
            print("Found it in run_calculator")
        finally:
            print("I am in the finally.")
    elif(operator == '*'):
        return multiply_numbers(num1, num2)
    elif(operator == '+'):
        return add_numbers(num1, num2) 
    elif(operator == '-'):
        return subtract_numbers(num1, num2)
    else:
        return("This is not a supported function")
    

run_calculator(10,0 , '/')