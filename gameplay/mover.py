import logging
import sys
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class mover:
    def __init__(self, mover_color, start_position: int):
        LOG.info("Call to mover")
        self.current_position = start_position
        self.wedges = []  # list of wedge colors that the player has obtained
        self.onSpokes = False
        self.mover_color = mover_color

    # The move method navigates the game positions by the amount delta.  This move might be a simple addition, however,
    # it is possible the next game position is jumping to another index number, like in the case of moving onto a spoke
    # or passing the last game position on a spoke and jumping back to 1.
    def move(self, delta):
        LOG.info("Call to mover.move")
        next_position = self.current_position + delta # this is simplified!! PUT LOGIC HERE FOR JUMPING
        LOG.info("Moving the player's mover from position " + str(self.current_position) + " to " + str(next_position))
        self.current_position = next_position

    def add_wedge(self, color):
        LOG.info("Call to mover.add_wedge")
        LOG.info("Adding wedge")
        if color not in ["red", "blue", "white", "green"]:
            LOG.info("Incorrect color type!")
        self.wedges.append(color)

