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

    def test_expand(self):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        player = 1
        root = Node(board, player)
        root.expand()
        # Checking to make sure there are the correct amount of children, a player switch, and a correct board
        self.assertEqual(len(root.children), 9)
        self.assertEqual(root.children[0].board, [1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(root.children[1].board, [0, 1, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(root.children[5].board, [0, 0, 0, 0, 0, 1, 0, 0, 0])
        self.assertEqual(root.children[7].board, [0, 0, 0, 0, 0, 0, 0, 1, 0])
        self.assertEqual(root.children[8].board, [0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(root.children[0].player, -1)

        board = [0, 0, 1, -1, 0, 0, 0, 0, 1]
        player = -1
        root = Node(board, player)
        root.expand()
        # Checking to make sure there are the correct amount of children, a player switch, and a correct board
        self.assertEqual(len(root.children), 6)
        self.assertEqual(root.children[0].player, 1)
        self.assertEqual(root.children[0].board, [-1, 0, 1, -1, 0, 0, 0, 0, 1])

        board = [1, -1, 1, -1, 1, -1, 1, -1, 1]
        player = -1
        root = Node(board, player)
        root.expand()
        # Edge Case: Checking for no children, and an empty list for children
        self.assertEqual(len(root.children), 0)
        self.assertEqual(root.children, [])

    def test_select(self):
        board = [0, 0, 1, -1, 0, 0, 0, 0, 1]
        player = -1
        root = Node(board, player)
        root.expand()
        i = 0
        # Create different score for each child node
        for child in root.children:
            child.wins = i
            i = i + 1
        # Test that the best node is the last node 
        node = root.select()
        self.assertEqual(node, root.children[-1])

        i = 0
        # Create different score for each child node
        for child in root.children:
            child.wins = 10 - i
            i = i + 1
        # Test that the best node is the first node 
        node = root.select()
        self.assertEqual(node, root.children[0])

        i = 0
        # Create different score for each child node
        for child in root.children:
            child.wins = 10 - i
            i = i + 1
            if child == root.children[3]:
                child.wins = 50
        # Test that the best node is the third node 
        node = root.select()
        self.assertEqual(node, root.children[3])

    def test_simulation(self):
        board = [0, 0, 1, -1, 0, 0, 0, 0, 1]
        player = -1
        root = Node(board, player)
        

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

    def test_chooseGame(self):
        # Test for a correctly chosen game
        game = 1
        gamemode = tictactoe.chooseGame(game)
        self.assertEqual(gamemode, 1)

        game = 2
        gamemode = tictactoe.chooseGame(game)
        self.assertEqual(gamemode, 2)

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