
import socket
from gameboard import BoardClass
import time
import signal
import tkinter as tk
from tkinter import ttk

def canvasSetup():
    master = tk.Tk()
    master.title('o')
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

def creategrid(master:tk.Tk, game, sockets):                             #make sure no parents for command so it waits
    for i in range(9):
        buttons[i] = tk.Button(master, text = '',command = lambda x=i:submit(x, game, master, sockets))
        buttons[i].grid(row = i//3, column = i%3,sticky='nsew')

    configGrid(master)
    updatePos(master, game.board)
    
    
    

def disableGrid(master:tk.Tk, game:BoardClass, sockets):
    for i in range(9):
        buttons[i] = tk.Button(master, text = '')
        buttons[i].grid(row = i//3, column = i%3,sticky='nsew')

    configGrid(master)
    updatePos(master, game.board)
    print("Listening")
    p2_move = int(sockets.recv(1024).decode())
    print("received")
    game.updateGameBoard(p2_move, 'x')
    if game.isWinner():
        print("x WINS")
        game.addloss()
    if game.boardIsFull():
        game.addtie()
        print("NOBODY WINS")
    print("updated")
    creategrid(master, game, sockets)
    print("BOAR DSHOUDL WORK")
    


def updatePos(master:tk.Tk, board):
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
        print("GOOD MOVE")
        game.updateGameBoard(ind +1 , 'o')
        print("DONE")
        
        # print(game.board)
        sockets.send(str(ind+1).encode())
        print('sent"')
        disableGrid(master, game, sockets)
        

def flush_input():
    '''copied from rosettacode.com to clear input buffer
        exception if the import doesn't work, try another way ig '''
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def play_again(game: BoardClass, sockets: socket):
    '''receives if play again
        returns bool whether to play again or not

        arg, game:boardclass, sockets: socket
        
        ex: go(game)
        '''
    play_again = sockets.recv(1024).decode()
    if play_again == 'Play Again':
        game.resetGameBoard()
        return True
    return False

def receive(game: BoardClass, sockets:socket):
    '''recieves other player move, updates and prints board

    args game:boardclass, socket:socket
dis
    ex:
    receive() 

    no returns

    '''

    opp_move= int(sockets.recv(1024).decode())
    game.updateGameBoard(opp_move, 'x')
    game.printBoard()

def getmove(game: BoardClass, sockets:socket):
    '''gets move and prints updated board
    
        args: game:boardclass, sockets:socket

        ex:
        getmove()
        [in termina]
        3
        
        returns nothing
        
        '''
    flush_input()
    try:
        p2_move= int(input('your move 1-9\n'))
    except:
        p2_move = 10
    #123
    #456
    #789
    valid = game.isValid(p2_move)
    while not valid:
        try:
            p2_move = int(input('your move 1-9\n'))
            valid = game.isValid(p2_move)
        except:
            pass
    if game.isWinner():
        print("O WINS")
        game.addwin()
    if game.boardIsFull():
        game.addtie()
        print("NOBODY WINS")
    sockets.send(str(p2_move).encode())
    game.updateGameBoard(p2_move, 'o')
    game.create
    

def run(game: BoardClass, otheruser:str, sockets:socket):
    ''' gets user move, checks for end game, recieves p2 move, checks for end game

        args: game:boardclass, otheruser: string, sockets:sockets
    
        ex:
        run()
        no returns
    '''
    game.updateGamesPlayed()
    game.setLastUser(otheruser)
    while not game.boardIsFull() or not game.isWinner():
        receive(game, sockets)
        game.setLastUser(otheruser)
        if game.isWinner():
            print("x WINS")
            game.addloss()
            break
        if game.boardIsFull():
            game.addtie()
            print("NOBODY WINS")
            break
        getmove(game, sockets)
        game.setLastUser('player2')
        if game.isWinner():
            print("O WINS")
            game.addwin()
            break
        if game.boardIsFull():
            game.addtie()
            print("NOBODY WINS")
            break
        


def connect():
    ''' connect sto other player
    no params,
    returns tuple of address and port

    ex:
        connect()
        [int term]
        127.0.0.1
        8003
        [outside]
    
    '''
    #using the looback addy as servier ip addy
    # serverAddress = input("ip")
    # #def a port nnumber for server
    # port = int(input("port"))
    # return (serverAddress, port)
    return ('127.0.0.1', 8016)



if __name__ == "__main__":
    #create a socket obj
    not_connected = True
    while not_connected:
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #bind my host with my port number
            serverSocket.bind(connect())
            not_connected = False
        except:
            print('didnt work')
    
    buttons = [0,0,0,0,0,0,0,0,0]

    #setup socket using listen
    # 5 means max num connections socket allows
    serverSocket.listen(0)
    #begin accepting incoming connection requrests
    sockets, clientAddress = serverSocket.accept()
    #printing the client address
    otheruser= sockets.recv(1024).decode()

    sockets.send('player2'.encode())
    game = BoardClass('player2', otheruser, player = 'o')
    master = canvasSetup()
    disableGrid(master,game,sockets)
    startUI(master)
    run(game, otheruser, sockets)
    while play_again(game, sockets):
        run(game, otheruser, sockets)
    game.printStats()
    serverSocket.close()
