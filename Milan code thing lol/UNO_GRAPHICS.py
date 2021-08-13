import tkinter as tk
from random import *

window = tk.Tk()

class Card():
    color = None
    number = None
    action = None

    def __init__(self, c, n, a):
        self.color = c
        self.number = n
        self.action = a

    def matches(self, other):
        return self.color == other.color or (self.number == other.number and self.number != None) or (self.action == other.action and self.action != None)
     
    def __str__(self):
        return f'{self.color}{self.action or self.number}'

    def __repr__(self):
        return self.__str__()
        
class Deck():
    #cards = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'rrev', 'rskp', 'r+2', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'brev', 'bskp', 'b+2', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'yrev', 'yskp', 'y+2', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'grev', 'gskp', 'g+2', 'w+4', 'w+4', 'w+0', 'w+0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'rrev', 'rskp', 'r+2', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'brev', 'bskp', 'b+2', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'yrev', 'yskp', 'y+2', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'grev', 'gskp', 'g+2', 'w+4', 'w+4', 'w+0', 'w+0']
    cards = []

    def __init__(self):
        for i in range(2):
            for color in ['red', 'green', 'blue', 'yellow']:
                for num in range(1, 10):
                    self.cards.append(Card(color, num, None))
                for ac in ['+2', 'skip', 'rev']:
                    self.cards.append(Card(color, None, ac))
            for i in range(2):
                self.cards.append(Card("Wild", None, "+4"))
                self.cards.append(Card("Wild", None, "+0"))
        for color in ['red', 'green', 'blue', 'yellow']:
            self.cards.append(Card(color, 0, None))

    def draw(self, n):
        c = []
        for i in range(n):
            play = choice(self.cards)
            self.cards.remove(play)
            c.append(play)
        return c

class Player():
    hand = []
    name = None

    def __init__ (self, deck, name):
        self.hand = deck.draw(7)
        self.name = name

deck = Deck()
cards = deck.draw(7)
w2 = tk.Toplevel()

def placeCard(event):
    event.widget.pack_forget()
    event.widget.config(master = w2)
    event.widget.pack()
    label = tk.Label(master = w2)
    label.pack()

for i in range(7):
    c = cards[i]
    print(f"{c.color} {c.number} {c.action}")
    color = c.color
    if color == "Wild":
        color = "black"
    label = tk.Label(text=c.action or c.number, font=("Arial", 32), width = 3, height = 2, bg = color, fg = "white", borderwidth = 10)
    #border_color = tk.Frame(window, background="red")
    #border_color.pack(padx=40, pady=40)
    label.pack(side=tk.LEFT)
    label.bind("<Button-1>", placeCard)
    label.pack()
window.mainloop()



