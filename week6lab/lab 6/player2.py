#import he sockets lib
import socket
from gameboard import BoardClass

#using the get host function
#print("Desktop Name: " +socket.gethostname())

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

    ex:
    receive() 

    no returns

    '''

    opp_move= int(sockets.recv(1024).decode())
    game.board[opp_move] = 'x'
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

    game.creategrid()
    while not game.gone:
        print("Waiting")
    game.disableGrid()

    

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
        8000
        [outside]
    
    '''
    #using the looback addy as servier ip addy
    serverAddress = input("ip")
    #def a port nnumber for server
    port = int(input("port"))
    return (serverAddress, port)


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
        

    #setup socket using listen
    # 5 means max num connections socket allows
    serverSocket.listen(0)
    #begin accepting incoming connection requrests
    sockets, clientAddress = serverSocket.accept()
    #printing the client address
    otheruser= sockets.recv(1024).decode()

    sockets.send('player2'.encode())
    game = BoardClass('player2', otheruser, 'x')
    run(game, otheruser, sockets)
    while play_again(game, sockets):
        run(game, otheruser, sockets)
    game.printStats()
    serverSocket.close()



