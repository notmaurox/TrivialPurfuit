import logging
import sys

#from game_position import GamePosition

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
        self.mover_color = mover_color

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
        expected_wedges = ["red", "blue", "white", "green"]
        if color not in expected_wedges:
            LOG.info("Incorrect color type!")
        if color not in self.wedges:
            self.wedges.append(color)
        for wedge in expected_wedges:
            if wedge not in self.wedges:
                return False
        return True

    def render(self):
        # Tie into the gui here using the following inputs FOR TARGET INCREMENT
        #self.curr_x_pos
        #self.curr_y_pos
        pass

