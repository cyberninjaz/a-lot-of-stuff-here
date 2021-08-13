from random import *
dogeenergy = 30
dogehp = 0
btcdmg = 200
btcenergy = 20
btchp = 0
ethdmg = 150
ethenergy = 10
ethhp = 0
ltcdmg = 100
ltcenergy = 5
ltchp = 0
fooddmg = 0
foodenergy = 10
foodhp = 0
meddmg = 0
medenergy = 0
medhp = 10

p1hp = 1000
p2hp = 1000
p1energy = 100
p2energy = 100
player = 0

def options():
    print(f'Player {player}: Pick a move: ')
    print(f'Dogecoin: Damage: 200 - 300, Energy: -{dogeenergy}, Health: {dogehp}')
    print(f'Bitcoin: Damage: {btcdmg}, Energy: -{btcenergy}, Health: {btchp}')
    print(f'Ethereum: Damage: {ethdmg}, Energy: -{ethenergy}, Health: {ethhp}')
    print(f'Litecoin: Damage: {ltcdmg}, Energy: -{ltcenergy}, Health: {ltchp}')
    print(f'Food: Damage: {fooddmg}, Energy: +{foodenergy}, Health: {foodhp}')
    print(f'Medicine: Damage: {meddmg}, Energy: {medenergy}, Health: +{medhp}')

while p1hp > 0 and p2hp > 0 and p1energy > 0 and p2energy > 0:
    player = 1
    options()
    attack = input('Attack Move: ')
    if attack == 'Dogecoin':
        dogedmgamount = randint(200, 300)
        p2hp = p2hp - dogedmgamount
        p1energy = p1energy - dogeenergy
        print(f'Doge damage amount: {dogedmgamount}')
    elif attack == 'Bitcoin':
        p2hp = p2hp - btcdmg
        p1energy = p1energy - btcenergy
    elif attack == 'Ethereum':
        p2hp = p2hp - ethdmg
        p1energy = p1energy - ethenergy
    elif attack == 'Litecoin':
        p2hp = p2hp - ltcdmg
        p1energy = p1energy - ltcenergy
    elif attack == 'Food':
        p2hp = p2hp - fooddmg
        p1energy = p1energy + foodenergy
    elif attack == 'Medicine':
        p1hp = p1hp + medhp
        p1energy = p1energy - medenergy
    else:
        print('An invalid attack move was entered')
    print(f'Player 2 health: {p2hp}')
    print(f'Player 1 energy: {p1energy}')
    player = 2
    options()
    attack = input('Attack Move: ')
    if attack == 'Dogecoin':
        p2hp = p2hp - randint(200, 300)
        p2energy = p2energy - dogeenergy
    elif attack == 'Bitcoin':
        p1hp = p1hp - btcdmg
        p2energy = p2energy - btcenergy
    elif attack == 'Ethereum':
        p1hp = p1hp - ethdmg
        p2energy = p2energy - ethenergy
    elif attack == 'Litecoin':
        p1hp = p1hp - ltcdmg
        p2energy = p2energy - ltcenergy
    elif attack == 'Food':
        p1hp = p1hp - fooddmg
        p2energy = p2energy + foodenergy
    elif attack == 'Medicine':
        p2hp = p2hp + medhp
        p2energy = p2energy - medenergy
    else:
        print('An invalid attack move was entered')
    print(f'Player 1 health: {p1hp}')
    print(f'Player 2 energy: {p2energy}')

if p1hp == 0 or p1energy == 0:
    print('Player 1 died')
    print('Player 2 won')
elif p2hp == 0 or p2energy == 0:
    print('Player 2 died')
    print('Player 1 won')










#playerpicksmove
#bothealthdecrease
#botpicksrandommove
#playerhealthdecrease
#moves:
#    dogecoin: -30 energy, 200 - 300 damage
#    bitcoin: -20 energy, 200 damage
#    ethereum: -10 energy, 150 damage
#    litecoin: -5 energy, 100 damage
#    food: +10 energy
#    medicine: +10 damage
#once one dies: say win or lose and say number of rounds survived
