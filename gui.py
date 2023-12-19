from tkinter import *
from tkinter import ttk
import tictacAI
MAXROW = 3
# create buttons
guiTiles = []
tiles = []*9

root = Tk()
tictacGame = Tk()
tiles = [-1]*9

def player1():
    global root
    root.destroy()
    #player = X
    createGrid(1)
    print("Pl 1")

def player2():
    #player = O
    global tiles
    global root
    root.destroy()
    
    print("waiting for ai")
    tiles, _ = tictacAI.aiProgram(tiles, "X")
    createGrid(2)
    print("Pl 2")

def playMove(move, player):
    global guiTiles
    global tiles
    global tictacGame

    if player == 1:
        tiles[move] = "X"
        guiTiles[move]["text"] = "X"
        tictacGame.update()
        winner = tictacAI.checkIfWin(tiles, move)
        disableAllButtons()
        tiles, aiMove = tictacAI.aiProgram(tiles, "O")
        guiTiles[aiMove]["text"] = "O"
    elif player == 2:
        tiles[move] = "O"
        guiTiles[move]["text"] = "O"
        tictacGame.update()
        winner = tictacAI.checkIfWin(tiles, move)
        disableAllButtons()
        tiles, aiMove = tictacAI.aiProgram(tiles, "X")
        guiTiles[aiMove]["text"] = "X"
    enableAllButtons()
    winner = tictacAI.checkIfWin(tiles, aiMove)
    if winner != -1:
        disableAllButtons()
        winAnnounce(tictacGame, winner, player)
        tictacGame.quit()

def winAnnounce(tictacGame, winner, player):

    annoucement = Toplevel(tictacGame)
    if winner == 0:
        label = "Draw!"
    elif winner == "X":
        label = "Player 1 wins!" if player == 1 else "AI wins!"
    elif winner == "O":
        label = "Player 2 wins!" if player == 2 else "AI wins!"
    Label(annoucement, text=label).pack(pady=20)


def disableAllButtons():
    for i in range(0,9):
        guiTiles[i].config(state="disabled", bg="light grey")
    return

def enableAllButtons():
    for i in range(0,9):
        guiTiles[i].config(state="normal", bg="white")
    return

#make user choose if P1 or P2
def choosePlayer():
    global root

    Label(root, text="Choose Player").pack()
    ttk.Button(root, text="Player 1", command=lambda: player1()).pack()
    ttk.Button(root, text="Player 2", command=lambda: player2()).pack()

def createGrid(pl):
    global guiTiles
    global tictacGame    
    label = "Tic Tac Toe - Player "+str(pl)
    
    Label(tictacGame, text=label)
    for row in range(0,3):
        for col in range(0,3):
            i = " " if tiles[row*3+col] == -1 else tiles[row*3+col]
            guiTiles.append(Button(tictacGame, text=i, padx=30, pady=30, command=lambda i=row*3+col, player=pl: playMove(i, player)))
            guiTiles[row*3+col].grid(row=row, column=col)
    tictacGame.mainloop()
choosePlayer()
root.mainloop()
