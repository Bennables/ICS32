#creat file obj
#default is read

myPath = '/Users/bensirivallop/Documents/ics32.py/Week 3/coidng/'

# read only
# inputFileObj = open("SampleInputFile.txt", 'r')

#read and write
# inputFileObj = open("SamleInputFile.txt", 'r+')
#write, deletes all contents
# open can't create directories, 
inputFileObj = open(myPath + "files/SampleInputFile.txt", 'w')
#append
# inputFileObj = open("SampleInputFile.txt", 'a')

'''
#read a line
fileContent = inputFileObj.readline()
print("First Line: ", fileContent)  
fileContent = inputFileObj.readline()
print("Second Line: ", fileContent)
fileContent = inputFileObj.readline()
print("Third Line: ", fileContent)
fileContent = inputFileObj.readline()
print("Fourth Line: ", fileContent)
'''

inputFileObj.write("I am now writing to mefile.\n")

# #write a loop to go thru ile
# for nextLine in inputFileObj:
#     print(nextLine, end = '')

# inputFileObj.close()


#with to make sure it's closed

with open("AnotherFileWith.txt", 'w+') as anotherFileObj:
    anotherFileObj.write("This is the first line in my new file.\n")
    anotherFileObj.write("This is the first line in my new file.\n")
