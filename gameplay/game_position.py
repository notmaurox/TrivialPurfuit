import logging
import sys

from typing import List
from card import Card

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class GamePosition:
    
    def __init__(self, i, i_next_1, i_next_2=None):
        LOG.info('Created GamePosition with index {}'.format(i))
        self.category = "CATEGORY_TYPE"
        self.location_index = i
        self.next_location_index = [i_next_1, i_next_2]
        self.position_type = "OUTSIDE/SPOKE/CENTER"

class GamePositions:
    
    def __init__(self):
        self.perimeter_len = 50
        self.game_positions = []
        # Inititalize perimeter
        LOG.info("Initialized perimeter positions")
        for pos in range(self.perimeter_len):
            self.game_positions.append(GamePosition(pos, pos+1, None))
            
        # Intitialize internal spokes
        self._initialize_interinal_positions(self.game_positions)
        
    def _initialize_interinal_positions(self, game_positions: List[GamePosition]):
        LOG.info("Initialized internal positions")
