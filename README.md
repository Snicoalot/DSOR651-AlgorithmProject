# DSOR651-AlgorithmProject
Final algorithm project for AFIT DSOR651 class. Using Monte Carlo Tree Search to play a game of tic-tac-toe. Produced by 2d Lt Nico De Ros.

## Algorithm Purpose
The main code file in this repository is the tictactoe.py file, which allows users to play a game of tic tac toe. When the code is run, the user will initially be prompted over the terminal on whether they would like to initiate a singleplayer game or a multiplayer game (classic). If the user chooses to play a multiplayer game, two players will take turns choosing which grid space they would like to put their marker into until a game has concluded. If the user chooses to play a singleplayer game, the user will play against the Monte Carlo Search Tree (MCST) algorithm, with each player taking turns choosing which grid space they would like to put their marker into until a game has concluded. The purpose of this is to demonstrate the decision-making algorithm and how it (hopefully) can prove to be a challenging opponent against a human in even a simple game like tic tac toe.

## Hyperparameters
Typical hyperparameters for different variations of MCTS include the number of simulations run, the maximum simulation depth (tree size), and the backpropogation strategy, which determines how future results are backpropogated up the tree to current game states. The hyperparameter that this iteration of MCTS uses is the number of the number of simulations run it creates to be able to imagine future gamestates and select one that leads to the best outcome. If this number is low, then the MCTS algorithm will not perform well because it will work with incomplete information and only be able to simulate a small portion of all the potential gamestates. If this number is high, the algorithm will have better predictive performance but the simulations will take longer to run. While no hyperparameter optimization was done, there are about 20,000 potential gamestates in tic tac toe (which does include impossible games, such as a player moving after another player has already won), so that is the current number of simulations set for the algorithm. If you do notice performance issues on your system, the lowest recommendation to still recieve useful results would be to set the hyperparameter to 1,000.

## Background
### History
The Monte Carlo method has been in use since the 1940's, when it was used to approach incredibly complex, deterministic problems with random sampling. However, the MCTS was developed and first used in 2006 to beat human players at elementary games of Go. MCTS was developed as a tool for winning games, and specifically tree-based games, such as Go, Checkers, and Tic Tac Toe. These games are tree based games because they can be represented as a directed graph whose nodes are positions in a game (the arrangement of the pieces in a board game) and whose edges are moves (actions taken to move a piece from one position to another). In 2012, a variation of the MCTS, AlphaGo, was used to defeat Lee Sedol, the second best Go player in the world at the time, which earned AlphaGo the prestigious rank of 9 dan (master) at the game of Go. Since that historic moment, MCTS has only continued to improve in its range of capability and power of the simulations it runs to apply to more problems, including non-deterministic games such as poker.

### Variations
There are multiple variations of MCTS, so we will examine a few of these. Specifically, we will look at UCB1, Flat Upper Confidence Bounds (Flat UCB), Bandit Algorithm for Small Trees (BAST), and Single-Player Monte Carlo Tree Search (SP-MCTS).

#### UCB1
UCB1 is a widely used algorithm in the context of the multi-armed bandit problem, where the goal is to maximize the cumulative reward by choosing the optimal action from a set of available options. It strikes a balance between exploration (trying out different actions to gather more information) and exploitation (choosing the action that currently appears to be the best based on the available information). The algorithm maintains a value estimate and a confidence interval for each action, and selects the action with the highest upper confidence bound at each step. The upper confidence bound is calculated as the sum of the value estimate and a exploration term that depends on the number of times the action has been played and a tunable exploration parameter. UCB1 has theoretical guarantees on its regret (the difference between the rewards obtained and the optimal rewards) and has been successfully applied in various domains, including reinforcement learning, online advertising, and Monte Carlo Tree Search.

#### Flat UCB
Flat UCB is a variant of the UCB1 algorithm used in MCTS for games with large branching factors. Instead of maintaining a separate upper confidence bound value for each child node, it computes a single UCB value for the entire set of child nodes. This approach reduces the computational overhead and memory requirements, making it suitable for games with large action spaces. However, this aggregation of results may result in a loss of accuracy compared to the standard UCB1 algorithm. Flat UCB is particularly useful in real-time scenarios where computational resources are limited.

