from PIL import Image as im, ImageTk
from tkinter import Tk, Label, Canvas

class GameBoardGUI:

    def __init__(self):
        self.win_x = 1331
        self.win_y = 900

        self.window = Tk()

        self.load = im.open('game_board.jpg')
        self.photoImage = ImageTk.PhotoImage(self.load)
        #self.window.update()

    def render(self, players, pixel_to_position_scaling_factor, pixel_to_position_offset):
        # Draw board (stationary)
        self.window.title("Trivial Purfuit")
        self.window.configure(background='black')
        self.canvas = Canvas(self.window, width=self.win_x, height=self.win_y)

        #self.canvas.pack() # this might be redundant with w.grid()

        self.canvas.create_image(self.win_x/2, self.win_y/2+100, image=self.photoImage)
        self.canvas.grid()

        # make buttons, text (should it be here or in init?)

        # Draw movers
        self.draw_movers(players,
                             pixel_to_position_scaling_factor,
                             pixel_to_position_offset)

        #self.window.mainloop()  # not sure where this lives.  Here?
        self.window.update()


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

        self.canvas.create_oval(
                pixel_to_position_offset[0] + mover.curr_x_pos * pixel_to_position_scaling_factor,
                pixel_to_position_offset[1] + mover.curr_y_pos * pixel_to_position_scaling_factor,
                pixel_to_position_offset[0] + mover.curr_x_pos * pixel_to_position_scaling_factor + 40,
                pixel_to_position_offset[1] + mover.curr_y_pos * pixel_to_position_scaling_factor + 40,
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
                pixel_to_position_offset[1] + mover.curr_y_pos * pixel_to_position_scaling_factor,
                pixel_to_position_offset[0] + mover.curr_x_pos * pixel_to_position_scaling_factor + 40,
                pixel_to_position_offset[1] + mover.curr_y_pos * pixel_to_position_scaling_factor + 40,
                start=start,
                extent=90,
                outline=mover.mover_color,
                fill=wedge,
                width=2)



