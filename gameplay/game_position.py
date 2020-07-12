import logging
import sys

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class GamePosition:
    
    def __init__(self, i, i_next_1, i_next_2=None):
        #LOG.info('Created GamePosition with index {}'.format(i))
        self.category = "CATEGORY_TYPE"
        self.location_index = i
        self.next_location_index = [i_next_1, i_next_2]
        self.position_type = "OUTSIDE/SPOKE/CENTER"

class GamePositions:
    
    def __init__(self):
        self.perimeter_len = 30
        self.internal_spoke_len = 10
        self.game_positions = []
        self.number_of_spokes = 4
        # Initialize perimeter
        LOG.info("Initializing perimeter game positions")
        for pos in range(self.perimeter_len):
            self.game_positions.append(GamePosition(pos+1, pos+2, None))  # avoiding zeroth index

        # Intitialize internal spokes
        LOG.info("Initializing internal spoke game positions")
        for pos in range(self.perimeter_len,
                         self.internal_spoke_len * self.number_of_spokes):  # start counting after the perimeter count
            self.game_positions.append(GamePosition(pos, pos + 1, None))

        # Initialize special cases
        self.game_positions[self.perimeter_len].next_location_index = 1  # wrap perimeter around to start


