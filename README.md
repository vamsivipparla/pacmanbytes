#### PACMAN BYTES SOFTWARE########

HOW TO RUN:

In order to run our Bidirectional search algorithm, we use the command 


“python pacman.py -l mediumMaze -p SearchAgent -a fn=bdmm,heuristic=euclideanHeuristic“


Here the heuristic function used is euclidean, if we wish to use manhattan Heuristic function, we we give the value “manhattanHeuristic” to our heuristic parameter


Here are some sample output.


"(cse571) mohilkhimani@Mohils-MacBook-Air 1.search % python pacman.py -l mediumMaze -p SearchAgent -a fn=bdmm,heuristic=euclideanHeuristic

[SearchAgent] using function bdmm and heuristic euclideanHeuristic

[SearchAgent] using problem type PositionSearchProblem

Path found with total cost of 77 in 0.0 seconds

Search nodes expanded: 226

Pacman emerges victorious! Score: 433

Average Score: 433.0

Scores: 433.0

Win Rate: 1/1 (1.00)

Record: Win"

 



 

 

 

 

(cse571) mohilkhimani@Mohils-MacBook-Air 1.search % python pacman.py -l smallMaze -p SearchAgent -a fn=bdmm,heuristic=manhattanHeuristic 

[SearchAgent] using function bdmm and heuristic manhattanHeuristic

[SearchAgent] using problem type PositionSearchProblem

Path found with total cost of 29 in 0.0 seconds

Search nodes expanded: 59

Pacman emerges victorious! Score: 481

Average Score: 481.0

Scores: 481.0

Win Rate: 1/1 (1.00)

Record: Win


To run bfs, we write the command: 

“python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs”   for mediumMaze.

If we wish to run in some other maze, instead of “mediumMaze”, we should write the maze name.


To run dfs, we write the command: 

“python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs”   for mediumMaze.

If we wish to run in some other maze, instead of “mediumMaze”, we should write the maze name.


To run ucs, we write the command: 

“python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs”   for mediumMaze.

If we wish to run in some other maze, instead of “mediumMaze”, we should write the maze name.


To run astar, we write the command: 

“python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic”   for mediumMaze.

If we wish to run in some other maze, instead of “mediumMaze”, we should write the maze name, and if we wish to run some other heuristic, we should write the heuristic name, instead of “manhattanHeuristic”.



To run mm0, we write the command: 

“python pacman.py -l mediumMaze -p SearchAgent -a fn=mm0”   for mediumMaze.

If we wish to run in some other maze, instead of “mediumMaze”, we should write the maze name
