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
        self.max_index = self.side_length-1
        
        # Due do the nature of this matrix, the coordinate system is accessed
        # by using self.matrix[y][x]
        matrix = [ [ "NONE" for i in range(side_length) ] for j in range(side_length) ] 
        curr_pos = [0, 0]
        # Initialize perimiter
        for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            for edge_counter in range(self.max_index):
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

    def _inverse_dir(self, dir):
        if dir:
            if dir == 'up':
                return 'down'
            if dir == 'down':
                return 'up'
            if dir == 'left':
                return 'right'
            if dir == 'right':
                return 'left'
        else:
            return None

    def _determine_move_dir(self, pos_x: int, pos_y: int, direction: str,
            prev_dir=None
        ):
        # If someone is on a join position between perimiter and spoke...
        if (
            pos_x == self.center_index and (pos_y == 0 or pos_y == self.max_index)
            or
            pos_y == self.center_index and (pos_x == 0 or pos_x == self.max_index)
        ):
            allowed_dirs = ['up', 'down', 'left', 'right']
            if self._inverse_dir(prev_dir) in allowed_dirs:
                allowed_dirs.remove(self._inverse_dir(prev_dir))
            if pos_x == 0 and 'left' in allowed_dirs:
                allowed_dirs.remove('left')
            if pos_y == 0 and 'down' in allowed_dirs:
                allowed_dirs.remove('down')
            if pos_x == self.max_index and 'right' in allowed_dirs:
                allowed_dirs.remove('right')
            if pos_y == self.max_index and 'up' in allowed_dirs:
                allowed_dirs.remove('up')
            dir_str = ", ".join(allowed_dirs)
            usr_msg = 'Pick direction to move from center ('+dir_str+') : '
            dir = input(usr_msg) 
            while dir not in allowed_dirs:
                dir = input(usr_msg)
            return dir
        # If someone is in the center, ask which direction to move in
        if pos_x == self.center_index and pos_y == self.center_index:
            usr_msg = "Pick direction to move from center (up, down, left, right) : "
            dir = input(usr_msg) 
            while dir not in ['up', 'down', 'left', 'right']:
                dir = input(usr_msg)
            return dir
        # If someone is on a vertical spoke, move them along spoke in same dir
        if pos_x == self.center_index and (pos_y > 0 and pos_y < self.max_index):
            print('on vertical')
            # if this is their first move, ask dir
            if prev_dir != None:
                return prev_dir
            else:
                usr_msg = "Pick direction to move along spoke (up, down) : "
                dir = input(usr_msg) 
                while dir not in ['up', 'down']:
                    dir = input(usr_msg)
                return dir
        # If someone is on a horizonal spoke, move them along spoke in same dir
        if pos_y == self.center_index and (pos_x > 0 and pos_x < self.max_index):
            print('on horizonal')
            # if this is their first move, ask dir
            if prev_dir != None:
                return prev_dir
            else:
                usr_msg = "Pick direction to move along spoke (left, right) : "
                dir = input(usr_msg) 
                while dir not in ['left', 'right']:
                    dir = input(usr_msg)
                return dir
        if direction == 'fwd':
            if pos_x == 0 and pos_y != (self.max_index):
                move_dir = 'up'
            elif pos_x == (self.max_index) and pos_y != 0:
                move_dir = 'down'
            elif pos_y == (self.max_index):
                move_dir = 'right'
            elif pos_y == 0:
                move_dir = 'left'
            return move_dir
        if direction == 'rev':
            if pos_x == 0 and pos_y != 0:
                move_dir = 'down'
            elif pos_x == (self.max_index) and pos_y != (self.max_index):
                move_dir = 'up'
            elif pos_y == (self.max_index):
                move_dir = 'left'
            elif pos_y == 0:
                move_dir = 'right'
            return move_dir
        
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
        move_dir = None
        while spaces_moved != spaces_to_move:
            move_dir = self._determine_move_dir(
                end_pos_x, end_pos_y, direction, move_dir
            )
            print(move_dir)
            if move_dir == 'up':
                end_pos_y += 1
            if move_dir == 'down':
                end_pos_y -= 1
            if move_dir == 'left':
                end_pos_x -= 1
            if move_dir == 'right':
                end_pos_x += 1
            spaces_moved += 1
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

