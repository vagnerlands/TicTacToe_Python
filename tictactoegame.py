#################################
# Tic Tac Toe Game in Python    #
# Developed by Vagner Landskron #
################################# 

InitialBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
BoardContent = list()
IsGameRunning = True
currentPlayer = 'X'

def SetNewGame():
    global BoardContent
    BoardContent = list(InitialBoard)

def PrintHeader():
    s = str("*"*32)
    print(s)
    print("Welcome to Tic Tac Toe Game")
    print("             by Vagner Landskron")
    print(s)
        

def PrintBoard(player):   
    global BoardContent     
    print("      |       |      ")
    print("  {}   |   {}   |   {}  ".format(BoardContent[0], BoardContent[3], BoardContent[6]))
    print("      |       |      ")
    print("------|-------|------")
    print("      |       |      ")
    print("  {}   |   {}   |   {}  ".format(BoardContent[1], BoardContent[4], BoardContent[7]))
    print("      |       |      ")
    print("------|-------|------")
    print("      |       |      ")
    print("  {}   |   {}   |   {}  ".format(BoardContent[2], BoardContent[5], BoardContent[8]))
    print("      |       |      ")
    
    print(" ")
    print(" It's {} player turn".format(player))
    
    
def GetUserInput():
    print("[1] Top Left     [4] Top Center     [7] Top Right")
    print("[2] Center Left  [5] Center Center  [8] Center Right")
    print("[3] Bottom Left  [6] Bottom Center  [9] Bottom Right")
    s = str("*"*32)
    print(s)
    return input("Select your movement: ")

def ValidateUserInput(userInput):
    global BoardContent
    isCellEmpty = False
    if 1 <= userInput <= 9:
        isCellEmpty = BoardContent[userInput - 1] == ' '
    # if cell is empty, then the range is also valid    
    return isCellEmpty
    
    
def CheckIfPlayerWon(player):
    global BoardContent
    winFlag = False
    setValues = list(BoardContent)
    for setKey in range(0,9,3):
        if setValues[setKey] == player and setValues[setKey + 1] == player and setValues[setKey + 2] == player:
            winFlag = True
    for setKey in range(0,3,1):
        if setValues[setKey] == player and setValues[setKey + 3] == player and setValues[setKey + 6] == player:
            winFlag = True
    if setValues[0] == player and setValues[4] == player and setValues[8] == player:
        winFlag = True
    if setValues[2] == player and setValues[4] == player and setValues[6] == player:
        winFlag = True
        
    return winFlag
	
def ExecuteMovement(location, player):
    global BoardContent
    BoardContent[location - 1] = player
    
def AlternatePlayer(currentPlayer):
    if currentPlayer == 'O':
        currentPlayer = 'X'
    else:
        currentPlayer = 'O'
        
    return currentPlayer
    
SetNewGame()    
while IsGameRunning and (BoardContent.count(' ') > 0):
    userInputValidity = False
    while (userInputValidity == False):
        PrintHeader()
        PrintBoard(currentPlayer)
        userInput = int(GetUserInput())
        userInputValidity = ValidateUserInput(userInput)
    ExecuteMovement(userInput, currentPlayer)
    if CheckIfPlayerWon(currentPlayer):
        PrintHeader()
        PrintBoard(currentPlayer)
		# congratulations message
        print("*"*55)
        print(" PLAYER " + currentPlayer + " HAS OWN THE GAME ! ! ! ")
        print("*"*55)
        IsGameRunning = False
    
    currentPlayer = AlternatePlayer(currentPlayer)
    