import tkinter as tk
from tkinter.constants import X
from random import choice, randint
from time import sleep

labels = []
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
computerChoices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
turn = 0
winner = None

window = tk.Tk()

statusFrame = tk.Frame(master=window)
boardFrame = tk.Frame(master=window)

gameUpdate = tk.Label(master = statusFrame, text = "You start first", height = 1)
gameUpdate.pack()

combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def computerChoice():
    global winner, turn, combos
    if len(computerChoices) == 0:
        gameUpdate.config(text = "You tied!")
    decision = choice(computerChoices)
    labels[decision].config(text = 'O')
    board[decision] = "o"
    computerChoices.remove(decision)
    winner = False
    for c in combos:
        if (board[c[0]] == "o" and board[c[1]] == "o" and board[c[2]] == "o"):
            winner = True
            gameUpdate.config(text = "You lost to a robot that picks randomly lol!")
            window.destroy
            break
    if not winner:
            turn = 0
            gameUpdate.config(text = "No winners yet. Player's turn.")

def placeMark(event):
    global winner, turn, combos
    if turn == 0:
        label = event.widget
        i = labels.index(label)
        if i in computerChoices:
            label.config(text = 'X')
            board[i] = "x"
            computerChoices.remove(i)
            winner = False
            for c in combos:
                if (board[c[0]] == "x" and board[c[1]] == "x" and board[c[2]] == "x"):
                    winner = True
                    gameUpdate.config(text = "You won!")
                    break
            if not winner:
                gameUpdate.config(text = "No winners yet. Computer's turn.")
                window.after(randint(500, 2000), computerChoice)
                turn = 1

for i in range(3):
    for j in range(3):
        frame = tk.Frame(master=boardFrame, relief=tk.RAISED, borderwidth=4)
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, width = 2, height = 1, font = ("Bebas Neue", 60))
        label.bind("<Button-1>", placeMark)
        label.pack()
        labels.append(label)

boardFrame.pack()
statusFrame.pack()
window.mainloop()
