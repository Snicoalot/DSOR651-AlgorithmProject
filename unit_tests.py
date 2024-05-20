'''
This code will perform unit testing for the tictactoe.py 
'''

# Import necessary libraries
import unittest
from io import StringIO
import sys
import tictactoe
from tictactoe import Node

# Test if the node initialization works
class TestFuncs(unittest.TestCase):

    def test_init(self):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        player = 1
        root = Node(board, player)

        self.assertEqual(root.player, 1)
        self.assertEqual(root.board, [0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(root.children, [])
        self.assertEqual(root.visits, 0)
        self.assertEqual(root.wins, 0)
        self.assertIsNone(root.parent)

    def test_checkWin(self):
        # Test for a winning row
        board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        player = 1
        result = tictactoe.checkWin(board, player)
        self.assertTrue(result)

        # Test for a winning column
        board = [1, 0, 0, 1, 0, 0, 1, 0, 0,]
        player = 1
        result = tictactoe.checkWin(board, player)
        self.assertTrue(result)

        # Test for a winning diagonal
        board = [-1, 0, 0, 0, -1, 0, 0, 0, -1]
        player = -1
        result = tictactoe.checkWin(board, player)
        self.assertTrue(result)

        # Test for a non-winning board
        board = [1, -1, 1, -1, 1, -1, -1, 1, -1]
        player = -1
        result = tictactoe.checkWin(board, player)
        self.assertFalse(result)

    # TODO: Find a way to test for an input
    # def test_getMove(self):
    #     board = [0, 0, 0, 0, 1, 0, 0, 0, 0]
    #     move = getMove(board)
    #     self.assertEqual(move, 4)

    def test_printBoard(self):
        # Capture the output of the printBoard function
        captured_output = StringIO()
        sys.stdout = captured_output

        # Test case 1: Empty board
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected_output = " _ _ _\n _ _ _\n _ _ _\n\n\n"
        tictactoe.printBoard(board)
        self.assertEqual(captured_output.getvalue(), expected_output)

        # Test case 2: Board with X and O
        board = [1, -1, 0, 0, 1, 0, 0, 0, -1]
        expected_output = " X O _\n _ X _\n _ _ O\n\n\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        tictactoe.printBoard(board)
        self.assertEqual(captured_output.getvalue(), expected_output)

# Load the tests
test_loader = unittest.TestLoader().loadTestsFromTestCase(TestFuncs)

# Run the tests
test_runner = unittest.TextTestRunner().run(test_loader)