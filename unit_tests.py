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

        # Test that wins, visits, and the childrens' children are all empty
        self.assertEqual(root.children[6].wins, 0)
        self.assertEqual(root.children[6].visits, 0)
        self.assertEqual(root.children[3].wins, 0)
        self.assertEqual(root.children[2].visits, 0)
        self.assertEqual(root.children[8].wins, 0)
        self.assertEqual(root.children[8].visits, 0)
        self.assertEqual(root.children[2].children, [])
        self.assertEqual(root.children[7].children, [])

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
            # Force the third node to have the highest score
            if child == root.children[3]:
                child.wins = 50
        # Test that the best node is the third node 
        node = root.select()
        self.assertEqual(node, root.children[3])

    # This is a stochastic function, so it is difficult to test for all cases.
    # We will make basic unit tests as a result
    def test_simulation(self):
        # Set up player 1 as the winner, checking to return a winner
        board = [1, -1, 0, -1, 1, 0, 0, 0, 1]
        player = -1
        root = Node(board, player)
        result = root.simulation()
        self.assertEqual(result, 1)

        # Set up player 2 as the winner, checking to return a winner
        board = [-1, -1, -1, 1, -1, 1, 0, 0, 1]
        player = 1
        root = Node(board, player)
        result = root.simulation()
        self.assertEqual(result, -1)

        # Set up a tie, checking to return a 0
        board = [1, 1, -1, -1, -1, 1, 1, -1, 1]
        player = 1
        root = Node(board, player)
        result = root.simulation()
        self.assertEqual(result, 0)

        # Set up for a tie after two simulations, checking to return a 0
        board = [-1, 1, -1, 1, -1, 1, 0, -1, 1]
        player = 1
        root = Node(board, player)
        result = root.simulation()
        self.assertEqual(result, 0)
        
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
'''
# Removing this function temporarily to test workflow, which cannot use inputs
    def test_getMove(self):
        # Set up a board and request a player input
        board = [1, 1, 1, 1, 0, 1, 1, 1, 1]
        player = -1
        print(f"To test the getMove function, press 4 on your keyboard.")
        move = tictactoe.getMove(board)
        board[move] = player

        # Test that the input produces the correct result
        self.assertEqual(move, 4)
        self.assertEqual(board, [1, 1, 1, 1, -1, 1, 1, 1, 1])

        # Set up a board and request a player input
        board = [0, 1, 1, 1, 1, 1, 1, 1, 1]
        player = -1
        print(f"To test the getMove function, press 0 on your keyboard.")
        move = tictactoe.getMove(board)
        board[move] = player

        # Test that the input produces the correct result
        self.assertEqual(move, 0)
        self.assertEqual(board, [-1, 1, 1, 1, 1, 1, 1, 1, 1])

        # Set up a board and request a player input
        board = [-1, -1, -1, -1, -1, -1, -1, -1, 0]
        player = 1
        print(f"To test the getMove function, press 8 on your keyboard.")
        move = tictactoe.getMove(board)
        board[move] = player

        # Test that the input produces the correct result
        self.assertEqual(move, 8)
        self.assertEqual(board, [-1, -1, -1, -1, -1, -1, -1, -1, 1])
'''

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

    # Because MCTS uses the simulation function, which is inherently stochastic, testing will be limited to
    # very specific scenarios.
    def test_mcts(self):
        board = [0, 1, 1, 0, -1, 0, 0, 0, 0]
        player = -1
        sims = 2000
        root = Node(board, player)
        # Test for MCTS to block the opponent without winning the board
        board = tictactoe.mcts(board, player, sims)
        self.assertEqual(board, [-1, 1, 1, 0, -1, 0, 0, 0, 0])

        board = [1, 0, 0, 0, -1, -1, 0, 1, 0]
        player = 1
        sims = 2000
        root = Node(board, player)
        # Test for MCTS to block the opponent without winning the board
        board = tictactoe.mcts(board, player, sims)
        self.assertEqual(board, [1, 0, 0, 1, -1, -1, 0, 1, 0])

        board = [-1, 1, 1, 0, -1, 1, 0, 0, 0]
        player = -1
        sims = 2000
        root = Node(board, player)
        # Test for MCTS to select the winning position in the board
        board = tictactoe.mcts(board, player, sims)
        self.assertEqual(board, [-1, 1, 1, 0, -1, 1, 0, 0, -1])

        board = [1, 1, 0, -1, -1, 0, 0, 0, 0]
        player = 1
        sims = 2000
        root = Node(board, player)
        # Test for MCTS to block the opponent
        board = tictactoe.mcts(board, player, sims)
        self.assertEqual(board, [1, 1, 0, -1, -1, 1, 0, 0, 0])

        board = [1, 1, 0, -1, -1, 1, 0, 1, -1]
        player = -1
        sims = 2000
        root = Node(board, player)
        # Test for MCTS to force a tie
        board = tictactoe.mcts(board, player, sims)
        self.assertEqual(board, [1, 1, -1, -1, -1, 1, 0, 1, -1])

# Load the tests
test_loader = unittest.TestLoader().loadTestsFromTestCase(TestFuncs)

# Run the tests
test_runner = unittest.TextTestRunner().run(test_loader)
