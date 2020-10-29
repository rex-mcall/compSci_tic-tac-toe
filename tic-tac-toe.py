import sqlite3
import random
originalBoard = [[1,2,3], [4,5,6], [7,8,9]]
tttBoard = [[1,2,3], [4,5,6], [7,8,9]]
con = sqlite3.connect('winloss.db')
cur = con.cursor()

playName = ""
playName2 = ""
playMode = 0

def NewPlayer_1(): # adds new player to data base if they don't already exist
    currNames = cur.execute("SELECT name from win_record")
    for i in currNames:
        if playName == i: return
    cur.execute("INSERT INTO win_record (name, wins, loss, tie) VALUES(?, ?, ?, ?)", (playName,0,0,0))
    con.commit()

def NewPlayer_2(): # adds new player to data base if they don't already exist
    currNames = cur.execute("SELECT name from win_record")
    for i in currNames:
        if playName2 == i: return
    cur.execute("INSERT INTO win_record (name, wins, loss, tie) VALUES(?, ?, ?, ?)", (playName2,0,0,0))
    con.commit()

def UpdateScore(Winner, Loser): # updates score pass wiiner first and loser 2nd
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : Winner})
    w = cur.fetchone()
    cur.execute("UPDATE win_record (wins) VALUES(?)",((w[1]+1)))
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : Loser})
    L = cur.fetchone()
    cur.execute("UPDATE win_record (wins) VALUES(?)",((w[2]+1)))
 
   

def Tie(p1,p2):
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : p1})
    p1s = cur.fetchone()
    cur.execute("UPDATE win_record (wins) VALUES(?)",((p1s[3]+1)))
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : p2})
    p2s = cur.fetchone()
    cur.execute("UPDATE win_record (wins) VALUES(?)",((p2s[3]+1)))
    
def PrintDatabase(): #prints whole database 
    print(cur.fetchall())


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
def DrawMove_computer(board):
    
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

def DrawMove_multiplayer(board):
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
    choice = int(input("Choose mode:\n1: Computer\n2: Multiplayer\n> "))
    playMode = choice

    if playMode == 1:
        print("You are now playing against the computer.")
    if playMode == 2:
        print("You are now playing in multiplayer mode.")

    playName = input("Enter player 1 name:\n> ")
    NewPlayer_1()

    if playMode == 2:        
        playName2 = input("Enter player 2 name:\n>  ")
        NewPlayer_2()
    
    PrintDatabase()
    DisplayBoard(tttBoard)

def main():
    while(1):
        if playMode == 1:
            DrawMove_computer(tttBoard)
        elif playMode == 2:
            DrawMove_multiplayer(tttBoard)
        else:
            exit(1)




startup()
main()
con.close()

