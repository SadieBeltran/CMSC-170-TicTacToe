import tkinter as tk
from tkinter.ttk import *
from functools import partial

PLAYERS = ['X', 'O']
MAXTILES = 9
tileFilled = 0
currentPlayer = "X"
tiles = [-1]*9
waiting = True

def startGame():
    global currentPlayer
    global guiTiles
    global tiles
    global tileFilled
    movesMade = 0
    
    
    choosePlayer = input("Choose Turn: (O) or (X) - ").strip()
    ai = "X" if choosePlayer == "O" else "O"
    root.mainloop()
    while checkIfWin(tiles, tileFilled) == -1 and not checkIfDraw(tiles):
        for pl in PLAYERS:
            currentPlayer = pl
            if movesMade == 9:
                return "Draw"
            # printTiles(tiles)
            if pl == ai:
                print("Ai turn")
                tiles, tileFilled = aiProgram(tiles, ai)
                guiTiles[tileFilled]['text'] = pl
                root.update()
                waiting = True
            else:
                print("Player turn")
                while waiting:
                    pass
            movesMade += 1
            winner = checkIfWin(tiles, tileFilled)
            if checkIfWin(tiles, tileFilled) != -1:
                return "AI wins!" if winner == ai else "Player wins!"
            print("")

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

### GUI SECTION
# root = tk.Tk()

def playMove(row, col):
    global currentPlayer
    global tileFilled
    global tiles
    global guiTiles
    global waiting

    if tiles[row*3+col] == -1:
        guiTiles[row*3+col]['text'] = currentPlayer
        tiles[row*3+col] = currentPlayer
        root.update()
        waiting = False
        tileFilled = row*3+col

# # create buttons
# guiTiles = []
# for row in range(0,3):
#     for col in range(0,3):
#         i = " " if tiles[row*3+col] == -1 else tiles[row*3+col]
#         guiTiles.append(tk.Button(root, text=i, padx=30, pady=30, command=lambda r=row, j=col: playMove(r,j)))
#         guiTiles[row*3+col].grid(row=row, column=col)

# # print(startGame())