tttBoard = [["X",2,3], [4,"O",6], [7,8,"X"]]
import random
def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    bLine = "+---------+---------+---------+"
    sLine = "|         |         |         |" # can u run code
    print(bLine)
    for x in range(0, 3):
        print(sLine)
        print("|   ", board[x][0], "   |   ", board[x][1], "   |   ", board[x][2], "   |")
        print(sLine)
        print(bLine)


def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    #
    move = int(input("Enter your move: "))
    for i in range(0,3):
        try:
            board[i][board[i].index(move)] = "X"
        except ValueError:
                pass

def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    loff = []
    for x in range(0,3):
        for i in tttBoard[x]:
            for y in range(1,10):
                if i == y:
                    loff.append((x,board[x].index(i)))
                    break
    return loff

def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    #
    for x in range(0,3):
        if board[x].count(sign) == 3: return True
        if board[0][x] == sign and board[1][x] == sign and board[2][x] == sign: return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: return True
    return False
def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    EnterMove(tttBoard)
    DisplayBoard(tttBoard)
    if VictoryFor(tttBoard, 'X'):
        print("You win!")
        exit(0)
    ff = MakeListOfFreeFields(tttBoard)
    randomMove = random.randrange(0,len(ff))
    for i in range(0,3):
        try:
            tttBoard[i][tttBoard[i].index(randomMove[ff](1))] = "O"
            DisplayBoard(tttBoard)
        except ValueError:
                pass


DrawMove(tttBoard)