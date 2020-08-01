import logging
import sys

from typing import List

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG.info("Call to game_position")

class GamePositions:
    def __init__(self, side_length=11):
        LOG.info("Call to GamePosition.__init__")
        self.side_length = side_length
        self.center_index = int((side_length-1)/2)
        self.total_perimeter = (side_length*4)-4
        
        matrix = [ [ "NONE" for i in range(side_length) ] for j in range(side_length) ] 
        curr_pos = [0, 0]
        # Initialize perimiter
        for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            for edge_counter in range(self.side_length-1):
                matrix[curr_pos[0]][curr_pos[1]] = "TYPE"
                curr_pos[0] += direction[0]
                curr_pos[1] += direction[1]
        # Initialize center
        matrix[self.center_index][self.center_index] = "CENT"
        # Initizlize vertical spokes
        vert_spoke = [1, self.center_index]
        for spoke_counter in range(self.side_length-2):
            if vert_spoke != [self.center_index, self.center_index]:
                matrix[vert_spoke[0]][vert_spoke[1]] = "SPOK"
            vert_spoke[0] += 1
        # Initizlize horizonal spokes
        horiz_spoke = [self.center_index, 1]
        for spoke_counter in range(self.side_length-2):
            if horiz_spoke != [self.center_index, self.center_index]:
                matrix[horiz_spoke[0]][horiz_spoke[1]] = "SPOK"
            horiz_spoke[1] += 1
            
        self.matrix = matrix
        
    def print(self):
        for row in self.matrix:
            print(row)
            
    def find_next_position(  # I think this needs to include (call to) ask_for_user_path()
        self,
        start_pos_x: int,
        start_pos_y: int,
        spaces_to_move: int,
        direction: str,
    ):
        pass
        return #return user's new position


    def get_position_type(self, pos_x: int, pos_y: int):
        # return "red" "white" "blue" "green"
        pass

if __name__ == "__main__":
    GamePositions().print()

