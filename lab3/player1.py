import socket
from gameboard import BoardClass
import time
import signal



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
def flush_input():
    '''from rosettacode to clear input buffer '''
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


class timeout:
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
global sockets
sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#attempt connect to server

def connect():
    '''connects to the other
    ex:
        connect()
        [in termina] 
        ip address (enter)
        port (enter)
    
        returns nothing
        '''
    try_connect= 'y'
    while try_connect == 'y':

        try:
            global sockets
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


def sendUser():
    '''asks for user and sends it to other person
        
        senduser()
        [in termina]
        USERNAME (enter)
        
    no return
    '''
    user = input('Username')
    sockets.send(user.encode())
    p2_user = sockets.recv(1024).decode()
    return user, p2_user
    #creates board with p1
    

def getMove(game: BoardClass):
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
        move = int(input('your move 1-9\n'))
    except:
        move = 10
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
    


def receive(game: BoardClass):
    '''recieves other player move, updates and prints board

    params: game of type boardclass

    ex:
    receive() 

    no returns

    '''
    p2_move = int(sockets.recv(1024).decode())
    game.updateGameBoard(p2_move, 'o')
    game.printBoard()


def run(game: BoardClass, user):
    ''' gets user move, checks for end game, recieves p2 move, checks for end game

        param is game of baordclass class
    
        ex:
        run()
        no returns
    '''
    game.setLastUser(None)
    game.updateGamesPlayed()
#nobody has won yet and board isn't full
    while not game.isWinner() or not game.boardIsFull():
        getMove(game)
        game.setLastUser(user)
        if game.isWinner():
            print("x WINS")
            game.addwin()
            break
        if game.boardIsFull():
            print("NOBODY WINS")
            game.addtie()
            break
        receive(game)
        game.setLastUser('player2')

        if game.isWinner():
            print("o WINS")
            game.addloss()
            break
        if game.boardIsFull():
            print("NOBODY WINS")
            game.addtie()
            break
    



'''

Player 1 will ask the user for their move using the built-in input() function
and send it to player 2.
Player 1 will always be x/X
Player 1 will always send the first move to player 2
Each move will correspond to the input given using the keyboard.
Once player 1 sends their move they will wait for player 2's move.
Repeat steps 3.1.2 - 3.1.4 until the game is over (A game is over when a winner is found or the board is full)
Once a game as finished (win or tie) the user will indicate if they want to play again using the command line.
If the user enters 'y' or 'Y' then player 1 will send "Play Again" to player 2
If the user enters 'n' or 'N' then player 1 will send "Fun Times" to player 2 and end the program
Once the user is done player they will print all the statistics.

'''

def go(game):
    ''' asks if you wanna play again. 

    params game of boardclass

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


connect()
user, p2_user = sendUser()
game = BoardClass(user,p2_user)
run(game,user)
while go(game):
    run(game,user)
game.printStats()
sockets.close()