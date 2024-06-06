import tkinter as tk
# import tkk names from tkinger
from tkinter import ttk
import gameboard as gb


#create class for user interface
class Board():
    
    board = [0,0,0,0,0,0,0,0,0]
    turn = 'x'
    #class variable in class scope
    buttons = [0,0,0,0,0,0,0,0,0]
    player = 0
    gone = False
    def __init__(self, player = 'x') -> None:
        #redefine it
        #initiate class vars

        self.canvasSetup()
        #init tkinter
        self.creategrid()
        

        # self.createNumber1Entry()
        # self.createOperationComboBox()
        # self.createNumber2Entry()
        # self.createResultLabel()
        # self.createSubmitButton()
        # self.createQuitButton()
        self.updatePos()
        self.startUI()


    #method that initializes tk vars

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
    basicCalc = Board()
    #confirm i have access to mombers of calculator object created


    

        
