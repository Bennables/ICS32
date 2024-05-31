import tkinter as tk
# import tkk names from tkinger
from tkinter import ttk



#create class for user interface
class Board():
    
    #class variable in class scope
    board = [0,0,0,0,0,0,0,0]
    button1 = 0
    button2 = 0
    button3 = 0
    button4 = 0
    button5 = 0
    button6 = 0
    button7 = 0
    button8 = 0
    button9 = 0
    X = 0
    O = 0

    def __init__(self) -> None:
        #redefine it

        #initiate class vars

        self.canvasSetup()
        self.creategrid()
        self.initTk()

        self.returnKeyBind()
        # self.createNumber1Entry()
        # self.createOperationComboBox()
        # self.createNumber2Entry()
        # self.createResultLabel()
        # self.createSubmitButton()
        # self.createQuitButton()
        self.updatePos()
        self.startUI()


    #method that initializes tk vars
    def initTk(self):
        self.X = tk.Text(self.master, font = 50)
        self.X.insert('insert',"X")
        self.O = tk.Text(self.master, font = 50)
        self.O.insert('insert',"O")
        


        #init tkinter

    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title("tictactoe")
        self.master.geometry('600x600')
        self.master.configure(background = 'grey')
        self.master.resizable(0,0)

    def creategrid(self):                                   #make sure no parents for command so it waits
        self.button1 = tk.Button(self.master, text = 'y',command = None)
        self.button2 = tk.Button(self.master, text = 'fds',command = None)
        self.button3 = tk.Button(self.master, text = 'hs',command = None)
        self.button4 = tk.Button(self.master, text = 'hds',command = None)
        self.button5 = tk.Button(self.master, text = 'hds',command = None)
        self.button6 = tk.Button(self.master, text = 'fds',command = None)
        self.button7 = tk.Button(self.master, text = 'hs',command = None)
        self.button8 = tk.Button(self.master, text = 's',command = None)
        self.button9 = tk.Button(self.master, text = 'ds',command = None)

        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 1)
        self.master.columnconfigure(2, weight = 1)
        self.master.rowconfigure(0, weight = 1)
        self.master.rowconfigure(1, weight = 1)
        self.master.rowconfigure(2, weight = 1)
        self.button1.grid(row = 0, column = 0,sticky='nsew')
        self.button2.grid(row = 0, column = 1,sticky='nsew')
        self.button3.grid(row = 0, column = 2,sticky='nsew')
        self.button4.grid(row = 1, column = 0,sticky='nsew')
        self.button5.grid(row = 1, column = 1,sticky='nsew')
        self.button6.grid(row = 1, column = 2,sticky='nsew')
        self.button7.grid(row = 2, column = 0,sticky='nsew')
        self.button8.grid(row = 2, column = 1,sticky='nsew')
        self.button9.grid(row = 2, column = 2,sticky='nsew')
    
    def updatePos(self):
        #loop thru it and change things, change to text box x and o
        for i in range(9):
        
            if self.board[i] == 'x':
                self.X.grid(row = i//3, column= i%3)

            if self.board[i] == 'o':
                self.O.grid(row = i//3, column= i%3)
                
            



    def updateBoard(self,board_arr):
        self.board = board_arr

    def createMoves(self):
        for i,j in enumerate(self.board):
            if i != 0:
                pass

    def createNumber1Entry(self):
        self.num1Entry = tk.Entry(self.master, textvariable=self.num1)
        self.num1Entry.pack()

    def createNumber2Entry(self):
        self.num2Entry = tk.Entry(self.master, textvariable=self.num2)
        self.num2Entry.pack()


    #make method that creates label for result
    def createResultLabel(self):
        self.result.set('')
        self.resultLabel = tk.Label(self.master, textvariable=self.result, width = 25).pack()

    #submit button
    def createSubmitButton(self):#                                              no parens = waits to run
        self.submitButton = tk.Button(self.master,text ="submit", command = self.calculateResult).pack()

    #calculate
    def calculateResult(self,event=None):
        self.myCalc.checkOpearation(self.operation.get(), self.num1.get(),self.num2.get())
        self.result.set(self.myCalc.getResult())

    #define a method that creates a combobox with operation values
    def createOperationComboBox(self):
        operationValues = ['+','-','*','/']
        self.operation.set("please select an optoin")
        self.opComboBox = ttk.Combobox(self.master,textvariable=self.operation,values =operationValues).pack()

    def returnKeyBind(self):
        self.master.bind('<Return>',self.calculateResult)
        
    
    #def method to start ui
    def startUI(self):
        self.master.mainloop()

    





#if for testing
if __name__ == '__main__':
    basicCalc = Board()
    #confirm i have access to mombers of calculator object created


    

        
