import unittest

from main import NumberScrabble

class Test(unittest.TestCase):
    def test_win_True(self):
        ns = NumberScrabble()
        
        ns.turn = 0
        ns.player_a = [5, 4, 3, 6]
        
        self.assertTrue(ns.is_win())
        
    def test_win_False(self):
        ns = NumberScrabble()
        
        ns.turn = 0
        ns.player_a = [5, 4, 3, 2]
        
        self.assertFalse(ns.is_win())
        
    def test_possible_moves(self):
        ns = NumberScrabble()
        ns.turn = 0
        
        # ns.player_a = [5, 4, 3, 6]
        ns.make_move(5)
        ns.make_move(4)
        ns.make_move(3)
        ns.make_move(6)
        
        self.assertEqual(ns.get_possible_moves(), [1, 2, 7, 8, 9])
        
if __name__ == '__main__':
    unittest.main()