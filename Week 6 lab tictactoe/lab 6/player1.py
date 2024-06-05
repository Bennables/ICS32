import socket
from gameboard import BoardClass
import time
import signal
import board



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

def connect():
    '''connects to the other

    no args
    returns nothing
    exception if socket fails to connect or type of input wrong
        just tries again

    ex:
        connect()
        [in termina] 
        ip address (enter)
        port (enter)
    
        
        '''
    sockets = None
    try_connect= 'y'
    while try_connect == 'y':

        try:
            
            sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            p2addy = input("p1 give p2 ip address")
            p2host = int(input("p1 give port"))
            with timeout(seconds=3):
                sockets.connect((p2addy,p2host))
            try_connect = ''
        except Exception as e:
            print(e)
            try_connect = input('again? (y/n)').strip()
            try_connect = try_connect.lower()
            sockets.close()
            while not (try_connect == 'y' or try_connect =='n'):
                try_connect = input('again? (y/n)').strip()
                try_connect = try_connect.lower()
            if try_connect == 'n':
                exit(0)
    return sockets


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
    

def getMove(game: BoardClass, sockets:socket, gui:board):
    '''gets move and prints updated board
    
        arg: game:boardclass, sockets:socket

        ex:
        getmove()
        [in termina]
        3
        
        returns nothing
        excepts for bad moves and asks for a new move
        '''
    
    #123
    #456
    #789
    valid = game.isValid(move)
    while not valid:
        try:
            move = int(input('your move 1-9\n'))
            valid = game.isValid(move)
        except:
            pass
    sockets.send(str(move).encode())
    game.updateGameBoard(move, 'x')
    game.printBoard()
    


def receive(game: BoardClass, sockets:socket):
    '''recieves other player move, updates and prints board

    params: game:boardclass, sockets:socket

    ex:
    receive() 

    no returns
    no exceptions

    '''
    p2_move = int(sockets.recv(1024).decode())
    game.updateGameBoard(p2_move, 'o')
    game.printBoard()


def run(game: BoardClass, user:str, sockets:socket, gui: board):
    ''' gets user move, checks for end game, recieves p2 move, checks for end game

        args: game:boardclass, user:str, sockets:socket
    
        ex:
        run()

        no returns
        no exceptions
    '''
    game.setLastUser(None)
    game.updateGamesPlayed()
#nobody has won yet and board isn't full
    while not game.isWinner() or not game.boardIsFull():
        getMove(game, sockets, gui)
        game.setLastUser(user)
        if game.isWinner():
            print("x WINS")
            game.addwin()
            break
        if game.boardIsFull():
            print("NOBODY WINS")
            game.addtie()
            break
        receive(game, sockets)
        game.setLastUser('player2')

        if game.isWinner():
            print("o WINS")
            game.addloss()
            break
        if game.boardIsFull():
            print("NOBODY WINS")
            game.addtie()
            break
    


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
    gui = board('x')
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockets = connect()
    user, p2_user = sendUser(sockets)
    game = BoardClass(user,p2_user)
    run(game,user, sockets, gui)
    while play_again(game, sockets):
        run(game,user, sockets)
    game.printStats()
    sockets.close()
