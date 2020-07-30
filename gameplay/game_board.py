from dice import Die
from players import Players
from card_deck import CardDecks
from mover import Mover

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
        
        self.red_deck = CardDeck()
        self.white_deck = CardDeck()
        self.blue_deck = CardDeck()
        self.green_deck = CardDeck()
        self.die = Die(num_sides=6)    
        self.game_positions = GamePositions()
                
        self.players = []
        
        for player_num in range(0, num_players):
            self.players.append(
                Mover(
                    name=name,
                    mover_color="COLOR",
                    start_pos_x=0,
                    start_pos_y=0
                )
            )

        
    def main_gameplay_loop(self):
        # while True
        #   for player in Players
        #    take_turn(player)
        #       if game over
        #          return
        pass
        
    def present_die(self, current_player: )
        
    def take_turn(self, current_player: Player):
        pass
        
    def display_question(self):
        pass
        
    def display_answer(self):
        pass
        
    def draw_board(self):
        pass
            
        