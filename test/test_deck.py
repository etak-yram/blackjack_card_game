import unittest
from blackjack_classes import Deck, Hand, Card



class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.deck)
        self.assertEqual(number_of_cards, 52)

    def test_shuffle_deck(self):
        pass

    def test_deal_card(self):
        pass

    def test_add_card(self):
        pass


class CardTestCase(unittest.TestCase):

    def setUp(self):
        self.card = Card()

    def tearDown(self):
        pass

    def test_view_card(self):
        pass


class HandTestCase(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()

    def test_add_score(self):
        pass

    def test_show_score(self):
        pass



if __name__ == '__main__':
    unittest.main()