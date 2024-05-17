"""
Name:
UCINetID:
"""

class IntegerOutOfRangeException(Exception):
    pass

class NoStaircaseSizeException(Exception):
    pass

''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function. This function will
raise any exceptions related to none integer user inputs.'''
def getUserInput():
    #your code belongs here
    a = input('Please input your staircase size:')
    if a == "DONE":
        return "DONE"
    a = int(a)
    return a
        
    


''' This function takes the number of steps as an input parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function. This function will raise
any exceptions resulting from invalid integer values.
'''
def createSteps(stepCount):
    #your code belongs here
    a = stepCount
    if a < 0 or a > 999:
        raise IntegerOutOfRangeException
    elif a == 0:
        raise NoStaircaseSizeException
    
    
    
    #stair shit
    b = '+-+'
    c = '| |'
    da_string = ''
    da_string += ' ' * 2 * (a-1)
    da_string += b + '\n'
    da_string += ' ' * 2 * (a-1)
    da_string += c + '\n'

    for i in range((a - 2) * 2, -1, -2):
        da_string += ' ' * i
        da_string += '+-+-+\n'
        da_string += ' ' * i
        da_string += '| |\n'
    da_string += '+-+'


    return da_string


'''This function kicks off the running of your program. Once it starts
it will continuously run your program until the user explicitly chooses to
end the running of the program based on the requirements. This function returns
the string "Done Executing" when it ends. Additionally, all exceptions will be
handled (caught) within this function.'''

def runProgram():
    #your code belongs here
    a = 0
    while True:
        try:
            a = getUserInput()
            while a != "DONE":
                if (not a == None):
                    stre = createSteps(a)
                    if createSteps(a) != None:
                        print(stre)

                a = getUserInput()

            return "DONE"
        except ValueError:
            print("Invalid staircase value entered.")
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
        except NoStaircaseSizeException:
            print("I cannot draw a staircase with no steps.")
        if a == "Done":
            break

#'Done', 'DoNe', 'DONe', 'DoNE', 'dONE', 0, 5, 0, 0, 150, 0, 0, 0, 'DONE'

    
'''Within this condition statement you are to write the code that kicks off
your program. When testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__": 
    #your code belongs here
    runProgram()



'''

??? 7. Perform a function call within the exception handling logic (Your function that contains the code to run the program should be within a try/except block - see comments in the starter code).

getUserInput()

Should read input from the user via the built-in Python input function with the prompt "Please input your staircase size:"
Should return the value from the function as an int (if possible) or as the string DONE
Should raise a ValueError for any non-numeric input (other than the word DONE)
createSteps(stepCount)

Should take the number of steps, passed in as stepCount, as an int input parameter
Should create a string containing the staircase based on the input stepCount and return that string as the result of the function
Should raise a custom exception called IntegerOutOfRangeException when the user provides an integer value that is not within the valid integer range of 1 <= stepCount < 1000.
Should raise a custom exception called NoStaircaseSizeException when the user provides an integer value of 0 for the number of steps.
NOTE: it is confusing, but realize that although the function is named createSteps, you should not need any print statements inside this function
runProgram()

Should run continuously in a loop that gets user input, creates a staircase, prints it to the console, repeat
Should print the staircase returned by createSteps to the console
Should terminate by calling return with the value "Done Executing" when the user enters the word DONE (case-sensitive) instead of a number for the steps
Should catch the ValueError raised by getUserInput and print the error string "Invalid staircase value entered." and then continue looping
Should catch the IntegerOutOfRangeException raised by createSteps and print the error string "That staircase size is out of range." and then continue looping
Should catch the NoStaircaseSizeException raised by createSteps and print the error string "I cannot draw a staircase with no steps." and then continue looping
Should not terminate the program when ValueError, IntegerOutOfRangeException or NoStaircaseSizeException are raised.
if __name__ == '__main__':

As described in class, this section of code is not used by the autograder.  You are free to put whatever test code you want here.  Generally it makes sense to just call runProgram() here to test your code.
Other

You will need to define custom exceptions for this assignment.  They should be defined at the "top-level" in the module (i.e. not inside a function) so that their scope is visible to all functions.  A custom exception can be defined as follows:
class MyCustomException(Exception):

    pass

This is using inheritance which is a concept we'll cover in later lectures.

Sample Output of Valid Values:
'''