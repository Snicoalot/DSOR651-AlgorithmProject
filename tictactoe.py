'''
This file contains the main code for tic tac toe.
'''

# Load necessary libraries
import random
import math
import multiprocessing as mp
import sys

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

    # Expand the tree to uncover new paths
    def expand(self):
        for i in range(9):
            # Where any spot is available
            if self.board[i] == 0:
                # Make a new copy of the board where the AI plays that spot, append to the tree
                new_board = self.board.copy()
                new_board[i] = self.player
                new_node = Node(new_board, -self.player)
                new_node.parent = self
                self.children.append(new_node)

    def select(self):
        # Use the number of wins as a heuristic to pick the best node
        best_child = self.children[0]
        for child in self.children:
            if child.wins > best_child.wins:
                best_child = child
        return best_child

    def simulation(self):
        # Simulate a game of random moves until a game ending state is reached
        board = self.board.copy()
        player = self.player
        while True:
            # Return a tie if no more possible moves exist
            if 0 not in board:
                return 0
            # Otherwise, randomly pick from empty cells
            empty_cells = [i for i in range(9) if board[i] == 0]
            move = random.choice(empty_cells)
            board[move] = player
            # If there is a winner, stop. Otherwise, switch players.
            if checkWin(board, player):
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

def mcts(board, player, sims):
    # Variation of MCTS. Perform Expand, Simulate, Backprop, then Select. As opposed to Selection first.

    # Create a root node from the current board, and expand all possible leaf nodes as children
    root = Node(board, player)
    root.expand()

    # For each child node, simulate 2000 games. This is a hyperparameter tunable by the user.
    for child in root.children:
        for i in range(sims):
            # Where I *would* put parellel processing, if I was good at coding
            # Use parallel processing to simulate the results with multiple cores
            # process = mp.Process(target=Node.simulation, args=(child, i))
            # process.start()
            # print(f"Completing process #{i} of 2000.")
            
            node = child
            
            result = node.simulation()
            switch = 0
            while switch == 0:
                node.visits += 1
                if result == -node.player: # Checks for a winner, doesn't check for blocking opponent
                    node.wins += 1
                # if result == 0: # Checks for a tie, which subverts any strategy from opponent to force a tie!
                #     node.wins += 1
                if node.parent == None:
                    #child = node
                    switch = 1
                else:
                    node = node.parent
            #process.join()
        root.child = child
    node = root.select()

    # Sanity Check the final selected node, return the child with the greatest number of wins
    #print(max(root.children, key=lambda child: child.wins).board)
    return max(root.children, key=lambda child: child.wins).board

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
        gamemode = 0
        sims = -1
        # Collect user input for hyperparameter for the number of iterations run per simulation
        print(f"How many simulations would you like to run for each MCTS iteration? (Recommend at least 1000) ")
        while gamemode == 0:
            sims = input("")
            # Will not accept non-integer numbers, or numbers in illegal placements
            try:
                sims = int(sims)
                if isinstance(sims, int):
                    if sims > 0:
                        gamemode = chooseGame(1)
                        print(f"Running each simulation for {sims} iterations! Good luck!")
                    else:
                        print("Please enter a positive number.")
            except:  
                print("Invalid. Try again.")
        while True:
            # Player and MCTS take turns.
            for player in players:
                printBoard(board)
                if player == 1:
                    # When its the players turn, prompt for a legal move
                    move = getMove(board)
                    print(f"Player 1 chooses to move to {move}:")
                    board[move] = player
                else:
                    # MCTS will play based on the algorithm
                    board = mcts(board, player, sims)
                if checkWin(board, player):
                    # If there is a winner, stop the game
                    printBoard(board)
                    print(f"Player {'1' if player == 1 else '2'} wins the game!")
                    return
                if 0 not in board:
                    # If there are no more moves to be made, declare a tie
                    printBoard(board)
                    print("It's a tie!")
                    return

    # Code for two player gamemode (classic)
    elif gamemode == 2:
        while True:
            # Players take turns playing tic tac toe. Self explanatory.
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
    # Choose 1 for playing against MCTS, choose 2 for playing against a human friend
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

# Play the game
if __name__ == "__main__":
    playGame()