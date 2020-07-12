import logging

from card import Card

LOG = logging.getLogger(__name__)

class GamePositions:
    
    def __init__(self):
        self.perimeter_len = 50
        self.game_positions = []
        # Inititalize perimeter
        LOG.info("Initialized perimeter positions")
        for pos in range(self.perimeter_len):
            self.game_positions.append(GamePositions(pos,i+1))
            
        # Intitialize internal spokes
        self._initialize_interinal_positions(self.game_positions)
        
    def _initialize_interinal_positions(self, game_positions: List[GamePositions]):
        LOG.info("Initialized internal positions")
        
class GamePosition:
    
    def __init__(self, i, i_next_1, i_next_2=None):
        LOG.info(f'Created GamePosition with index {i}')
        self.category = "CATEGORY_TYPE"
        self.location_index = i
        self.next_location_index = [i_next_1, i_next_2]
        self.position_type = 