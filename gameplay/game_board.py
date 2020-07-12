from dice import Die
from players import Players
from card_deck import CardDecks
from typing import List
from game_position import GamePositions

class GameBoard:
    
    def __init__(self, num_players: int, player_names: List[str]):
        self.players = Players()
        self.card_decks = CardDecks()
        self.die = Die(num_sides=6)

        for player_num in range(0, num_players):
            self.players.add_player(player_names[player_num], "blue", 0)
            
        self.game_positions = GamePositions()
            
        