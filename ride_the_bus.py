import random
from initializer import *

num_players = int(input("Enter number of players: "))

for i in range(num_players):
    print("Enter name of player", i+1, ":")
    player_name = input("")
    player_name = Player(player_name)

print("Players: ", end="")
for p in Player.registry:
    print(p.name, end=" ")
print("\n")

def initial_round(players):
    deck = Deck()
    random.shuffle(deck.cards)

    for i in range(4):
        for p in Player.registry:
            p.draw(deck)
            print(p.name)
            p.showCards()
            input("Press Enter to continue...")
            print()

    print("First round complete\n")

    for i in range(8):
        print(i+1)
        card = deck.drawCard()
        card.show()
        for p in Player.registry:
            if p.check(card):
                if (i+1) % 2 == 0:
                    print(p.name, "has to take drink")
                else:
                    print(p.name, "has to give drink")
        input("Press Enter to continue...")
        print()

    final_card = deck.drawCard()
    final_card.show()
    for p in Player.registry:
        if p.check(final_card):
            print(p.name, "has to ride the bus")

initial_round(Player.registry)