#### BAST
BAST is a variation of MCTS designed specifically for small search trees. It combines the UCB1 algorithm with a depth-first search approach, allowing for a more thorough exploration of the tree. BAST is particularly effective in situations where the search tree is small enough to be explored exhaustively within the available computational budget. It can outperform traditional MCTS algorithms in certain domains with small search spaces. However, BAST may not scale well to larger search trees or domains with high branching factors.

#### SP-MCTS
Single-Player Monte Carlo Tree Search is a variant of MCTS applied to single-player games or decision-making problems. In these scenarios, there is no adversary, and the goal is to find the optimal sequence of actions to maximize a certain objective function. The algorithm follows a similar structure to MCTS, but without the need for simulations against an opponent. It uses rollouts or heuristic evaluations to estimate the value of each state or action sequence. Single-Player MCTS has been successfully applied in domains such as optimization, planning, and decision-making under uncertainty.

## Pseudocode
Selection, Expansion, Simulation, Backpropogation

There are two fundamental parts to the MCTS algorithm. The first part is understanding how the algorithm actually simulates future moves, and then uses those simulations to make good decisions. The process for this is Selection, Expansion, Simulation, and Backpropogation. The following image will be helpful in understanding:

![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/74c948d4-4cb5-4876-823a-50a8a4912838)

In the Selection phase, the algorithm chooses a non-leaf node, and passes it to the Expansion function. In the Expansion phase, the algorithm creates a new child node for each **immediately** possible move. For example, lets say we were working with a blank tic tac toe board, the expansion algorithm would create 9 child nodes, each with the ***X*** symbol in one of the 9 grid squares. It would then pass those children on to the Simulation phase. The Simulation phase takes each child node and plays a random game until terminating. Once a simulated game is completed, it is "backed up" in the Backpropogation phase, which adjusts the statistic of each prior node to allow the algorithm to make an "intelligent" choice on where to play next.

The full psuedocode is here:

![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/d3c3fdce-da77-43f2-b92d-72df8e92f572)

A root node is created, and while a predefined ending criteria is not yet met, the algorithm performs a selection, expansion, and backpropogation. Once the ending criteria is met, it selects the child node with the best probability of leading to a winning gamestate and makes that move. Rinse and repeat until gameover!

## Example code to import and use module
Screenshots of actual code and explanation of how it works.

## Visualization or animation of algorithm steps or results
To get a better idea on how MCTS works, watch these two video clips!
https://youtube.com/clip/UgkxcLUTgE6jOOiOC8taLX54co23UHLOlci7?si=ZZ2-CMyxJMwW0I09
https://youtube.com/clip/Ugkxe_k9BzKlb-T77BCq5N2m620UfasHR_G1?si=LRiWVclOpuVhw7K_

An example iteration is provided here:

![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/bd5e03ef-08e3-4f12-8b3f-e55e66411d49)

From the image, we see some two player game (white nodes represent player 1, and gray nodes represent player 2) unfolding. In each node, we see a fraction where the numerator is the number of games won from that point moving forward and the denominator is the number of games *simulated* from that point forward. On the far left, under Selection, we see a bolded path from the root node to a gray leaf node with a 3/3 in it (again, meaning 3 games have been simulated from this node and that player 2 won each of those 3 games). The picture moves forward into an expansion, and creates a white node with a 0/0. This means this *would* be player 1's turn, but 0 games have been simulated or won from this point forward. The algorithm continues on to Simulation, where a nondescript number of games took place with random moves resulting in a loss for player 1 (shown by the 0/1). This is then backpropogated up the tree, updating the simulated results for all nodes in the path. Thus, all nodes in the path receive an increment in their demonitaor (for one extra simulation), and **only** the nodes in the path corresponding to player 2 (gray) receive an increment in their numerator (for one extra win). This iterative process takes place until a predefined ending criteria is met.

