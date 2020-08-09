import unittest

import game_position

class TestGamePositions(unittest.TestCase):
    def setUp(self):
        # Default board is 11x11
        self.gp = game_position.GamePositions()
        
    def test_move_bottom_left_corner_fwd(self):
        start_x, start_y = 4, 0
        spaces_to_move = 6
        expected_end_x = 0
        expected_end_y = 2
        direction = 'fwd'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_top_left_corner_fwd(self):
        start_x, start_y = 0, 7
        spaces_to_move = 4
        expected_end_x = 1
        expected_end_y = 10
        direction = 'fwd'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_top_right_corner_fwd(self):
        start_x, start_y = 7, 10
        spaces_to_move = 4
        expected_end_x = 10
        expected_end_y = 9
        direction = 'fwd'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_bottom_right_corner_fwd(self):
        start_x, start_y = 10, 3
        spaces_to_move = 4
        expected_end_x = 9
        expected_end_y = 0
        direction = 'fwd'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_bottom_left_corner_rev(self):
        start_x, start_y = 0, 2
        spaces_to_move = 4
        expected_end_x = 2
        expected_end_y = 0
        direction = 'rev'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_top_left_corner_rev(self):
        start_x, start_y = 2, 10
        spaces_to_move = 4
        expected_end_x = 0
        expected_end_y = 8
        direction = 'rev'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_top_right_corner_rev(self):
        start_x, start_y = 10, 7
        spaces_to_move = 4
        expected_end_x = 9
        expected_end_y = 10
        direction = 'rev'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_bottom_right_corner_rev(self):
        start_x, start_y = 8, 0
        spaces_to_move = 4
        expected_end_x = 10
        expected_end_y = 2
        direction = 'rev'
        newx, newy = self.gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_along_spoke_from_bottom(self):
        game_position.input = lambda _: 'up'  
        gp = game_position.GamePositions()       
        start_x, start_y = 4, 0
        spaces_to_move = 4
        expected_end_x = 5
        expected_end_y = 3
        direction = 'rev'
        newx, newy = gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
            
    def test_move_along_spoke_from_top(self):
        print('test_move_along_spoke_from_top')
        game_position.input = lambda _: 'down'  
        gp = game_position.GamePositions()       
        start_x, start_y = 4, 10
        spaces_to_move = 4
        expected_end_x = 5
        expected_end_y = 7
        direction = 'fwd'
        newx, newy = gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_along_spoke_from_left_side(self):
        print('test_move_along_spoke_from_left_side')
        game_position.input = lambda _: 'right'  
        gp = game_position.GamePositions()       
        start_x, start_y = 0, 4
        spaces_to_move = 4
        expected_end_x = 3
        expected_end_y = 5
        direction = 'fwd'
        newx, newy = gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_move_along_spoke_from_right_side(self):
        print('test_move_along_spoke_from_right_side')
        game_position.input = lambda _: 'left'  
        gp = game_position.GamePositions()       
        start_x, start_y = 10, 6
        spaces_to_move = 4
        expected_end_x = 7
        expected_end_y = 5
        direction = 'fwd'
        newx, newy = gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_start_turn_from_left_spoke(self):
        print('test_start_turn_from_spoke')
        game_position.input = lambda _: 'right'  
        gp = game_position.GamePositions()       
        start_x, start_y = 3, 5
        spaces_to_move = 2
        expected_end_x = 5
        expected_end_y = 5
        direction = 'fwd'
        newx, newy = gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_start_turn_from_top_spoke(self):
        print('test_start_turn_from_spoke')
        game_position.input = lambda _: 'down'  
        gp = game_position.GamePositions()       
        start_x, start_y = 5, 9
        spaces_to_move = 2
        expected_end_x = 5
        expected_end_y = 7
        direction = 'fwd'
        newx, newy = gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
    def test_go_from_spoke_to_perim(self):
        print('test_start_turn_from_spoke')                
        commands = ['right', 'down']
        command_iter = iter(commands)
        game_position.input = lambda _: next(command_iter)
        gp = game_position.GamePositions()       
        start_x, start_y = 7, 5
        spaces_to_move = 5
        expected_end_x = 10
        expected_end_y = 3
        direction = 'fwd'
        newx, newy = gp.find_next_position(
            start_x,
            start_y,
            spaces_to_move,
            direction
        )
        self.assertEqual(newx, expected_end_x)
        self.assertEqual(newy, expected_end_y)
        
if __name__ == "__main__":
    unittest.main()