import unittest

from card_deck import CardDeck
from game_board import GameBoard

class TestInteractions(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual('test'.upper(), 'TEST')
        
    def test_card_deck_to_card_interaction(self):
        test_card_deck = CardDeck()
        self.assertEqual(len(test_card_deck.cards), 1)
        
    def test_game_board_interactions(self):
        test_game_board = GameBoard(
            num_players = 4,
            player_names = ["p1", "p2", "p3", "p4"]
        )
        
        
if __name__ == '__main__':
    unittest.main()