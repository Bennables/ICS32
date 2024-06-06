import socket
import tkinter as tk
# import tkk names from tkinger
from tkinter import ttk

class BoardClass:
    '''Class to keep track of the game and board.

    Attributes:
        The player's user name
        User name of the last player to have a turn
        Number of wins the user has
        Number of ties the user has
        Number of losses the user has
        board of game
        count of games played
    '''
    game_count = 0


    def __init__(self,  username: str = "", lastUser: str= "", wins: int = 0, ties: int = 0, losses: int = 0, player:str = 'x') -> None:
        '''Making a gameboard.
        
        Args:
            username: The user's name
            lastUser: The last player to make a move
            wins: The amount of wins
            losses: The amount of losses
            ties: The amount of ties
        '''
        self.setUsername(username)
        self.setLastUser(lastUser)
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.board = [0,0,0,0,0,0,0,0,0]
        self.game_count = 0
        self.buttons = [0,0,0,0,0,0,0,0,0]
        self.turn = 'x'
        self.player = player

        #TKINRER
        self.canvasSetup()
        self.creategrid()
        self.updatePos()
        self.startUI()

    def setUsername(self, username: str) -> None:
        '''Retrieving the user's name into the database.

        Args:
            username: Username of the player
        '''
        self.username = username
    
    def setLastUser(self, lastUser: str) -> None:
        '''Updating/initializing the last user to make a move.

        Args:
            lastUser: Username of the player who made the last move
        '''
        self.lastUser = lastUser
    
    def addwin(self):
        '''increases wins by 1
        no args'''
        self.wins +=1

    def addloss(self):
        '''increases losses by 1
        no args'''
        self.losses +=1
    def addtie(self):
        '''increases ties by 1
        no args'''
        self.ties +=1
    
    def getUsername(self) -> str:
        """Get the name of the user.

        Returns:
            The username of the player
        """
        return self.username
    
    def getLastUser(self) -> str:
        """Get the name of the last user.

        Returns:
            The username of the last player
        """
        return self.lastUser
    
    def getWins(self) -> str:
        """Get the win count of the user.

        Returns:
            The wins of the player
        """
        return self.wins
    
    def getTies(self) -> str:
        """Get the tie count of the user.

        Returns:
            The ties of the player
        """
        return self.ties
    
    def getLosses(self) -> str:
        """Get the loss count of the user.

        Returns:
            The losses of the player
        """
        return self.losses
    

    '''Keeps track how many games have started'''
    def updateGamesPlayed(self) -> None:
        self.game_count +=1
    
    '''Clear all the moves from game board'''
    def resetGameBoard(self) -> None:
        self.board = [0,0,0,0,0,0,0,0,0]

    '''Updates the game board with the player's move'''
    def updateGameBoard(self, num, letter) -> None:
        self.board[num-1] = letter

    '''Checks if the latest move resulted in a win and updates the wins and losses count'''
    def isWinner(self) -> bool:
        '''checks for the wins
        no args'''
        for i in range(3):
            #this one loops thru rows
            if self.board [i*3+ 0] == self.board[i*3 +1] == self.board[i*3 +2] and self.board[i*3+2] != 0:
                return True
            #this loops through columns
            if self.board [0+i] == self.board[3+i] == self.board[6+i] and self.board [6+i]!= 0:
                return True
        if self.board [2] == self.board[4] == self.board[6] and self.board [6]!=0:
            return True
        if self.board [0] == self.board[4] == self.board[8] and self.board[0] != 0:
            return True
        return False
    
    def isValid(self, num):
        '''chekcs if a move is valid returns if it is
        arg is a number'''
        try:
            num = int(num)
            if 1<=num<=9:
                if self.board[num-1] ==0:
                    return True
            return False
        except:
            return False

    def printBoard(self):
        '''prints the board'''
        for i in range(3):
            for j in range(3):
                if self.board[i * 3 + j] == 0:
                    print('_', end = ' ')
                else:
                    print(self.board[i * 3 + j], end = ' ')
            print()

    '''Checks if the board is full (I.e. no more moves to make - tie) and updates the ties count'''
    def boardIsFull(self) -> bool:
        for i in range(9):
            if self.board[i] == 0:
                return False
        return True


    '''Prints usernames, last user to make a move, number of games, wins, losses, ties'''
    def printStats(self) -> None:
        print('USER: ' + self.username)
        print('LastUser: ' + self.lastUser)
        print('games played: '+ str(self.game_count))
        print("wins: " + str(self.wins))
        print('losses: ' + str(self.losses))
        print('ties: '+ str(self.ties))


    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title("tictactoe")
        self.master.geometry('600x600')
        self.master.configure(background = 'grey')
        self.master.resizable(0,0)

    def configGrid(self):
        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 1)
        self.master.columnconfigure(2, weight = 1)
        self.master.rowconfigure(0, weight = 1)
        self.master.rowconfigure(1, weight = 1)
        self.master.rowconfigure(2, weight = 1)
    
    def creategrid(self):                                   #make sure no parents for command so it waits
        self.gone = False
        for i in range(9):
            self.buttons[i] = tk.Button(self.master, text = '',command = lambda x=i:self.submit(x))
            
            self.buttons[i].grid(row = i//3, column = i%3,sticky='nsew')

        self.configGrid()
        self.updatePos()
        
        

    def disableGrid(self):
        for i in range(9):
            self.buttons[i] = tk.Button(self.master, text = '')
            self.buttons[i].grid(row = i//3, column = i%3,sticky='nsew')

        self.configGrid()
        self.updatePos()

    def updatePos(self):
        #loop thru it and change things, change to text box x and o
        for i in range(9):
            if self.board[i] == 'x':
                self.buttons[i].config(text='X')
            elif self.board[i] == 'o':
                self.buttons[i].config(text='O')

    #def method to start ui
    def startUI(self):
        self.master.mainloop()
    def switchUser(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

    def submit(self,ind):
        self.gone = False
        if self.turn == self.player:
            if self.board[ind] == 0:
                self.board[ind] = self.player
                self.gone = True
        self.updatePos()
        self.switchUser()
        return ind + 1
    


#if for testing
if __name__ == '__main__':
    basicCalc = BoardClass()
    #confirm i have access to mombers of calculator object created


    

        
