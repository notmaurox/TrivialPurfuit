from dice import Die
#from players import Players
#from card_deck import CardDecks
from mover import Mover
from card_deck import CardDeck
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
        
        #self.card_decks = CardDecks()
        self.red_deck = CardDeck("Events")              # Are these the right color to category mappings?  If we want to stick with colors, that's fine
        self.white_deck = CardDeck("Independence Day")
        self.blue_deck = CardDeck("People")
        self.green_deck = CardDeck("Places")

        self.die = Die(num_sides=6)    
        self.game_positions = GamePositions()
                
        self.players = []
        self.current_player = None # It might be useful to have this property to easily access the player whose turn it is
        self.direction = ""  # The direction the player has chosen to move (not yet sure what values this can take)

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
        while True:
            for player in self.players:
                self.take_turn(player)


    def ask_user_direction(self, message):
        userInput = 0
        while userInput not in range(1,3):
            userInput = int(input(message))
        self.direction = userInput
        
    def present_die(self):
        input("Press Enter to roll the die.\n")  # This isn't working right, just have to look up the usage
        value = self.die.roll()
        print("Die face value: ", value)
        return value

    def take_turn(self, current_player: Mover):
        self.set_current_player(current_player)
        rolledNumber = self.present_die()
        self.ask_user_direction()
        newPosition = self.game_positions.find_next_position(
                                                    current_player.get_pos(),
                                                    rolledNumber,
                                                    self.direction
                                           )
        current_player.update_pos(newPosition)
        type = self.game_positions.get_position_type(current_player.get_pos())
        card = self.draw_card_by_type(type)
        self.display_question(card)
        self.display_answer(card)
        self.current_player.add_wedge(type)  # logic either needs to sit here to only add a wedge if it is isn't already owned OR let the mover worry about that (latter seems better)
        self.report_end_of_game()  # should be a conditional
        self.report_end_of_turn()
        return

    def display_question(self, card):
        print(card.question)
        
    def ask_user_answer(self):
        input("Press Enter to see the answer.\n")


    def report_end_of_turn(self):
        input(self.current_player + ", your turn is now over.  Press Enter to finish.")

    def report_end_of_game(self, winner):
        input(winner + " has won the game!  Press Enter to finish.")
        self.end_game()  # this call might better live outside of this method, like in the calling method (presumably the main gameplay loop)

    def display_answer(self, card):
        print(card.answer)
        val = input("Did " + self.current_player.name + " answer the question correctly? [y/n]\n")
        if val == "y":
            return 1
        elif val == "n":
            return 0
        else:
            print("Invalid input. Please enter y or n")
            return self.display_answer(card) # this is recursive.  consider changing

        
    def draw_board(self):  # for target increment
        pass

    def set_current_player(self, player):
        self.current_player = player

    def end_game(self): # kick off the sequence of ending the game (proclaim the winner, etc)
        pass

    def draw_card_by_type(self, type):  # Move this logic to game board
        if type == "red":
            return self.get_red_card()
        if type == "white":
            return self.get_white_card()
        if type == "blue":
            return self.get_blue_card()
        if type == "green":
            return self.get_green_card()
