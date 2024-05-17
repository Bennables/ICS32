import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    # TODO: Complete the function
    sport_separated = []
    #starts iteration
    sports = []

    for i in all_clubs:
        #to see if slot found
        found = False
        #checks if each one works
        for b, j in enumerate(sports):
            if i.getSport() == j:
                sport_separated[b].append(i)
                found = True
        #if not found, then make a new one
        if not found:
            sports.append(i.getSport())
            sport_separated.append([i])

    return sport_separated # erase this


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """

    g = sorted(sport, reverse = True)
    
  

    return g


    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    return []  # erase this


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function
    with open("survey_database.csv", "w") as f:
        f.write("City,Team Name,Sport,Count\n")
        for i in sorted_sports:
            for j in i:
                f.write(f'{j.getCity()},{j.getName()},{j.getSport()},{j.getCount()}\n')


if __name__ == "__main__":
    d = [SportClub('a', 'bf','b',5),SportClub('a', 'bfd','b',2343),SportClub('a', 'cf','b',3420),SportClub('a', 'ce','b',2342),SportClub('a', 'b','b',23),SportClub('a', 'g','b',23),SportClub('a', 'cd','b',403)]
    for i in sortSport(d):
        print(i.getName(), i.getCount())