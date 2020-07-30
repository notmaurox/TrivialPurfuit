import logging
import sys

from game_position import GamePosition

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Mover:
    def __init__(
        self, name: str, mover_color: str, start_pos_x: int, start_pos_y: int
    ):
        LOG.info("Call to mover.__init")
        self.name = name
        self.mover_color = mover_color
        self.curr_x_pos = start_pos_x
        self.curr_y_pos = start_pos_y
        self.wedges = []  # list of wedge colors that the player has obtained
        self.on_spokes = False
        self.mover_color

    def update_pos(self, new_x: int, new_y: int):
        LOG.info("Call to mover.move")
        LOG.info("Moving the player's mover to position "+str(new_x)+","+str(new_y))
        self.curr_x_pos = new_x
        self.curr_y_pos = new_y
        
    def get_pos(self):
        return self.curr_x_pos, self.curr_y_pos

    def add_wedge(self, color):
        LOG.info("Call to mover.add_wedge")
        LOG.info("Adding wedge")
        if color not in ["red", "blue", "white", "green"]:
            LOG.info("Incorrect color type!")
        self.wedges.append(color)

