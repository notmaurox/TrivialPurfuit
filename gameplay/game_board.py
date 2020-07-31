from dice import Die
#from players import Players
from card_deck import CardDecks
from mover import Mover
#from card_deck import CardDeck
import time
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
        
        self.card_decks = CardDecks()

        self.die = Die(num_sides=6)    
        self.game_positions = GamePositions()
                
        self.players = []
        self.current_player = None # It might be useful to have this property to easily access the player whose turn it is
        
        for player_num in range(0, num_players):
            self.players.append(
                Mover(
                    name=player_names[player_num],
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
        
    def present_die(self):
        input("Press Enter to roll the die.\n")  # This isn't working right, just have to look up the usage
        value = self.die.roll()
        print("Die face value: ", value)

    def take_turn(self, current_player: Mover):
        self.set_current_player(current_player)
        
    def display_question(self, card):
        print(card.question)

        
    def display_answer(self, card):
        print(card.answer)
        val = input("Did " + self.current_player.name + " answer the question correctly? [y/n]\n")
        if val == "y":
            return 1
        elif val == "n":
            return 0
        else:
            print("Invalid input. Please enter y or n")
            return self.display_answer()

        
    def draw_board(self):  # for target increment
        pass

    def set_current_player(self, player):
        self.current_player = player

        