# 카드 뽑기 게임 구현 - 상속 없이 구현
from random import shuffle, randint

class Deck:
    def __init__(self):
        self.suites = ['Hearts', 'Diamonds', 'Clover', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.mycardset = []

        for s in self.suites:
            for v in self.values:
                self.mycardset.append(v + ' of ' + s)

    def shufflesDeck(self):
        if len(self.mycardset) < 52:
            print("Cannot shuffle the deck")
            return
        shuffle(self.mycardset)
        return self

    def popCard(self):
        if len(self.mycardset) == 0:
            print("NO CARDS CAN BE POPPED FURTHER")
            return
        return self.mycardset.pop(randint(0, len(self.mycardset)-1))

class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.cards = []

    def __str__(self):
        return "Player " + self.nickname + " has "+ str(self.cards)

    def add_card(self, card):
        self.cards.append(card)

if __name__ == "__main__":
    deck = Deck()

    print(f'[Current Deck]\n{deck.mycardset}\n')

    shuffled_deck = deck.shufflesDeck()

    print(f'[Shuffled Deck]\n{shuffled_deck.mycardset}\n]')

    player1 = Player('Gil Dong')
    player2 = Player('Chul Su')

    for _ in range(4):
        player1.add_card(shuffled_deck.popCard())
        player2.add_card(shuffled_deck.popCard())

    print(f'{player1}')
    print(f'{player2}')