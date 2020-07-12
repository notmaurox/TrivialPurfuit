import unittest

from start_game import GameStarter

class GameStarterInteractions(unittest.TestCase):
    
    def test_game_starter_start_game(self):
        print("test_game_starter_start_game")
        game_starter = GameStarter()
        
        game_starter.start_game(
            num_players = 4,
            player_names = ["p1", "p2", "p3", "p4"]
        )
        
    def test_game_starter_view_questions(self):
        print("test_game_starter_view_questions")
        game_starter = GameStarter()
        
        game_starter.view_questions()