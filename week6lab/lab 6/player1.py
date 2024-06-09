import socket
from gameboard import BoardClass
import time
import signal
import tkinter as tk
from tkinter import ttk

def canvasSetup():
    master = tk.Tk()
    master.title('x')
    master.geometry('600x600')
    master.configure(background = 'grey')
    master.resizable(0,0)
    return master

def configGrid(master:tk.Tk):
    master.columnconfigure(0, weight = 1)
    master.columnconfigure(1, weight = 1)
    master.columnconfigure(2, weight = 1)
    master.rowconfigure(0, weight = 1)
    master.rowconfigure(1, weight = 1)
    master.rowconfigure(2, weight = 1)

def creategrid(master:tk.Tk, game, sockets):        #make sure no parents for command so it waits
    global waiting
    
    if waiting:
        for i in range(9):
            buttons[i] = tk.Button(master, text = '', command = None)
            buttons[i].grid(row = i//3, column = i%3,sticky='nsew')
        configGrid(master)
        updatePos(game.board)
        time.sleep(2)
        print("WAITING")
        p2_move = int(sockets.recv(1024).decode())
        print("REceived")
        game.updateGameBoard(p2_move, 'o')
        if game.isWinner():
            print("o WINS")
            game.addloss()
        if game.boardIsFull():
            print("NOBODY WINS")
            game.addtie()
        
        waiting = False
        creategrid(master, game, sockets)
        print(waiting)
    else:
        for i in range(9):
            buttons[i] = tk.Button(master, text = '',command = lambda x=i:submit(x, game, master, sockets))
            buttons[i].grid(row = i//3, column = i%3,sticky='nsew')

    configGrid(master)
    updatePos(game.board)
    

def updatePos(board):
    #loop thru it and change things, change to text box x and o
    for i in range(9):
        if board[i] == 'x':
            buttons[i].config(text='X')
        elif board[i] == 'o':
            buttons[i].config(text='O')

#def method to start ui
def startUI(master:tk.Tk):
    master.mainloop()

def submit(ind, game:BoardClass, master, sockets):
    if game.isValid(ind +1):
        game.updateGameBoard(ind +1 , 'x')
        updatePos(game.board)
        creategrid(master, game, sockets)
        time.sleep(2)
        print(game.board)
        global waiting
        waiting = True
        if game.isWinner():
            print("x WINS")
            game.addwin()
        if game.boardIsFull():
            print("NOBODY WINS")
            game.addtie()
        sockets.send(str(ind+1).encode())
        print("DONE")
        creategrid(master, game, sockets)
        


        

        # print(game.board)
        







"""

player 1 implementation according to specs in assignment


timeout code from https://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish
functions:
connect: gets connection info and tries to cnnect to p2
send_user: sends the username
getMove:gets the move, restries if invalid, sends the move to p2, plots it
run:gets move, sends, checks if game over, receives move, checks if game over,
receive: gets other player's move and plots it

"""
#

class timeout:
    '''time out class copied from stack overflow to solve connection 
    taking too long
    
    has seconds and error message to hold time and tell what happens when it takes too long'''
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)


#create a socket obj


#attempt connect to server

def connectgui(master:tk.Tk):
    #create the input boxes

    ipbox = tk.Entry (master, textvariable = '(ex. 127.0.0.1)')
    portbox = tk.Entry(master, textvariable='ex 9000')
    ipbox.pack()
    portbox.pack()
    submitbutton = tk.Button(master, text = 'submit', command = lambda: connect(master, ipbox.get(), portbox.get())).pack()
    startUI(master)
    
def connect(master, p2addy, p2host):
    master.destroy()
    sockets = None
    try_connect= 'y'
    while try_connect == 'y':
        try:
            sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            with timeout(seconds=3):
                sockets.connect((p2addy,int(p2host)))
                # sockets.connect(('127.0.0.1',8016))
            try_connect = ''
        except Exception as e:
            print(e)
            master1 = canvasSetup()
            try_connec = tk.Entry(master1, textvariable= 'a')
            try_connec.pack()
            submit = tk.Button(master1, command = lambda: tryagain(master1, try_connec.get().lower().strip())).pack()
            startUI(master1)
            sockets.close()

    return sockets

def tryagain(master, text):
    master.destroy()
    if text == 'y':
        master = canvasSetup()
        connectgui(master)

    elif text == 'n':
        exit(0)
    else:
        while text == 'y' or text != 'n':
            master = canvasSetup()
            try_connec = tk.Entry(master, textvariable= 'a')
            try_connec.pack()
            submit = tk.Button(master, command = lambda: tryagain(master, try_connec.get().lower().strip())).pack()
            startUI(master)
            if text == 'y':
                master = canvasSetup()
                connectgui(master)
            elif text == 'n':
                exit(0)




def sendUser(sockets:socket):
    '''asks for user and sends it to other person
        
        args: sockets

        senduser()
        [in termina]
        USERNAME (enter)
        
    no return
    no exceptions
    '''
    user = input('Username')
    sockets.send(user.encode())
    p2_user = sockets.recv(1024).decode()
    return user, p2_user
    #creates board with p1
    

def getMove(game: BoardClass, sockets:socket):
    '''gets move and prints updated board
    
        arg: game:boardclass, sockets:socket

        ex:
        getmove()
     s  [in termina]
        3
        
        returns nothing
        excepts for bad moves and asks for a new move
        '''
    #123
    #456
    #789
    print("FELS")
    game.creategrid()
    print("UAAYAYYA")
    while not game.gone:
        print("Waiting for a move")
    sockets.send(str(game.getMove()).encode())
    


def receive(game: BoardClass, sockets:socket):
    '''recieves other player move, updates and prints board0
    params: game:boardclass, sockets:socket

    ex:
    receive() 

    no returns
    no exceptions

    '''
    p2_move = int(sockets.recv(1024).decode())
    game.updateGameBoard(p2_move, 'o')
    game.updatePos()


def play_again(game, sockets):
    ''' asks if you wanna play again. 

    args: game:boardclass, sockets:socket

    returns if you wanna play again

    ex:
    go()
    [in terminal]
    y

    
    '''
    again = input('play again? (y/n)').strip()
    again = again.lower()
    while not (again == 'y' or again =='n'):
        again = input('play again? (y/n)').strip()
        again = again.lower()
    if again == 'n':
        sockets.send('Fun Times'.encode())
        return False
    if again == 'y':
        sockets.send('Play Again'.encode())
        game.resetGameBoard()
        return True
    
if __name__ == '__main__':
    global waiting
    waiting = False
    buttons = [0,0,0,0,0,0,0,0,0]
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   
    
    gui = canvasSetup()
    
    connectgui(gui)

    startUI(gui)
    user, p2_user = sendUser(sockets)
    game = BoardClass(user,p2_user, player = 'x')
    #creategrid(gui,game,sockets)
   
    game.printStats()
    sockets.close()

    
