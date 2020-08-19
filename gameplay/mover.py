import logging
import sys

#from game_position import GamePosition

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.CRITICAL)
logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)

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
        self.mover_color = mover_color  # Right now the mover colors are char of 0,1,2,3.  Should these be changed to 'r','g','b', etc (or 'red','green','blue', etc)??

        mover_offset_constant = 18  # pixel offset to make sure the movers aren't on top of eachother
        if mover_color == "red":
            self.mover_offset_x = mover_offset_constant
            self.mover_offset_y = mover_offset_constant
        elif mover_color == "white":
            self.mover_offset_x = mover_offset_constant
            self.mover_offset_y = -mover_offset_constant
        elif mover_color == "green":
            self.mover_offset_x = -mover_offset_constant
            self.mover_offset_y = mover_offset_constant
        elif mover_color == "blue":
            self.mover_offset_x = -mover_offset_constant
            self.mover_offset_y = -mover_offset_constant


    def update_pos(self, new_x: int, new_y: int):
        LOG.info("Call to mover.move")
        LOG.info("Moving the player's mover to position "+str(new_x)+","+str(new_y))
        self.curr_x_pos = new_x
        self.curr_y_pos = new_y
        
    def get_pos(self):
        return self.curr_x_pos, self.curr_y_pos
        
    def is_full(self):
        expected_wedges = ["red", "blue", "white", "green"]
        for wedge in expected_wedges:
            if wedge not in self.wedges:
                return False
        return True
                
    def add_wedge(self, color):
        LOG.info("Call to mover.add_wedge")
        LOG.info("Adding wedge")
        expected_wedges = ["red", "blue", "white", "green"]
        print("Checking if wedge of color:", color, "is in", expected_wedges)
        if color not in expected_wedges:
            LOG.info("Incorrect color type!")
            quit()
        if color not in self.wedges:
            self.wedges.append(color)
            print("Player earned a", color, "wedge!")
        for wedge in expected_wedges:
            if wedge not in self.wedges:
                return False
        return True

    def render(self):
        # Tie into the gui here using the following inputs FOR TARGET INCREMENT
        #self.curr_x_pos
        #self.curr_y_pos
        pass

