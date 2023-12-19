PLAYERS = ['X', 'O']
MAXTILES = 9
tiles = [-1]*9

def startGame():
    #how to set one of the players as AI (ig if-else statement na lang)
    global tiles
    i = 0
    j = 0
    #j is the updated tile
    choosePlayer = input("Choose Turn: (O) or (X) - ")
    ai = "X" if choosePlayer.strip() == "O" else "O"

    while not checkIfWin(tiles, j) and not checkIfDraw(tiles):
        for pl in PLAYERS:
            if i == 9:
                return "Draw"
            printTiles(tiles)
            if pl == ai:
                aiProgram(tiles, ai, i)
            else:
                tiles, j = updateTile(tiles, pl)
            if checkIfWin(tiles, j):
                return "Player "+pl+" wins"
            i += 1

def aiProgram(tiles, plMove, move):
    #accepts a tile, and what move it is as well as the current turn
    #ig program muna ung pagfillup ng table (alternating)
    
    #receive state ng tile, duplicate it into newtile para hindi ma-modify ung contents
    tempTile = tiles[:]
    aiplayers = PLAYERS[-len(PLAYERS):] if plMove == 'O' else PLAYERS #reverse list if AI == O

    j = 0 x
    
    while not checkIfWin(tempTile, j) and not checkIfDraw(tempTile):
        #start muna sa plMove. First move is the first blank space    
        for player in aiplayers:
            if move == 9:
                return "Draw"
            printTiles(tempTile)
            tempTile, j = aiUpdateTile(tempTile, player)
            printTiles(tempTile)
            if checkIfWin(tempTile, j):
                return "Player "+player+" wins"
            move += 1
    
    # should return move that yields best case scenario

def aiUpdateTile(tiles, plMove):
    print(tiles)
    print(plMove)
    #this function fills the most recent empty tile
    for i in range(0, MAXTILES):
        if tiles[i] == -1:
            tiles[i] = plMove
            print(tiles)
            return tiles, i

def printTiles(tiles):
    for i in range(1, len(tiles)+1):
        if tiles[i-1] == -1:
            print("[ ]", end=" ")
        else:
            print("["+tiles[i-1]+"]", end=" ")
        
        if i % 3 == 0:
            print("")

def updateTile(tiles, player):
    while True:
        print("= Player "+player+" Turn =")
        index = int(input("Input index: "))
        if tiles[index] == -1:
            tiles[index] = player
            return tiles, index
        else:
            print("THAT TILE HAS ALREADY BEEN FILLED!")

def checkIfDraw(tiles):
    sum = 0
    for e in tiles:
        if e == -1:
            sum += e
    return True if sum == 0 else False

def checkIfWin(tiles, i):
    #check if there are enough filled tiles to form a win in the array
    sum = 0
    for e in tiles:
        if e == -1:
            sum += e
    
    if sum < -4:
        return False
    else:
        if tiles[i] == 'X' or tiles[i] == 'O':
                #check horizontal and vertical
            if checkHorizontal(tiles, i, tiles[i]) or checkVertical(tiles, i, tiles[i]) or checkDiagonal(tiles, i, tiles[i]):
                return True
    return False

def checkHorizontal(tiles, i, elem):
    #get row
    row = int(i/3)*3
    for j in range(row, row+3):
        if tiles[j] != elem:
            return False
    return True

def checkVertical(tiles, i, elem):
    col = i%3
    j = col
    for _ in range(0,3):
        if tiles[j] != elem:
            return False
        j += 3
    return True

def checkDiagonal(tiles, i, elem):
    if i % 2 != 0:
        return False
    
    #check middle
    if tiles[4] != elem:
        return False
    #check left side and right side
    if (tiles[0] == elem and tiles[8] == elem) or (tiles[2] == elem and tiles[6] == elem):
        return True
    return False

print(startGame())
