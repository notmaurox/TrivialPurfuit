from dice import Die
from players import Players
from card_deck import CardDecks
from typing import List
from game_position import GamePositions
import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class GameBoard:
    
    def __init__(self, num_players: int, player_names: List[str]):
        LOG.info("Call to GameBoard.__init__")
        self.players = Players()
        self.card_decks = CardDecks()
        self.die = Die(num_sides=6)

        for player_num in range(0, num_players):
            self.players.add_player(player_names[player_num], "blue", 0)
            
        self.game_positions = GamePositions()
        
    def main_gameplay_loop(self):
        # while True
        #   for player in Players
        #    take_turn(player)
        #       if game over
        #          return
        pass
        
    def take_turn(self, current_player : Player):
        pass
        
    def display_question(self):
        pass
        
    def display_answer(self):
        pass
        
    def draw_board(self)
        pass
            
        