"""
Name:Ben Sirivallop
UCINetID:bsirival
"""

''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function'''

def getUserInput():
    
    #your code belongs here
    a = input('How many steps do you want to move?\n')
    return a
    

''' This function takes the number of steps as an unput parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function
'''
def createSteps(a):

    try:
        a = int(a)
        if a < 0:
            raise ValueError
    except:
        return 'You have provided an invalid staircase size.'
    
    if a == 0:
        return 'Your staircase has no steps to build.'
    elif a >= 1000:
        return 'The staircase is too tall to build.'
    else:
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


    
    #your code belongs here

'''Within this condition statement you are to write the code that
calls the above functions when testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__": 
    #your code belongs here
    a = getUserInput()
    print(createSteps(a))
    