## Benchmark Results
Win metric only: Made mistakes after the second move

Tie metric only: Only made mistakes

Combination of Win and Tie metrics: Devious weapon, ties every game.

Because the algorithm is inherently stochastic, it is difficult to get a baseline to compare it to. It would be more interesting if, now that it has been successfully adapted to tic tac toe, it could be generalized to play other games like checkers, chess, or Go.

However, the code was still adapted to make a 4x4 grid of tic tac toe, where the same rules for winning apply (any 3-long sequence of any one token). This makes it harder to strategize, especially since most people do not play tic tac toe on a 4x4 grid and thus are unaccustomed to the game. This puts the player and MCTS on the same starting point! Where before, I was able to tie every game easily, I now find myself struggling to consider future moves in a way that allows me to tie, much less win. To be honest, my very first time playing on the 4x4 grid with intention still resulted in a loss on my part! A screenshot of my loss is included here:
![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/d47eb714-4b5b-4925-b6a5-b628029bd1b7)


## Lessons Learned
My implementation of MCTS is flawed. When determining whether immediately to win a game or block the player, the algorithm will take the move that results in a block. This is likely due to my rewards function, which gives equal reward for tieing a game or winning a game. This means that there is hyperparameter tuning to be done in the background of MCTS to nudge it in the direction of always choosing winning vs winning and tieing. Originally, I had only included code to make the algorithm look for a win. This resulted in a garbage algorithm that never blocked me from winning! It was, however, consistent in the order of the moves it would play given my strategy used. I thought I would be sneaky and instead try to implement a solution that always forces a tie. After all, any two sufficiently experienced players should be able to tie every game. However, this produced an even worse algorithm that played erratically without any stable, consistent strategy at all. So I turned it off.

![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/b1e32b73-cbef-4754-ae6d-24272af314a2)

I tried many other implementations for creating a method for winning the game, but was unsuccessful until I took the time to write out by hand the steps I wanted my code to follow on pen and paper. This allowed me to build an intuition of how I wanted my code to flow from start to finish, and then allowed me to have a scaffold to work with for the remained of the project. This is a spectacular reminder that using online references is never the best strategy, and that our own brains are our best resource.

Additionally, the amount of publicly available documentation for adding multiprocessing to MCTS is incredibly low, with concrete examples of usage being even rarer. This made implementing multiprocessing very difficult, and I ultimately ran out of time to successfully incorporate it into my project. 


## Unit-testing strategy
There are 10 functions in this algorithm. Of the 10, all functions except the main function are tested. The tested functions are: the initializer, expand, select, simulation, checkWin, mcts, chooseGame, getMove, and printBoard functions were tested individually. To implement the unit testing, an additional script, unit_tests.py, was created. The traditional approach of creating a unit test and running it to ensure it fails before fixing it was not implemented. Instead, the entire tictactoe.py script was created, and then unit tests were implemented to ensure that the code operated as expected.

Additionally, after the code was finished, coverage.py was installed and used to get an understanding of the code coverage completed for this project. An image is included which shows that there is 78% code coverage. 

![image](https://github.com/Snicoalot/DSOR651-AlgorithmProject/assets/144690537/91a865df-fc30-4184-883d-676bbe0f98dc)

According to Microsoft.com, a minimum code coverage should be between 60% - 70%, and a decent testing code coverage should be between 70% - 80%, with anything above 80% being 'Overkill Test Coverage'. This means that the algorithm created has a good code coverage, and will likely not run into and major bugs or errors while running. As a matter of fact, no bugs can be reported at the time of publishing.

## Documentation
All code here was produced by 2d Lt Nico De Ros without the use of external aid. Code examples from a variety of websites to include online journals, YouTube videos, and wikipedias were used, in addition to code previously created for other purposes (specifically unit testing from Databases and the Class and Node system from USAFA CS220). The source, https://repository.essex.ac.uk/4117/1/MCTS-Survey.pdf, was foundational to understanding this material.























