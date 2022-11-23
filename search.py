# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


d = {'North': 'South', 'East': 'West', 'South': 'North', 'West': 'East'}

def bidirectionalHeuristic(problem, heuristic):
    
    # bidirectional heursitic search (a*  search from start and goal)
    
    # declaration of dicitonary variables to store visited position from both points
    queue1, position_visited_1 = util.PriorityQueue(),{}
    queue2,position_visited_2 = util.PriorityQueue(),{}

    # start and goal states are added to visited dictionaries defined above

    start_state = problem.getStartState()
    goal_state = problem.goal

    position_visited_1[start_state] = []
    position_visited_2[goal_state] = []

    # two priority queues are used to store nodes based on cost metric in the frontier of both directions from start and end
    #added cost below represent the sum of both cost of actions and heuristic cost

    goal = "g"
    start = "s"
    c = problem.getCostOfActions({})
    h1 = heuristic(start_state, problem, goal)
    added_cost_1 = c+h1
    queue1.push(start_state,added_cost_1)
    
    h2 = heuristic(goal_state, problem, start)
    added_cost_2 = c+h2
    queue2.push(problem.goal, added_cost_2)

    # While loop continues until the both frontier queues are not empty
    #if the goal state unreachable from start we are returning []
    qe1 = queue1.isEmpty()
    qe2 = queue2.isEmpty()
    
    while not qe1:
     while not qe2:

        position_1 = queue1.pop()
        is_goal = problem.isGoalState
        cond = is_goal(position_1, position_visited_2)

        if cond:
            d_reverse = []
            vis2_lst = position_visited_2[position_1]
            for dir_key in vis2_lst:
                drev=d[dir_key]
                d_reverse.append(drev)
            vis1_lst =  position_visited_1[position_1]
            sum = vis1_lst
            sum=sum+d_reverse[::-1] 
            return sum

        successors = problem.getSuccessors(position_1)
        length = len(successors)
        
        i = 0
        while length>0:
            
            state = successors[i]
            length = length -1
            i = i+1
            s0 = state[0]
            s1= state[1]
            lst2=[]
            if s0 not in position_visited_1:
                lst1 = list(position_visited_1[position_1])
                lst2.append(s1)
                position_visited_1[s0] = lst1 + lst2
                c = problem.getCostOfActions(position_visited_1[s0])
                h = heuristic(s0, problem, "g")
                added_cost = c+ h
                queue1.push(s0, added_cost)
            else:
                continue

        position_2 = queue2.pop()
        cond = problem.isGoalState(position_2, position_visited_1)
        
        if cond:

            lst = []
            vis2_lst=position_visited_2[position_2]
            for dir_key in vis2_lst:
                drev = d[dir_key]
                lst.append(drev)
            vis1_lst = position_visited_1[position_2]
            sum = vis1_lst 
            sum=sum+lst[::-1]
            return sum

        successors = problem.getSuccessors(position_2)
        length = len(successors)
         
        i = 0
        while length>0:

            state = successors[i]
            length = length -1
            i = i+1
            s0 = state[0]
            s1= state[1]
            lst2=[]
            if s0 not in position_visited_2:
                    lst1 = list(position_visited_2[position_2])
                    lst2.append(s1)
                    position_visited_2[s0] = lst1 + lst2
                    c =  problem.getCostOfActions(position_visited_2[s0])
                    h = heuristic(s0, problem, "s")
                    added_cost = c+h
                    queue2.push(s0,added_cost)
            else:
                continue
            
    return []

# Abbreviations

bdh = bidirectionalHeuristic
