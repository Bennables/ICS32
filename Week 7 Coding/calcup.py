import Calculatorclass as csgg
import tkinter as tk
# import tkk names from tkinger
from tkinter import ttk



#create class for user interface
class CalcUIPacker():
    #class variable in class scope
    myCalc = 0
    master= 0
    num1 = 0
    num2 = 0
    operation = 0
    result = 0

    def __init__(self) -> None:
        #redefine it
        self.myCalc = csgg.Calculator()

        #initiate class vars

        self.canvasSetup()
       
        self.initTk()
        self.returnKeyBind()
        self.createNumber1Entry()
        self.createOperationComboBox()
        self.createNumber2Entry()
        self.createResultLabel()
        self.createSubmitButton()
        self.createQuitButton()
        self.startUI()


    #method that initializes tk vars
    def initTk(self):
        self.num1 = tk.IntVar()
        self.num2 = tk.IntVar()
        self.operation = tk.StringVar()
        self.result = tk.IntVar()
        



        #init tkinter

    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title("BASIC CALC")
        self.master.geometry('400x400')
        self.master.configure(background = 'blue')
        self.master.resizable(0,0)

    def createQuitButton(self):
        self.quitButton = tk.Button(self.master, text= 'Quit',command = self.master.destroy).pack()

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
    basicCalc = CalcUIPacker()
    #confirm i have access to mombers of calculator object created
    print(basicCalc.myCalc.getResult())


    

        
