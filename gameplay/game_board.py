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
import random
from game_board_gui import GameBoardGUI

from PIL import Image as im, ImageTk
from tkinter import Tk, Label, Canvas, Button, IntVar

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.CRITICAL)
logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)

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

        self.red_deck = CardDeck("People")              # Are these the right color to category mappings?  If we want to stick with colors, that's fine
        self.white_deck = CardDeck("Events")
        self.blue_deck = CardDeck("Places")
        self.green_deck = CardDeck("Independence Day")

        self.die = Die(num_sides=6)
        self.game_positions = GamePositions()

        self.players = []
        self.current_player = None # It might be useful to have this property to easily access the player whose turn it is
        self.direction = ""  # The direction the player has chosen to move (not yet sure what values this can take)

        self.pixel_to_position_scaling_factor = 75  # Multiple a game_position location (in matrix) by this number to get the pixel location equivalent
        self.pixel_to_position_offset = (24, 24)  # add these x and y values to the scaled pixel location to get starting square (since it isn't in top left corner)

        colors = ['red', 'white', 'blue', 'green']
        for player_num in range(0, num_players):
            self.players.append(
                Mover(
                    name=player_names[player_num],
                    mover_color=colors[player_num],
                    start_pos_x=0,
                    start_pos_y=0
                )
            )

        #self.GUI = GameBoardGUI()
        #self.GUI.render(
        #           self,
        #           self.players,
        #           self.pixel_to_position_scaling_factor,
        #           self.pixel_to_position_offset
        #           )


    def main_gameplay_loop_GUI(self):
        self.win_x = 829
        self.win_y = 830
        self.window = Tk()

        self.load = im.open('game_board.jpg')
        self.photoImage = ImageTk.PhotoImage(self.load)

        # Draw board (stationary)
        self.window.title("Trivial Purfuit")
        self.window.configure(background='black')
        self.canvas = Canvas(self.window, width=self.win_x, height=self.win_y)

        self.canvas.create_image(self.win_x / 2, self.win_y / 2, image=self.photoImage)
        self.canvas.grid()

        # make label
        self.label = Label(self.window, text="",)
        self.label.grid(row=1, column=0)
        self.set_current_player(self.players[0])

        # make buttons
        b = Button(self.window, text="Roll Die", command=self.present_die_GUI)
        b.grid(row=3, column=0)

        b = Button(self.window, text="Clockwise", command=self.set_start_direction_fwd)
        b.grid(row=4, column=0, sticky='E')
        b = Button(self.window, text="Counter-clockwise", command=self.set_start_direction_rev)
        b.grid(row=4, column=0, sticky='W')

        b = Button(self.window, text="See Answer", command=self.display_answer)
        b.grid(row=5, column=0)

        b = Button(self.window, text="Correct", command=self.answered_correct)
        b.grid(row=6, column=0, sticky='E')
        b = Button(self.window, text="Incorrect", command=self.answered_incorrect)
        b.grid(row=6, column=0, sticky='W')


        # update label
        self.set_label_text(self.current_player.mover_color + " player's turn. Roll the die and select a direction to move!")
        # Draw movers
        self.draw_movers(self.players,
                         self.pixel_to_position_scaling_factor,
                         self.pixel_to_position_offset)

        self.window.mainloop()  # not sure where this lives.  Here?

    def answered_correct(self):
        if (self.new_x_pos, self.new_y_pos) in self.game_positions.get_headquarter_positions():
            board_type = self.game_positions.get_position_type(
                self.new_x_pos, self.new_y_pos
            )
            real_type = GAME_POSITION_TYPE_MAP[board_type]
            is_full = self.current_player.add_wedge(real_type)
            if is_full:
                self.report_end_of_game()  # should be a conditional
        self.set_label_text(self.current_player.mover_color + ' player can roll again.')

    def answered_incorrect(self):
        self.report_end_of_turn()

    def set_start_direction_fwd(self):
        print('Player will move clockwise')
        self.set_label_text('Player will move clockwise')
        self.game_positions.start_direction = "fwd"
        self.move_player()

    def set_start_direction_rev(self):
        print('Player will move counter-clockwise')
        self.set_label_text('Player will move counter-clockwise')
        self.game_positions.start_direction = "rev"
        self.move_player()

    def move_player(self):
        self.new_x_pos, self.new_y_pos = self.game_positions.find_next_position(
            self.current_player.get_pos()[0],
            self.current_player.get_pos()[1],
            self.die.last_roll,
            self.players,
            self.window,
        )

        self.current_player.update_pos(self.new_x_pos, self.new_y_pos)
        self.draw_movers(self.players,
                         self.pixel_to_position_scaling_factor,
                         self.pixel_to_position_offset)

        gp_type = self.game_positions.get_position_type(self.new_x_pos, self.new_y_pos)
        # Mapp 4 character game_positions to game_board position type
        type = GAME_POSITION_TYPE_MAP[gp_type]
        print(type)
        if type == 'center':
            colors = ['red', 'white', 'blue', 'green']
            n = len(colors) - 1
            i = random.randint(0, n)
            type = colors[i]

        if type != 'roll_again':
            self.card = self.draw_card_by_type(type)
            # card = self.MINIMAL_INCREMENT_draw_card_by_type(type)
            self.game_positions.render(self.players)
            self.display_question(self.card)
            ## break this method here, following code goes to new button
        '''


            self.ask_user_answer()
            answered_correct = self.display_answer(card)
            if (new_x_pos, new_y_pos) in self.game_positions.get_headquarter_positions():
                is_full = self.current_player.add_wedge(type)
                if is_full:
                    self.report_end_of_game()  # should be a conditional

        self.report_end_of_turn()
        '''





    def set_label_text(self, text):
        # make label
        self.label['text'] = text


    def main_gameplay_loop(self):
        while True:
            for player in self.players:
                # I think this should be where the gui is incorporated
                self.take_turn(player)
                self.game_positions.render(self.players)
                self.GUI.render(
                    self.players,
                    self.pixel_to_position_scaling_factor,
                    self.pixel_to_position_offset
                )


    def present_die(self):
        roll_amount = input("Press Enter to roll the die. Type quit to exit game.")
        if roll_amount == 'quit':
            exit()
        else:
            value = self.die.roll()
            print("Die face value: ", value)
            return value

    def present_die_GUI(self):
        value = self.die.roll()
        self.set_label_text("Die face value: " + str(value))
        print("Die face value: ", value)

        return value


    def take_turn(self, current_player: Mover):
        self.set_current_player(current_player)
        type = 'roll_again'
        answered_correct = False
        while type == 'roll_again' or answered_correct:
            self.game_positions.render(self.players)
            val = self.present_die()
            new_x_pos, new_y_pos = self.game_positions.find_next_position(
                current_player.get_pos()[0],
                current_player.get_pos()[1],
                val,
                self.players
            )
            current_player.update_pos(new_x_pos, new_y_pos)
            # Currently game_positions stores types of positions as 4 character stings
            gp_type = self.game_positions.get_position_type(new_x_pos, new_y_pos)
            # Mapp 4 character game_positions to game_board position type
            type = GAME_POSITION_TYPE_MAP[gp_type]
            if type == 'center':
                colors = ['red', 'white', 'blue', 'green']
                n = len(colors) - 1
                i = random.randint(0, n)
                type = colors[i]

            if type != 'roll_again':
                card = self.draw_card_by_type(type)
                #card = self.MINIMAL_INCREMENT_draw_card_by_type(type)
                self.game_positions.render(self.players)
                self.display_question(card)
                #self.display_answer()
                answered_correct = self.display_answer(card)
                ### break button function here
                if (new_x_pos, new_y_pos) in self.game_positions.get_headquarter_positions():
                    board_type = self.game_positions.get_position_type(new_x_pos, new_y_pos)
                    real_type = GAME_POSITION_TYPE_MAP[board_type]
                    is_full = self.current_player.add_wedge(real_type)
                    if is_full:
                        self.report_end_of_game()  # should be a conditional

        self.report_end_of_turn()
        return

    def display_question(self, card):
        self.set_label_text(card.type + " question: " + card.question + "\n Press 'See Answer' when ready.")
        print(card.type, "question:", card.question)


    def ask_user_answer(self):

        pass
        # Ask user to press correct or incorrect button (enter logic to enable these buttons here)
        #input("Press Enter to see the answer.")

    def report_end_of_turn(self):
        self.set_label_text(self.current_player.name + ", your turn is now over.  Press Enter to finish.")
        input(self.current_player.name + ", your turn is now over.  Press Enter to finish.")

    def report_end_of_game(self, winner):
        input(winner + " has won the game!  Press Enter to finish.")
        self.end_game()  # this call might better live outside of this method, like in the calling method (presumably the main gameplay loop)

    def display_answer(self):

        print("Answer:", self.card.answer)
        self.set_label_text("Answer: " + self.card.answer + " \n Did the player answer the question correctly? Press either 'correct' or 'incorrect'")

        '''
        val = input("Did " + self.current_player.name + " answer the question correctly? [y/n]\n")
        while val not in ['y', 'n']:
            val = input("Did " + self.current_player.name + " answer the question correctly? [y/n]\n")
        if val == 'y':
            return True
        if val == 'n':
            return False
        '''

    def set_current_player(self, player):
        self.set_label_text('It is '+player.name+'\'s turn!')
        #print('It is '+player.name+'\'s turn!')
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


    def draw_movers(self, players, pixel_to_position_scaling_factor: float,
                   pixel_to_position_offset: tuple ):
        for player in players:
            self.draw_mover(player,
                   pixel_to_position_scaling_factor,
                   pixel_to_position_offset)
        #self.window.update()


    def draw_mover(self, mover,
                   pixel_to_position_scaling_factor: float,
                   pixel_to_position_offset: tuple):

        mover_size = 33

        self.canvas.create_oval(
                pixel_to_position_offset[0] + mover.mover_offset_x + mover.curr_x_pos * pixel_to_position_scaling_factor,
                self.win_y - (pixel_to_position_offset[1] + mover.mover_offset_y  + mover.curr_y_pos * pixel_to_position_scaling_factor),
                pixel_to_position_offset[0] + mover.mover_offset_x  + mover.curr_x_pos * pixel_to_position_scaling_factor + mover_size,
                self.win_y - (pixel_to_position_offset[1] + mover.mover_offset_y + mover.curr_y_pos * pixel_to_position_scaling_factor + mover_size),
                outline=mover.mover_color,
                fill='grey',
                width=2)

        for wedge in mover.wedges:
            if wedge == "red":
                start = 0
            elif wedge == "yellow":
                start = 90
            elif wedge == "green":
                start = 180
            elif wedge == "blue":
                start = 270

            self.canvas.create_arc(
                pixel_to_position_offset[0] + mover.curr_x_pos * pixel_to_position_scaling_factor,
                self.win_y - (pixel_to_position_offset[1] + mover.curr_y_pos * pixel_to_position_scaling_factor),
                pixel_to_position_offset[0] + mover.curr_x_pos * pixel_to_position_scaling_factor + mover_size,
                self.win_y - (pixel_to_position_offset[1] + mover.curr_y_pos * pixel_to_position_scaling_factor + mover_size),
                start=start,
                extent=90,
                outline=mover.mover_color,
                fill=wedge,
                width=2)






if __name__ == "__main__":
    gb = GameBoard(4, ['r', 'w', 'g', 'b'])
    #gb.main_gameplay_loop()
    gb.main_gameplay_loop_GUI()
