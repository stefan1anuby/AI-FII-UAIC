import unittest

from main import *

class BoardTest(unittest.TestCase):

    def test_initial_and_goal_state(self):
        initial_state = [[2, 5, 3], [1, 0, 6], [4, 7, 8]]
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        puzzle = Board(initial_state)

        self.assertEqual(puzzle.state, initial_state)
        self.assertFalse(puzzle.is_goal())

        puzzle.state = goal_state
        self.assertTrue(puzzle.is_goal())

    def test_transitions(self):
        state = [[2, 5, 3], [1, 0, 6], [4, 7, 8]]
        puzzle = Board(state)

        self.assertTrue((1, 2) in puzzle.possible_moves())

        new_puzzle = puzzle.make_move((1, 2))
        self.assertEqual(new_puzzle.state, [[2, 5, 3], [1, 6, 0], [4, 7, 8]])

    def test_iddfs(self):

        puzzle = Board([[8, 6, 7], [2, 5, 4], [0, 3, 1]])
        """
        print("distanta manhatam : " + str(manhattan_distance_as_list(puzzle)))
        print("distanta hamming : " + str(hamming_distance_as_list(puzzle)))
        print("distanta euclidian : " + str(euclidian_distance_as_list(puzzle)))
        """
        """
        solution = iddfs(puzzle, 100)
        self.assertTrue(solution.is_goal())
        """
    
        puzzle2 = Board([[2, 5, 3], [1, 0, 6], [4, 7, 8]])
        """
        print("distanta manhatam : " + str(manhattan_distance_as_list(puzzle2)))
        print("distanta hamming : " + str(hamming_distance_as_list(puzzle2)))
        print("distanta euclidian : " + str(euclidian_distance_as_list(puzzle2)))
        """
        issuccess , solution2 , iterations = iddfs(puzzle2, 100)
        self.assertTrue(solution2.is_goal())
        
        """
        puzzle3 = Board([[2, 7 , 5], [0, 8, 4], [3, 1, 6]])
        issuccess , solution3 , iterations = iddfs(puzzle3, 100)
        self.assertTrue(solution3.is_goal())
        """
        
    def test_greedy_search_hamming(self):
        initial_state = [[8, 6, 7], [2, 5, 4], [0, 3, 1]]
        puzzle = Board(initial_state)
        issuccess , solution , iterations = greedy_search(puzzle, hamming_distance)
        self.assertTrue(solution.is_goal())

    def test_greedy_search_manhattan(self):
        initial_state = [[8, 6, 7], [2, 5, 4], [0, 3, 1]]
        puzzle = Board(initial_state)
        issuccess , solution , iterations = greedy_search(puzzle, manhattan_distance)
        self.assertTrue(solution.is_goal())

    def test_greedy_search_euclidean(self):
        initial_state = [[8, 6, 7], [2, 5, 4], [0, 3, 1]]
        puzzle = Board(initial_state)
        issuccess , solution , iterations = greedy_search(puzzle, euclidean_distance)
        self.assertTrue(solution.is_goal())
        

if __name__ == '__main__':
    unittest.main()