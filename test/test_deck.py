import unittest
from blackjack_classes import Deck, Hand, blackjack_check



class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.deck)
        self.assertEqual(number_of_cards, 52)



if __name__ == '__main__':
    unittest.main()