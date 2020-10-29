class drawMove:
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