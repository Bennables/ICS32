#import he sockets lib
import socket
from gameboard import BoardClass

#using the get host function
#print("Desktop Name: " +socket.gethostname())

def flush_input():
    '''from rosettacode to clear input buffer '''
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def go(game: BoardClass):
    '''receives if play again
        returns bool whether to play again or not

        param: game of boardclass 
        
        ex: go(game)
        '''
    play_again = sockets.recv(1024).decode()
    if play_again == 'Play Again':
        game.resetGameBoard()
        return True
    return False

def receive(game: BoardClass):
    '''recieves other player move, updates and prints board

    params: game of type boardclass

    ex:
    receive() 

    no returns

    '''

    opp_move= int(sockets.recv(1024).decode())
    game.updateGameBoard(opp_move, 'x')
    game.printBoard()

def getmove(game: BoardClass):
    '''gets move and prints updated board
    
        parameter: game of boardclass class

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
    sockets.send(str(p2_move).encode())
    game.updateGameBoard(p2_move, 'o')
    game.printBoard()
    

def run(game: BoardClass, otheruser):
    ''' gets user move, checks for end game, recieves p2 move, checks for end game

        param is game of baordclass class
    
        ex:
        run()
        no returns
    '''
    game.updateGamesPlayed()
    game.setLastUser(otheruser)
    while not game.boardIsFull() or not game.isWinner():
        receive(game)
        game.setLastUser(otheruser)
        if game.isWinner():
            print("x WINS")
            game.addloss()
            break
        if game.boardIsFull():
            game.addtie()
            print("NOBODY WINS")
            break
        getmove(game)
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
    no returns

    ex:
        connect()
        [int term]
        127.0.0.1
        8000
        [outside]
    
    '''
    #using the looback addy as servier ip addy
    serverAddress = input("ip")
    #def a port nnumber for server
    port = int(input("port"))
    return (serverAddress, port)

#create a socket obj
j = True
while j:
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #bind my host with my port number
        serverSocket.bind(connect())
        j = False
    except:
        print('didnt work')

#setup socket using listen
# 5 means max num connections socket allows
serverSocket.listen(0)
#begin accepting incoming connection requrests
sockets, clientAddress = serverSocket.accept()
#printing the client address
otheruser= sockets.recv(1024).decode()
sockets.send('player2'.encode())
game = BoardClass('player2', otheruser)
run(game, otheruser)
while go(game):
    run(game, otheruser)
    
game.printStats()
serverSocket.close()



