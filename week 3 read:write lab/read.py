from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A god CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    # TODO: Complete the function
    c = []
    with open(file,newline='') as a:
        b = csv.reader(a)
        for k,i in enumerate(b):
            if k == 0:
                if i != ['City','Team Name','Sport']:
                    raise ValueError
            if len(i) < 3:
                raise ValueError
            
            for g in i:
                if g.strip() == '':
                    raise ValueError
            c.append(tuple(i))
        #returns tuple of values, and then number of lines
    return (c[1:])


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of god files and god lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    k = open("error_log.txt", 'w')
    goodfiles = 0
    goodlines = 0
    listy = []

    a = list(Path(".").glob('*.csv'))
    for j in a:
        try:
            
        # reads each file
            club = readFile(j)
        except ValueError:
            k.write(str(j)+ '\n')
            continue
        #club has all tuples
        goodfiles+=1
        goodlines+=len(club)
        
        for i in club:
            
            clurb = SportClub(i[0],i[1],i[2])
            #make sure that it's unique
            if clurb in listy:
                for o in listy:
                    if o == clurb:
                        o.incrementCount()
            else:
                #add a new one
                listy.append(SportClub(i[0],i[1],i[2],1))

        
        
    d = open('report.txt', 'w')
    d.write('Number of files read: ' +str(goodfiles) + '\n')
    d.write('Number of lines read: ' + str(goodlines) + '\n')
    k.close()
    d.close()



    return listy

        

if __name__ == "__main__":
    for i in readAllFiles():
        print(i)
    
