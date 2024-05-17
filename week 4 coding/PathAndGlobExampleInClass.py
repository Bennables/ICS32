from pathlib import Path

def userGivenPath(userPath):
    p = Path(userPath)
    return p

def staticPath():
    p = Path('/Users/bensirivallop/Documents/ics32.py/Week 4')
    return p

def fileAndPaths(myReturnedPathObject):
    myFilePath = myReturnedPathObject/Path("StudentList.csv")

    print('\nDoes this path exist? ', myReturnedPathObject.exists())
    print('\nIs this path a directory? ', myFilePath.is_dir())

    if myFilePath.is_file() == True:
        myFile = myFilePath.open('r')
        print(myFile.readlines())


def checkMyPathObject(myReturnedPathObject):
    print('This is my user given path:\n', myReturnedPathObject)
    print('\nDoes this path exist? ', myReturnedPathObject.exists())

    print("\nIs this path a directory? ", myReturnedPathObject.is_dir())
    print("\nIs this path a file? ", myReturnedPathObject.is_file())

def myGlobAndPath(myReturnedPathObject):
    globbedPath = myReturnedPathObject.glob("*.csv")
    for files in globbedPath:
        print(files)

if __name__ == '__main__':
    print("This is my path object:\n", type(staticPath()))
    myReturnedPathObject = staticPath()

    checkMyPathObject(myReturnedPathObject)
    fileAndPaths(myReturnedPathObject)
    myGlobAndPath(myReturnedPathObject)
