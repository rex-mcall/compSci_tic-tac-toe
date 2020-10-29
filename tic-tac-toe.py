from drawMove import drawMove
import sqlite3
import random
import os
from drawMove import drawMove

originalBoard = [[1,2,3], [4,5,6], [7,8,9]]
tttBoard = [[1,2,3], [4,5,6], [7,8,9]]
con = sqlite3.connect('winloss.db')
cur = con.cursor()

playName = ""
playName2 = ""
playMode = 0

files = os.listdir('.')
dbExists = False
for i in files:
    if i == "winloss.db" and os.path.getsize("winloss.db") > 0 : dbExists = True
if dbExists: pass
else:
    cur.execute("""CREATE TABLE win_record (
    name text,
    wins integer,
    loss integer,
    tie integer
    )""")
    con.commit()
    cur.execute("INSERT INTO win_record (name, wins, loss, tie) VALUES(?, ?, ?, ?)", ("bot",0,0,0))
    con.commit()

def NewPlayer_1(): # adds new player to data base if they don't already exist
    cur.execute("SELECT name FROM win_record")
    currNames = cur.fetchall()
    playerExists = False
    for i in currNames:
        if playName == i[0]: playerExists = True
    if playerExists != True:
        cur.execute("INSERT INTO win_record (name, wins, loss, tie) VALUES(?, ?, ?, ?)", (playName,0,0,0))
        con.commit()

def NewPlayer_2(): # adds new player to data base if they don't already exist
    cur.execute("SELECT name FROM win_record")
    currNames = cur.fetchall()
    playerExists = False
    for i in currNames:
        if playName == i[0]: playerExists = True
    if playerExists != True:
        cur.execute("INSERT INTO win_record (name, wins, loss, tie) VALUES(?, ?, ?, ?)", (playName,0,0,0))
        con.commit()

def UpdateScore(Winner, Loser): # updates score pass wiiner first and loser 2nd
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : Winner})
    w = cur.fetchone()
    with con: 
        cur.execute("""UPDATE win_record SET wins = :wins 
                        WHERE name = :name """,
                        {'name': Winner,'wins':(w[1]+1)})
                        # cur.execute( "UPDATE win_record SET wins = ? WHERE true", ((w[1]+1)) )
            
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : Loser})
    L = cur.fetchone()
    with con:       
        cur.execute("""UPDATE win_record SET loss = :loss 
                        WHERE name = :name """,
                        {'name': Loser,'loss':(L[2]+1)})
                        #cur.execute("UPDATE win_record SET wins = ?",((L[2]+1)))
    con.commit()
 
   

def Tie(p1,p2):
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : p1})
    w = cur.fetchone()
    with con: 
        cur.execute("""UPDATE win_record SET tie = :tie 
                        WHERE name = :name """,
                        {'name': p1,'wins':(w[3]+1)})
                        # cur.execute( "UPDATE win_record SET wins = ? WHERE true", ((w[1]+1)) )
            
    cur.execute("SELECT * FROM win_record Where name = :name",{'name' : p2})
    L = cur.fetchone()
    with con:       
        cur.execute("""UPDATE win_record SET tie = :tie 
                        WHERE name = :name """,
                        {'name': p2,'tie':(L[3]+1)})
                        #cur.execute("UPDATE win_record SET wins = ?",((L[2]+1)))
    con.commit()
    
def PrintDatabase(): #prints whole database 
    cur.execute("SELECT * FROM win_record")
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
def EnterMoveP2(board):
    #
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    #
    move = int(input("Enter your move: "))
    for i in range(0,3):
        try:
            board[i][board[i].index(move)] = "O"
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
        UpdateScore(playName,"bot")
        end()
    print("My turn: ")
    ff = MakeListOfFreeFields(tttBoard)
    if len(ff) == 0: 
        print("Tie")
        Tie(playName,"bot")
        end()
    randomMove = random.randrange(1,len(ff))
    try:
        tttBoard[ff[randomMove][0]][ff[randomMove][1]] = "O"
        DisplayBoard(tttBoard)
    except ValueError:
        pass
    if VictoryFor(tttBoard, 'O'):
        print("You lose :(")
        UpdateScore("bot", playName)
        end()

def DrawMove_multiplayer(board):
    print("It is ", playName, "\'s turn")
    EnterMove(tttBoard)
    DisplayBoard(tttBoard)
    if VictoryFor(tttBoard, 'X'):
        print(playName, " wins!")
        UpdateScore(playName, playName2)
        end()


    ff = MakeListOfFreeFields(tttBoard)
    if len(ff) == 0: 
        print("Tie")
        Tie(playName,playName2)
        end()
    print("It is ", playName2, "\'s turn")
    EnterMoveP2(tttBoard)
    DisplayBoard(tttBoard)
    if VictoryFor(tttBoard, 'O'):
        print(playName2, "wins")
        UpdateScore(playName2,playName)

   
def startup():
    print("""
              ________________   _________   ______   __________  ______
             /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \/ ____/
              / /  / // /  ______/ / / /| |/ /  ______/ / / / / / __/   
             / / _/ // /__/_____/ / / ___ / /__/_____/ / / /_/ / /___   
            /_/ /___/\____/    /_/ /_/  |_\____/    /_/  \____/_____/      
         """)                                                   
       
    choice = int(input("Choose mode:\n1: Computer\n2: Multiplayer\n> "))
    global playMode
    
    playMode = choice

    if playMode == 1:
        print("You are now playing against the computer.")
    if playMode == 2:
        print("You are now playing in multiplayer mode.")

    global playName
    global playName2
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
            break
def playAgain():
    global tttBoard
    tttBoard = originalBoard
    playAgain = input("Play again? (y/n)\n> ")
    if playAgain == 'y':

        startup()
        main()
    elif playAgain == 'n':
        print("Goodbye")
        con.commit()
        con.close()
        exit(0)
    else:
        print("Please type y or n.")
        playAgain()

def end():
    print("Current standings:")
    PrintDatabase()
    playAgain()


startup()
main()
con.close()

