import random


# class Card:  # a class to represent a card, with suit and value
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value
#
#     def view_card(self):  # a function to view a card
#         print('{} of {}'.format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.deck = []
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for val in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                self.deck.append('{} of {}'.format(val, suit))
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def add_card(self, card):
        self.deck.append(card)


class Hand(Deck):
    def __init__(self, label):
        super().__init__()
        self.deck = []
        self.label = label
        self.score = 0

    def __str__(self):  # a function to view the hand
        return self.label + ' || ' + ' || '.join(self.deck) + ' || '

    def add_score(self):
        self.score = 0
        for card in self.deck:
            if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                self.score += 10
            elif card[0] == 'A':
                if 'Player' in self.label:
                    ace_val = input('Ace is 1 or 11?: ')
                    self.score += int(ace_val)
                else:
                    self.score += 11
            else:
                self.score += int(card[:2])

    def show_score(self):
        print('{} Hand: {} points'.format(self.label, self.score))

    def show_dealer_hand(self):
        print('Dealer Hand:   {}      ??   \n'.format(self.deck[0]))



