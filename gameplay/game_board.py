from dice import Die
#from players import Players
#from card_deck import CardDecks
from mover import Mover
from card_deck import CardDeck
from card import Card
import time
from typing import List
from game_position import GamePositions
import logging
import sys

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

GAME_POSITION_TYPE_MAP = {
    "REDD": "red",
    "WHTE": "white",
    "BLUE": "blue",
    "GREN": "green",
    "R//A": "roll_again",
    "CENT": "center"
}


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
                    mover_color=str(player_num),
                    start_pos_x=0,
                    start_pos_y=0
                )
            )

        
    def main_gameplay_loop(self):
        while True:
            for player in self.players:
                self.take_turn(player)
                self.game_positions.render(self.players)
                


    def ask_user_direction(self):
        userInput = 0
        message = "pick direction to move across board (fwd/rev)"
        while userInput not in ['fwd', 'rev']:
            userInput = input(message)
        return userInput
        
    def present_die(self):
        input("Press Enter to roll the die.\n")  # This isn't working right, just have to look up the usage
        value = self.die.roll()
        print("Die face value: ", value)
        return value

    def take_turn(self, current_player: Mover):
        self.set_current_player(current_player)
        type = 'roll_again'
        answered_correct = False
        while type == 'roll_again' or answered_correct:
            self.game_positions.render(self.players)
            rolledNumber = self.present_die()
            direction = self.ask_user_direction()
            new_x_pos, new_y_pos = self.game_positions.find_next_position(
                current_player.get_pos()[0],
                current_player.get_pos()[1],
                rolledNumber,
                direction
            )
            current_player.update_pos(new_x_pos, new_y_pos)
            # Currently game_positions stores types of positions as 4 character stings
            gp_type = self.game_positions.get_position_type(new_x_pos, new_y_pos)
            # Mapp 4 character game_positions to game_board position type
            type = GAME_POSITION_TYPE_MAP[gp_type]
            if type != 'roll_again':
                card = self.MINIMAL_INCREMENT_draw_card_by_type(type)
                self.display_question(card)
                self.ask_user_answer()
                answered_correct = self.display_answer(card)
                # logic either needs to sit here to only add a wedge if it is isn't already owned OR let the mover worry about that (latter seems better)
                if (new_x_pos, new_y_pos) in self.game_positions.get_headquarter_positions():
                    is_full = self.current_player.add_wedge(type)
                    if is_full:
                        self.report_end_of_game()  # should be a conditional
        self.report_end_of_turn()
        return

    def display_question(self, card):
        print(card.question)
        
    def ask_user_answer(self):
        input("Press Enter to see the answer.\n")

    def report_end_of_turn(self):
        input(self.current_player.name + ", your turn is now over.  Press Enter to finish.")

    def report_end_of_game(self, winner):
        input(winner + " has won the game!  Press Enter to finish.")
        self.end_game()  # this call might better live outside of this method, like in the calling method (presumably the main gameplay loop)

    def display_answer(self, card):
        print(card.answer)
        val = input("Did " + self.current_player.name + " answer the question correctly? [y/n]\n")
        while val not in ['y', 'n']:
            val = input("Did " + self.current_player.name + " answer the question correctly? [y/n]\n")
        if val == 'y':
            return True
        if val == 'n':
            return False

        
    def draw_board(self):  # for target increment
        pass

    def set_current_player(self, player):
        print('It is '+player.name+'\'s turn!')
        self.current_player = player

    def end_game(self): # kick off the sequence of ending the game (proclaim the winner, etc)
        exit

    def MINIMAL_INCREMENT_draw_card_by_type(self, type):
        return Card(
            "place_holder_type",
            "place_holder_question",
            "place_holder_answer",
            "easiest"
        )

    def draw_card_by_type(self, type):  # Move this logic to game board
        if type == "red":
            return self.red_deck.deal_card()
        if type == "white":
            return self.white_deck.deal_card()
        if type == "blue":
            return self.blue_deck.deal_card()
        if type == "green":
            return self.green_deck.deal_card()
            
if __name__ == "__main__":
    gb = GameBoard(4, ['r', 'w', 'g', 'b'])
    gb.main_gameplay_loop()
