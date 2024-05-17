''' You are expected to comment your code. At a minimum if statements and for loops
 need at least 1 line of comment to explain what the loop does'''

#------------IMPORT ANY LIBRARIES YOU NEED HERE-----------
from pathlib import Path
#---------- CREATE YOUR CUSTOM EXCEPTION HERE-------------
class NotAValidDirectory(Exception):
    '''You will raise a custom exception called "NotAValidDirectory"
if the directory provided is not a directory.
'''
    pass
class NoFilesFoundInDirectory(Exception):
    '''You will raise a custom
exception called "NoFilesFoundInDirectory" if the directly is empty
and contains no files.'''
    pass



'''Write a function called combineFiles that reads all the text
files (.txt extension) which takes the relative directory/path and the name of the combined file
it will create as input parameters (function arguements) 


all the text files located in the directory and writes
it to a new combined file created in the current directory. done

 It returns the values
defined below. You will raise a custom exception called "NotAValidDirectory"
if the directory provided is not a directory. 


You will raise a custom
exception called "NoFilesFoundInDirectory" if the directly is empty
and contains no files. The function will return 3 variables.
(Ensure they are in the same order)
I am specifying:
  - A variable that returns the total number of files in the directory provided
  - A variable that provides the number of text files found in the directory
  - A variable that provides the total number of lines in the final combined file
'''
#----------------YOUR FUNCTION CODE STARTS HERE--------------- 

def combineFiles(path, combined_name):
    
    # this creates the path
    path = Path(path)
    #checks if it's a directory, if not, raise the error
    if path.is_dir():
        pass
    else:
        raise NotAValidDirectory

    #checks that the directory isn't empty. It will raise the error otherwise
    amt_files = len(list(Path(path).glob('*')))
    if amt_files == 0:
        raise NoFilesFoundInDirectory
    

    #checks for txt files in the directory
    a = list(Path(path).glob('*.txt'))

    #vars for amt of text files and amt of lines in those text files
    amt_text = len(a)
    tot_lines = 0


    #open the output file
    with open(combined_name, 'w') as file:
        #goes through each text file path in the list of text files
        for i in a:
            opened = open(i,'r', newline = '')
            #goes through each line in each text file
            for j in opened:
                #adds it to output
                file.write(j.strip() + '\n')
        


    #opens the file to read total lines
    with open(combined_name, 'r') as j:
        tot_lines = len(j.readlines())

    #return values
    return(amt_files, amt_text, tot_lines)
        







      
#------------------- YOUR FUNCTION CODE ENDS HERE------------------   

'''This will run your program. You should only add code to
handle exceptions that are raised. Any exceptions found will only
display "Exception Found" and end program execution. The program will
only run once.(Does not automatically restart)'''
#--------- ADD CODE HERE THAT HANDLES RUNNING THE PROGRAM AND EXEPTIONS AS DESCRIBED ABOVE-------

#if the file is main? the one you're running from
if  __name__ == "__main__":
    #try and exceptionhandling as per specifications
    try:
        combineFiles('text', 'i.txt')
    except:
        print("Exception Found")

    # print(combineFiles('text', 'i.txt'))