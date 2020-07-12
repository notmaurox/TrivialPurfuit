import unittest

from card_deck import CardDeck
from game_board import GameBoard
from dice import Die
from players import Players
from game_position import GamePosition

class TestInteractions(unittest.TestCase):

    def test_game_position(self):
        # Create a game position, assign it a category of History, index of 14, and link it with positions 15 and 61
        game_position = GamePosition(14, 15, 61)
        game_position.category = "History"
        game_position.position_type = "OUTSIDE"
        print("Testing game positions attributes")
        self.assertEqual(game_position.category, "History")
        self.assertEqual(game_position.next_location_index, [15, 61])
        
    def test_card_deck_to_card_interaction(self):
        # Create a single deck of cards of length 25
        print("Testing the card deck.")
        test_card_deck = CardDeck()
        self.assertEqual(len(test_card_deck.cards), 25)

    def test_player_movement(self):
        # Create a player and mover, and move its mover 10 spaces
        players = Players()
        players.add_player("Test Player", "green", 10)
        print("Player's mover should start at 10 and end at 20")
        players.players[0].mover.move(10)
        self.assertEqual(players.players[0].mover.current_position, 20)

    def test_game_board_interactions(self):
        # Create a gameboard with 4 players, 1 die of six sides, and card decks 4 card decks of 25 cards each
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
        self.assertGreater(face_value, 0)
        self.assertLessEqual(face_value, 6)

if __name__ == '__main__':
    unittest.main()