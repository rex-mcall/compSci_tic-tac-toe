tttBoard = [["X",2,3], [4,"O",6], [7,8,"X"]]

def DisplayBoard(board):
    bLine = "+---------+---------+---------+"
    print(bLine)
    for x in range(0,3):
        print("|   ",board[x][0],"   |   ",board[x][1],"   |   ",board[x][2],"   |")
        print(bLine)
            

#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

DisplayBoard(tttBoard)