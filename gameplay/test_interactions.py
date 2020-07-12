import unittest

from card_deck import CardDeck

class TestInteractions(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual('test'.upper(), 'TEST')
        
    def test_card_deck_to_card_interaction(self):
        test_card_deck = CardDeck()
        self.assertEqual(len(test_card_deck.cards), 1)
        
if __name__ == '__main__':
    unittest.main()