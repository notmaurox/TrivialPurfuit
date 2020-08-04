import logging
import sys
import copy

from typing import List
from mover import Mover

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.NOTSET)
logging.basicConfig(stream=sys.stdout, level=logging.NOTSET)
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
        self.matrix = [ [ "    " for i in range(side_length) ] for j in range(side_length) ] 
        self._initialize_default_board()
    
    def _initialize_default_board(self):
        red_pos = [
            (0,5), (0,10), (8,10), (10,6), (10, 4), (8, 0), #outer positions
            (4,5), (9,5), (5,3), (5,8) #inner positions
        ]
        blue_pos = [
            (5,0), (0,8), (6,10), (4,10), (10,8), (0,0), #outer positions
            (2,5), (7,5), (5,9), (5,4) #inner positions
        ]
        white_pos = [
            (10,5), (2,0), (0,4), (0,6), (2,10), (10,0), #outer positions
            (1,5), (6,5), (5,7), (5,2) #inner positions
        ]
        green_pos = [
            (5, 10), (10,10), (10,2), (6,0), (4,0), (0,2), #outer positions
            (3,5), (8,5), (5,1), (5,6) #inner positions
        ]
        colored_positions = [
            (red_pos, "REDD"),
            (blue_pos, "BLUE"),
            (white_pos, "WHTE"),
            (green_pos, "GREN")
        ]
        for color_pos, color in colored_positions:
            for pos in color_pos:
                self.matrix[pos[1]][pos[0]] = color
        # add roll again spaces
        curr_pos = [0, 0]
        for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            for edge_counter in range(self.max_index):
                if self.matrix[curr_pos[0]][curr_pos[1]] == "    ":
                    self.matrix[curr_pos[0]][curr_pos[1]] = "R//A"
                curr_pos[0] += direction[0]
                curr_pos[1] += direction[1]
        # add center
        self.matrix[self.center_index][self.center_index] = "CENT"
    
    def _intitialize_dummy_matrix(self):
        curr_pos = [0, 0]
        # Initialize perimiter
        for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            for edge_counter in range(self.max_index):
                self.matrix[curr_pos[0]][curr_pos[1]] = "TYPE"
                curr_pos[0] += direction[0]
                curr_pos[1] += direction[1]
        # Initialize center
        self.matrix[self.center_index][self.center_index] = "CENT"
        # Initizlize vertical spokes
        vert_spoke = [1, self.center_index]
        for spoke_counter in range(self.side_length-2):
            if vert_spoke != [self.center_index, self.center_index]:
                self.matrix[vert_spoke[0]][vert_spoke[1]] = "TYPE"
            vert_spoke[0] += 1
        # Initizlize horizonal spokes
        horiz_spoke = [self.center_index, 1]
        for spoke_counter in range(self.side_length-2):
            if horiz_spoke != [self.center_index, self.center_index]:
                self.matrix[horiz_spoke[0]][horiz_spoke[1]] = "TYPE"
            horiz_spoke[1] += 1
        
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
        direction = 'fwd'  #   TEMP, REMOVE
        end_pos_x = start_pos_x
        end_pos_y = start_pos_y
        spaces_moved = 0
        delta = 1
        move_dir = None
        while spaces_moved != spaces_to_move:
            move_dir = self._determine_move_dir(
                end_pos_x, end_pos_y, direction, move_dir
            )
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
        return self.matrix[pos_y][pos_x]
        
    def render(self, players : List[Mover]):
        to_print = [copy.deepcopy(row) for row in self.matrix]
        for i in range(len(players)):
            player = players[i]
            player_icon = player.mover_color[0].lower()
            pos_label = to_print[player.curr_y_pos][player.curr_x_pos]
            new_label = pos_label[:i] + player_icon + pos_label[i + 1:]
            to_print[player.curr_y_pos][player.curr_x_pos] = new_label
        # Print matrix in reverse order so bottom left cell is (0,0)
        for i in range(1, len(self.matrix)+1):
            print(to_print[len(self.matrix)-i])
            
    def get_headquarter_positions(self):
        return [
            (0, self.center_index),
            (self.center_index, 0),
            (self.max_index, self.center_index),
            (self.center_index, self.max_index)
        ]

if __name__ == "__main__":
    gp = GamePositions()
    p1 = Mover(
        name="player",
        mover_color="BLUE",
        start_pos_x=0,
        start_pos_y=0
    )
    p2 = Mover(
        name="player",
        mover_color="GREEN",
        start_pos_x=0,
        start_pos_y=0
    )
    gp.render([p1,p2])

