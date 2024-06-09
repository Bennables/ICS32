
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

def getmo(sockets):
    return int(sockets.recv(1024).decode())

def disableGrid(master:tk.Tk, game:BoardClass, sockets):
    for i in range(9):
        buttons[i] = tk.Button(master, text = '')
        buttons[i].grid(row = i//3, column = i%3,sticky='nsew')

    configGrid(master)
    updatePos(master, game.board)
    master.update()
    master.update_idletasks()
    print("Listening")
    p2_move = getmo(sockets)
    
    print("received")
    print(p2_move)
    if p2_move == 12:
        print("x WINS")
        game.addloss()
        game.resetGameBoard()
        
        for widget in master.winfo_children():
            widget.destroy()
        
        d = tk.Text(master)
        d.insert(tk.INSERT, 'X wins')
        d.pack()
        master.update_idletasks()
        time.sleep(3)
        d = int(sockets.recv(1024).decode())
        if d == 1:
            master.destroy()
            master= canvasSetup()
            disableGrid(master,game,sockets)
            master.update()
            master.update_idletasks()
            startUI(master)
            
        else:
            endgame(master,game)

    elif p2_move == 13:
        game.addtie()
        print("NOBODY WINS")
        game.resetGameBoard()
        for widget in master.winfo_children():
            widget.destroy()
        
        d = tk.Text(master)
        d.insert(tk.INSERT, 'Tie')
        d.pack()
        master.update_idletasks()
        time.sleep(3)
        d = int(sockets.recv(1024).decode())
        if d == 1:
            master.destroy()
            master= canvasSetup()
            disableGrid(master,game,sockets)
            master.update()
            master.update_idletasks()
            startUI(master)
            
        else:
            endgame(master,game)


    else:
        game.updateGameBoard(p2_move, 'x')
        print("updated")
        creategrid(master, game, sockets)
        print("BOAR DSHOUDL WORK")
    
    
def endgame(master, game : BoardClass):
    '''dfjlsdjfkldsf
    p'''
    master.destroy()
    master = canvasSetup()
    text = tk.Text(master)
    text.insert(tk.INSERT, game.printStats())
    text.pack()    
    startUI(master)


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
        sockets.send(str(ind+1).encode())
        if game.isWinner():

            game.addtie()
            print("o wins")
            game.resetGameBoard()
            for widget in master.winfo_children():
                widget.destroy()
            d = tk.Text(master)
            d.insert(tk.INSERT, 'o wins')
            d.pack()
            master.update_idletasks()
            d = int(sockets.recv(1024).decode())

            time.sleep(3)
            
            if d == 1:
                master.destroy()
                master= canvasSetup()
                disableGrid(master,game,sockets)
                master.update()
                master.update_idletasks()
                startUI(master)
            
            else:
                endgame(master,game)
            
        if game.boardIsFull():

            game.addtie()
            print("NOBODY WINS")
            game.resetGameBoard()
            for widget in master.winfo_children():
                widget.destroy()
        
            d = tk.Text(master)
            d.insert(tk.INSERT, 'Tie')
            d.pack()
            master.update_idletasks()
            time.sleep(3)
            d = int(sockets.recv(1024).decode())
            if d == 1:
                master.destroy()
                master= canvasSetup()
                disableGrid(master,game,sockets)
                master.update()
                master.update_idletasks()
                startUI(master)
                
            else:
                endgame(master,game)
                # game.addtie()
                # master.destroy()
                # game.resetGameBoard()
                # master =canvasSetup()
                # d = tk.Text(master)
                # d.insert(tk.INSERT, 'TIE')
                # d.pack()
                # startUI(master)
            # print(game.board)
        else:
            
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
    x = int(input('port'))
    return ('127.0.0.1', x)



if __name__ == "__main__":
    try:
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
        game.printStats()
        serverSocket.close()
    except:
        sockets.close()
