class Player:
    registry = []

    def __init__(self, name):
        self.registry.append(self)
        self.name = name
        self.cards = []


    def draw(self, deck):
        self.cards.append(deck.drawCard())
        return self

    def showCards(self):
        for card in self.cards:
            card.show()

    def check(self, drawn_card):
        for card in self.cards:
            if drawn_card.value == card.value:
                return True

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val


    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,14):
                if v == 11:
                    self.cards.append(Card(s, "Jack"))
                elif v == 12:
                    self.cards.append(Card(s, "Queen"))
                elif v == 13:
                    self.cards.append(Card(s, "King",))
                elif v == 14:
                    self.cards.append(Card(s, "Ace",))
                else:
                    self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()
