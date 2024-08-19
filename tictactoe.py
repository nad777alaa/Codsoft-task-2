import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
Cplayer = "X"
winner = None
gameRun = True

def gameBoard (board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("-----")


def playInput (board):
    inp = int(input("select a position from 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = Cplayer
    else:
        print("Position occupied!")



def checkHoriz (board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True



def checkVerti (board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiag (board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True



def checkWin (board):
    global gameRun
    if checkHoriz(board):
        gameBoard(board)
        print("The winner is " + winner)
        gameRun = False
    elif checkVerti(board):
        gameBoard(board)
        print("The winner is " + winner)
        gameRun = False
    elif checkDiag(board):
        gameBoard(board)
        print("The winner is " + winner)
        gameRun = False


def checkTie (board):
    global gameRun
    if "-" not in board:
        gameBoard(board)
        print("It is a Tie!")
        gameRun = False



def switchPlayr ():
    global Cplayer
    if Cplayer == "X":
        Cplayer = "O"
    else:
        Cplayer = "X"



def CompPlayer (board):
    while Cplayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayr()





while gameRun :
    gameBoard(board)
    playInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayr()
    CompPlayer(board)
    checkWin(board)


