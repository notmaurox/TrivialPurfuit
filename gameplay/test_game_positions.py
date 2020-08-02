import unittest

from game_position import GamePositions

class TestInteractions(unittest.TestCase):
    def setUp(self):
        # Default board is 11x11
        self.gp = GamePositions()
        
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