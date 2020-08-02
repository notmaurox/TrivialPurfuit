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
        
        # Due do the nature of this matrix, the coordinate system is accessed
        # by using self.matrix[y][x]
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
        # Print matrix in reverse order so bottom left cell is (0,0)
        for i in range(1, len(self.matrix)+1):
            print(self.matrix[len(self.matrix)-i])
            
    def find_next_position(  # I think this needs to include (call to) ask_for_user_path()
        self,
        start_pos_x: int,
        start_pos_y: int,
        spaces_to_move: int,
        direction: str,
    ):
        # Direction can take form fwd or rev where by default the game GameBoard
        # runs clockwise.
        end_pos_x = start_pos_x
        end_pos_y = start_pos_y
        spaces_moved = 0
        delta = 1
        while spaces_moved != spaces_to_move:
            # ask user for direction...
            if end_pos_x == self.center_index and end_pos_y == self.center_index:
                dir = input("Pick direction to move from center (up, down, left, right) : ") 
                while dir not in ['up', 'down', 'left', 'right']:
                    dir = input("Pick direction to move from center (up, down, left, right) : ")
                if dir == 'up':
                    end_pos_y += 1
                elif dir == 'down':
                    end_pos_y -= 1
                elif dir == 'left':
                    end_pos_x -= 1
                elif dir =='right':
                    end_pos_x += 1
                spaces_moved += 1
            # user at join position between perimiter and spoke
            elif end_pos_x == self.center_index or end_pos_y == self.center_index:
                pass 
            # traverse board perimiter
            elif direction == 'fwd':
                if end_pos_x == 0 and end_pos_y != (self.side_length-1):
                    end_pos_y += delta
                elif end_pos_x == (self.side_length-1) and end_pos_y != 0:
                    end_pos_y -= delta
                elif end_pos_y == (self.side_length-1):
                    end_pos_x += delta
                elif end_pos_y == 0:
                    end_pos_x -= delta
                spaces_moved += 1
            
        print('started')
        print(start_pos_x, start_pos_y)
        print('ended')
        print(end_pos_x, end_pos_y)
        
        return end_pos_x, end_pos_y


    def get_position_type(self, pos_x: int, pos_y: int):
        # return "red" "white" "blue" "green"
        pass

if __name__ == "__main__":
    gp = GamePositions()
    x, y = 0, 6
    gp.matrix[y][x] = 'STRT'
    gp.print()
    newx, newy = gp.find_next_position(x, y, 6, 'fwd')
    gp.matrix[newy][newx] = 'ENDD'
    gp.print()

