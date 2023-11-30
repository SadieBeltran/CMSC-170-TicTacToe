
def startGame():
    tiles = [-1]*9
    PLAYERS = ['X', 'O']
    i = 0
    j = 0
    while not checkIfWin(tiles, j):
        for pl in PLAYERS:
            if i == 8:
                break
            printTiles(tiles)
            tiles, j = updateTile(tiles, pl)
            if checkIfWin(tiles, j):
                return "Player "+pl+" wins"
            i += 1
    return "Draw"

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