# DSOR651-AlgorithmProject
Final algorithm project for AFIT DSOR651 class. Using Monte Carlo Tree Search to play a game of tic-tac-toe. Produced by 2d Lt Nico De Ros.

## Algorithm Purpose
The main code file in this repository is the tictactoe.py file, which allows users to play a game of tic tac toe. When the code is run, the user will initially be prompted over the terminal on whether they would like to initiate a singleplayer game or a multiplayer game (classic). If the user chooses to play a multiplayer game, two players will take turns choosing which grid space they would like to put their marker into until a game has concluded. If the user chooses to play a singleplayer game, the user will play against the Monte Carlo Search Tree (MCST) algorithm, with each player taking turns choosing which grid space they would like to put their marker into until a game has concluded. The purpose of this is to demonstrate the decision-making algorithm and how it (hopefully) can prove to be a challenging opponent against a human in even a simple game like tic tac toe.

## Hyperparameters
Typical hyperparameters for different variations of MCTS include the number of simulations run, the maximum simulation depth (tree size), and the backpropogation strategy, which determines how future results are backpropogated up the tree to current game states. The hyperparameter that this iteration of MCTS uses is the number of the number of simulations run it creates to be able to imagine future gamestates and select one that leads to the best outcome. If this number is low, then the MCTS algorithm will not perform well because it will work with incomplete information and only be able to simulate a small portion of all the potential gamestates. If this number is high, the algorithm will have better predictive performance but the simulations will take longer to run. While no hyperparameter optimization was done, there are about 20,000 potential gamestates in tic tac toe (which does include impossible games, such as a player moving after another player has already won), so that is the current number of simulations set for the algorithm. If you do notice performance issues on your system, the lowest recommendation to still recieve useful results would be to set the hyperparameter to 5,000.

## Background
### History
The Monte Carlo method has been in use since the 1940's, when it was used to approach incredibly complex, deterministic problems with random sampling. However, the MCTS was developed and first used in 2006 to beat human players at elementary games of Go. MCTS was developed as a tool for winning games, and specifically tree-based games, such as Go, Checkers, and Tic Tac Toe. These games are tree based games because they can be represented as a directed graph whose nodes are positions in a game (the arrangement of the pieces in a board game) and whose edges are moves (actions taken to move a piece from one position to another). In 2012, a variation of the MCTS, AlphaGo, was used to defeat Lee Sedol, the second best Go player in the world at the time, which earned AlphaGo the prestigious rank of 9 dan (master) at the game of Go. Since that historic moment, MCTS has only continued to improve in its range of capability and power of the simulations it runs to apply to more problems, including non-deterministic games such as poker.

### Variations
There are multiple variations of MCTS, so we will examine these one by one.

## Pseudocode
Selection, Expansion, Simulation, Backpropogation
There are two fundamental parts to the MCTS algorithm. The first part is understanding how the algorithm actually simulates future moves, and then uses those simulations to make good decisions. The process for this is Selection, Expansion, Simulation, and Backpropogation. The following image will be helpful in understanding:

![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/74c948d4-4cb5-4876-823a-50a8a4912838)

In the Selection phase, the algorithm chooses a non-leaf node, and passes it to the Expansion function. In the Expansion phase, the algorithm creates a new child node for each **immediately** possible move. For example, lets say we were working with a blank tic tac toe board, the expansion algorithm would create 9 child nodes, each with the ***X*** symbol in one of the 9 grid squares. It would then pass those children on to the Simulation phase. The Simulation phase takes each child node and plays a random game until terminating. Once a simulated game is completed, it is "backed up" in the Backpropogation phase, which adjusts the statistic of each prior node to allow the algorithm to make an "intelligent" choice on where to play next.

The full psuedocode is here:

![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/d3c3fdce-da77-43f2-b92d-72df8e92f572)

## Example code to import and use module

## Visualization or animation of algorithm steps or results

## Benchmark Results
Comparison of efficiency and effectiveness 

## Lessons Learned
Such as new code snippets to support some computations

## Unit-testing strategy
What steps of the algorithm were tested individually?
Code-coverage measurement
