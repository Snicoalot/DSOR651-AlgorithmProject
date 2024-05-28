'''
This file contains the main code for tic tac toe.
'''

# Load necessary libraries
import random
import math

# Create a class to describe the contents of the objects that belong to it
    # For this game, we will treat a single instance of a tic tac toe boardgame as a single node, with future gameboards being
    # represented as nodes stemming from the root node as children.

class Node:
    # Intialize a node
    def __init__(self, board, player):
        # Each node will contain information on the player whose turn it is, the current gameboard, a list of their children
        # (as immediate possibilities for future gamestates), and counts of how often future nodes are visited and result
        # in wins.
        self.player = player
        self.board = board
        self.children = []
        self.visits = 0
        self.wins = 0
        # Additionally, define a way for children nodes to refer back to their parents
        self.parent = None
        for child in self.children:
            child.parent = self

    # def update(self, result):
    #     self.visits += 1
    #     self.wins += result

    # def backpropagate(self, node, result):
    #     while node is not None:
    #         node.update(result)
    #         result = -result
    #         node = node.parent

    # Expand the tree to uncover new paths
    def expand(self):
        for i in range(9):
            # Where any spot is available
            if self.board[i] == 0:
                # Make a new copy of the board where the AI plays that spot, append to the tree
                new_board = self.board.copy()
                new_board[i] = self.player
                new_node = Node(new_board, -self.player)
                self.children.append(new_node)

    def select(self):
        total_visits = sum(child.visits for child in self.children)
        if total_visits != 0:
            log = math.log(total_visits)
        else:
            log = 0
        best_score = -99999
        best_child = None
        for child in self.children:
            if child.visits == 0:
                return child
            # UCT Algorithm for determining best child
                # Upper Confidence Bound for Trees
            score = (child.wins / child.visits) + math.sqrt(2 * log / child.visits)
            if score > best_score:
                best_score = score
                best_child = child
        return best_child

    def simulation(self):
        board = self.board.copy()
        player = self.player
        while True:
            
            if 0 not in board:
                return 0
            empty_cells = [i for i in range(9) if board[i] == 0]
            move = random.choice(empty_cells)
            board[move] = player
            if check_winner(board, player):
                return player
            player = -player


def checkWin(board, player):
    # Define a list of winning gamestates
    winningPositions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    # Return true if all elements in a winning position are assigned to a single player
    for positions in winningPositions:
        if all(board[pos] == player for pos in positions):
            return True
    return False

def mcts(board, player):
    root = Node(board, player)
    root.expand()
    for _ in range(20000):
        node = root
        while node.children:
            node = node.select()
            if not node.children:
                node.expand()
        result = node.simulation()
        while node is not None:
            node.visits += 1
            if result == node.player:
                node.wins += 1
            node = node.parent
    return max(root.children, key=lambda child: child.visits).board

def playGame():
    # Intialize a new game and have the user select singleplayer or two player gamemode
    board = [0] * 9
    players = [1, -1]
    print(f"Would you like to play 1 or 2 player tic tac toe? (enter 1 or 2): ")
    gamemode = 0
    while gamemode == 0:
        game = input("")
        # Will not accept non-integer numbers, or numbers in illegal placements
        try:
            game = int(game)
            if isinstance(game, int):
                if game == 1 or game == 2:
                    gamemode = chooseGame(game)
                else:
                    print("Invalid choice. Try again.")
        except:  
            print("Invalid choice. Try again.")

    # Code for singleplayer gamemode (MCTS)
    if gamemode == 1:
        while True:
            for player in players:
                printBoard(board)
                if player == 1:
                    move = getMove(board)
                    print(f"Player 1 chooses to move to {move}:")
                    board[move] = player
                else:
                    # TODO: Change to MCTS algorithm taking a turn
                    board = mcts(board, player)
                if checkWin(board, player):
                    printBoard(board)
                    print(f"Player {'1' if player == 1 else '2'} wins the game!")
                    return
                if 0 not in board:
                    printBoard(board)
                    print("It's a tie!")
                    return

    # Code for two player gamemode (classic)
    elif gamemode == 2:
        while True:
            for player in players:
                printBoard(board)
                if player == 1:
                    move = getMove(board)
                    print(f"Player 1 chooses to move to {move}:")
                    board[move] = player
                else:
                    move = getMove(board)
                    print(f"Player 2 chooses to move to {move}:")
                    board[move] = player
                if checkWin(board, player):
                    printBoard(board)
                    print(f"Player {'1' if player == 1 else '2'} wins the game!")
                    return
                if 0 not in board:
                    printBoard(board)
                    print("It's a tie!")
                    return

def chooseGame(gamemode):
    if gamemode == 1:
        return 1
    else:
        return 2

def getMove(board):
    # Get a valid move from a user
    while True:
        print(f"Enter your move (0-8): ")
        move = input("")
        # Will not accept non-integer numbers, or numbers in illegal placements
        try:
            move = int(move)
            if isinstance(move, int):
                if 0 <= move <= 8 and board[move] == 0:
                    return move
                else:
                    print("Invalid move. Try again.")
        except:  
            print("Invalid move. Try again.")

def printBoard(board):
    # Print the board
    for i in range(0, 9, 3):
        print(f" {' '.join(['X' if board[j] == 1 else ('O' if board[j] == -1 else '_') for j in range(i, i+3)])}")
    print("\n")

if __name__ == "__main__":
    playGame()