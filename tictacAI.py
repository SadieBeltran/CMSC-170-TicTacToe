PLAYERS = ['X', 'O']
MAXTILES = 9

def aiProgram(tiles, plTile):
    simTile = tiles[:]
    bestMove = 0 
    maxVal = -999
    
    for i in range(0, MAXTILES):
        if tiles[i] == -1:
            simTile[i] = plTile
            v = minMax(simTile, False, plTile, i)
            if maxVal < v:
                maxVal = v
                bestMove = i
            simTile = tiles[:]
        # print("maxVal: "+str(maxVal))
    tiles[bestMove] = plTile
    return tiles, bestMove

def minMax(tiles, isMove, plTile, move):
    simTile = tiles[:]
    enTile = "X" if plTile == "O" else "O"
    m = -999 if isMove else 999
    winner = checkIfWin(simTile, move)

    if winner == plTile: 
        return 1
    elif winner == enTile: return -1
    elif winner == 0: return 0
    elif winner == -1:
        for i in range(0, MAXTILES):
            if simTile[i] == -1:
                simTile[i] = plTile if isMove else enTile
                v = minMax(simTile, False, plTile, i) if isMove else minMax(simTile, True, plTile, i)
                
                if isMove: #maximizing m = -999
                    v = minMax(simTile, False, plTile, i) 
                    if m < v:
                        m = v
                else: #minimizing m = 999
                    v = minMax(simTile, True, plTile, i) 
                    if m > v: m = v
                simTile = tiles[:]
        # print("m: "+str(m))
        return m

def checkIfWin(tiles, i):
    #check if there are enough filled tiles to form a win in the array
    sum = 0
    for e in tiles:
        if e == -1:
            sum += e
    
    if sum < -4:
        return -1
    else:
        if tiles[i] == 'X' or tiles[i] == 'O':
                #check horizontal and vertical
            if checkHorizontal(tiles, i, tiles[i]) or checkVertical(tiles, i, tiles[i]) or checkDiagonal(tiles, i, tiles[i]):
                return tiles[i]
    if checkIfDraw(tiles): return 0
    return -1

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

def checkIfDraw(tiles):
    sum = 0
    for e in tiles:
        if e == -1:
            sum += e
    return True if sum == 0 else False
