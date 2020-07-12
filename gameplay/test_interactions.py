import unittest

from card_deck import CardDeck
from game_board import GameBoard
from dice import Die

class TestInteractions(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual('test'.upper(), 'TEST')
        
    def test_card_deck_to_card_interaction(self):
        print("Testing")
        test_card_deck = CardDeck()
        self.assertEqual(len(test_card_deck.cards), 25)
        
    def test_game_board_interactions(self):
        print(r"Creating gameboard.  Players: 4, names: p1, p2, p3, p4")
        test_game_board = GameBoard(
            num_players =4,
            player_names=["p1", "p2", "p3", "p4"]
        )
        print("Testing that four players were created")
        self.assertEqual(len(test_game_board.players.players), 4)
        print("Testing that the dice has 6 sides")
        self.assertEqual(test_game_board.die.num_sides, 6)
        print("Testing that the card decks have 25 in each category")
        self.assertEqual(len(test_game_board.card_decks.blue_deck.cards), 25)
        self.assertEqual(len(test_game_board.card_decks.white_deck.cards), 25)
        self.assertEqual(len(test_game_board.card_decks.red_deck.cards), 25)
        self.assertEqual(len(test_game_board.card_decks.green_deck.cards), 25)



    def test_die(self):
        print("Testing a six-sided die by creating and rolling.  The result must be between 1 and 6 (inclusive).")
        die = Die(6)
        face_value = die.roll()
        self.assertGreaterEqual(face_value,0)
        self.assertLessEqual(face_value, 6)

if __name__ == '__main__':
    unittest.main()