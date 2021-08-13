from random import randint

class Player():
    hp = 1000
    energy = 100
    name = None

    def __init__ (self, name):
        self.name = name
    
    def isAlive(self):
        return self.hp > 0 and self.energy > 0

p1 = Player('CYBER HACKER')
print('p1.name')

p2 = Player('CYBER NINJA')
print(f'Hi {p2.name}')


class Attack():
    name = None
    mindamage = None
    maxdamage = None
    energy = None
    hpheal = None
    energyheal = None

    def __init__ (self, name, mnD, mxD, e, hh, eh):
        self.name = name
        self.mindamage = mnD
        self.maxdamage = mxD
        self.energy = e
        self.hpheal = hh
        self.energyheal = eh

    def use(self, user, target):
        target.hp -= randint(self.mindamage, self.maxdamage)
        user.energy -= self.energy
        user.hp += self.hpheal
        user.energy += self.energyheal
        print('BOOM!!!')

    def printStats(self):
        print(f'{self.name}: Damage: {self.mindamage}-{self.maxdamage}, Energy: -{self.energy}, Health Heal: {self.hpheal}, Energy Heal: {self.energyheal}')

dogecoin = Attack('Dogecoin', 200, 300, 30, 0, 0)
bitcoin = Attack('Bitcoin', 200, 200, 20, 0, 0)
ethereum = Attack('Ethereum', 150, 150, 10, 0, 0)
litecoin = Attack('Litecoin', 100, 150, 5, 0, 0)
medicine = Attack('Medicine', 0, 0, 0, 100, 0)
food = Attack('Food', 0, 0, 0, 0, 10)

moves = [dogecoin, bitcoin, ethereum, litecoin, medicine, food]

def options():
    for x in moves:
        x.printStats()

while p1.hp > 0 and p2.hp > 0 and p1.energy > 0 and p2.energy > 0:
    options()
    move = input('Move: ')
    for x in moves:
        if move == x.name:
            x.use(p1, p2)
            break
    print(f'Player 2 health: {p2.hp}')
    print(f'Player 1 energy: {p1.energy}')
    options()
    move = input('Move: ')
    for x in moves:
        if move == x.name:
            x.use(p2, p1)
            break
    print(f'Player 1 health: {p1.hp}')
    print(f'Player 2 energy: {p2.energy}')
if p1.energy == 0 or p1.hp == 0:
    print('PLAYER 2 WON!!!')
elif p2.energy == 0 or p2.hp == 0:
    print('PLAYER 1 WON!!!')