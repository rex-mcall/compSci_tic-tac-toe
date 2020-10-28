import sqlite3
import random
tttBoard = [[1,2,3], [4,5,6], [7,8,9]]
con = sqlite3.connect('winloss.db')
cur = con.cursor()

def NewPlayer(): # adds new player to data base
    playName = input("enter name: ")
    cur.execute("INSERT INTO win_record VALUES('rex',0,0,0)")
    con.commit()

def UpdateScore(Winner, Loser): # updates score pass wiiner first and loser 2nd
    cur.execute("""UPDATE win_record SET wins = :wins
                WHERE name = :name""",{'name': Winner, 'wins' : num })


def PrintDatabase(): #prints whole database 
    print(cur.fetchall())
def testInt():
    NewPlayer()
    cur.execute("SELECT * FROM win_record Where name ='rex'")
    print(cur.fetchone())
testInt()

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

#
# the function draws the computer's move and updates the board
#
def DrawMove(board):
    
    EnterMove(tttBoard)
    DisplayBoard(tttBoard)
    if VictoryFor(tttBoard, 'X'):
        print("You win!")
        exit(0)
    print("My turn: ")
    ff = MakeListOfFreeFields(tttBoard)
    if len(ff) == 0: 
        print("Tie")
        exit(0)
    randomMove = random.randrange(1,len(ff))
    try:
        tttBoard[ff[randomMove][0]][ff[randomMove][1]] = "O"
        DisplayBoard(tttBoard)
    except ValueError:
        pass
    if VictoryFor(tttBoard, 'O'):
        print("You lose!")
        exit(0)

def startup():
    PrintDatabase()
    DisplayBoard(tttBoard)

def main():
    while(1):
        DrawMove(tttBoard)




startup()
main()
con.close()

