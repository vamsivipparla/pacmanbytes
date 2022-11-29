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
from game import Directions
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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    dfs_s = util.Stack()
    """defining a stack using the util package"""
    dfs_s.push((problem.getStartState(), [])) 
    node_checked = list()
    """Defining a list for all the nodes that are already visited"""

    while not dfs_s.isEmpty():
        stateInPresent, steps = dfs_s.pop()
        if stateInPresent in node_checked: continue
        if problem.isGoalState(stateInPresent): return steps
        """ if the goal state is same as the current state, return the solution"""

        node_checked.append(stateInPresent)
        """ Add all the current nodes after every loop to the list of already visited nodes"""
        for s,a,c in problem.getSuccessors(stateInPresent):
            dfs_s.push((s, steps + [ a ]))

    return []







    
    
    
    
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    bfs_q = util.Queue() 
    
    bfs_q.push((problem.getStartState(), [])) 
    node_checked = []
    """Defining an empty list for the already visited nodes"""

    while not bfs_q.isEmpty(): 
        stateInPresent, steps = bfs_q.pop() #pooping the stack and storing the state and actions in the current states and actions
        if stateInPresent not in node_checked:   
            node_checked.append(stateInPresent)
            if problem.isGoalState(stateInPresent): 
                return steps # if the goal state is same as the current state then return the solution
            else:
                
                    next_state = problem.getSuccessors(stateInPresent)
                      
                    for state in next_state:
                            bfs_q.push((state[0], steps + [state[1]]))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ucs_q = util.PriorityQueue()
    """We are using the priority queue data structure from the util.py package"""
    ucs_q.push((problem.getStartState(), [], 0), 0)
    """we are pushing the starting states of our problem into the priority queue in this step"""
    """Initially, the steps and cost are both zero for the start state"""
    
    node_checked = list()
    """ here we are defining the list as the nodes that are visited """

    

    while not ucs_q.isEmpty():
        """whenever the priority queue is not empty, the while loop will execute""" 
        stateInPresent, steps, cost = ucs_q.pop()
        """popping the queue to check the present state of the node"""
        if stateInPresent in node_checked:
            continue
        """ if the present state is present in the checked nodes that is the nodes that are visited, our search will continue"""
        
        if problem.isGoalState(stateInPresent):
            return steps
        """if our present state is same as the goalstate, we return the total steps"""

        node_checked.append(stateInPresent)
        """ adding all the checked nodes to our present state"""

        
        for s, a, c in problem.getSuccessors(stateInPresent):

            """Gets the information of the successor state"""
            ucs_q.push((s, steps + [ a ], cost + c), cost + c)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    astar_q = util.PriorityQueue()
    #Initialiazing a priority queue for astar using the util package
    

    Initial_state = [problem.getStartState(), 0, []]
    #Initially passing 0 for the steps and cost

    push = 0

    astar_q.push(Initial_state, push)  # Pushing the initial state in the priority queue

    node_checked = []

    #empty list for the already visited nodes

    while not astar_q.isEmpty():
        [s, c, p] = astar_q.pop()
        # popping the first element of the stack and storing the states, actions and cost
        if problem.isGoalState(s):
            
            return p  # if goal state is equal to the current state then return the solution
        if s not in node_checked:
            node_checked.append(s)
            for next_state, next_steps, next_cost in problem.getSuccessors(s):
                final_cost = c + next_cost
                final_path = p + [next_steps, ]
                astar_q.push([next_state, final_cost, final_path], final_cost + heuristic(next_state, problem))
    util.raiseNotDefined()
    
    

                
                
  ################
  
 # ''' Brute force algorithm code starts here '''
  
  ###############
        
            
    
def Reverse(p):               #Pathreverse
    
        path = []
        
        for path_2 in p:
            
            if path_2 == 'East':
                path_reverse = 'West'
                
            if path_2 == 'North':
                path_reverse = 'South'
                
            if path_2 == 'West':
                path_reverse = 'East'

            if path_2 == 'South':
                path_reverse = 'North'
                
            path.append(path_reverse)
            
        return path[::-1]
    

def node_check_1(Queue_1, i, path_start):

        if Queue_1.isthere(i[0]):
            node_present = i[0]
            Queue_1.remove_by_value(node_present)
            
            
        if i[0] in path_start:
            path_present = i[0]
            del path_start[path_present]

def node_check_2(Queue_2, i, path_goal):

        if Queue_2.isthere(i[0]):
            node_present = i[0]
            Queue_2.remove_by_value(node_present)
            
        elif i[0] in path_goal:
            path_present = i[0]
            del path_goal[path_present]
        
    
def util_func(State_1, Queue_1, path_start, cost_1_dic, path_1, problem, cost_1):


    for i in problem.getSuccessors(State_1):

        successor_present_1 = Queue_1.isthere(i[0])

        if successor_present_1:
        
            cost_to_successor = i[2]
            
            if  cost_1 + cost_to_successor > cost_1_dic[i[0]]:
                    #
                continue
                
            node_check_1(Queue_1, i, path_start)
            
            
            
        if i[0] in path_start:
        
            cost_to_successor = i[2]
        
            if  cost_1 + cost_to_successor > cost_1_dic[i[0]]:
                    #
                continue
                
            node_check_1(Queue_1, i, path_start)
        
        

        cost_to_successor = i[2]
        
        cost_1_dic[i[0]] = cost_1 + cost_to_successor
        
        new_path = path_1 + [i[1]]
        
        new_cost = cost_1 + cost_to_successor
        
        optimal_cost = 2 * new_cost

        Queue_1.push((i[0], new_path, new_cost),(optimal_cost))
            

def util_func2(State_2, Queue_2, path_goal, cost_2, cost_2_dic, problem, path_2):
    for i in problem.getSuccessors(State_2):
    
        successor_present_2 = Queue_2.isthere(i[0])

        if successor_present_2:
        
            cost_to_successor = i[2]


            if  cost_2 + i[2] > cost_2_dic[i[0]]:
                continue
                
            node_check_2(Queue_2, i, path_goal)
            
        if i[0] in path_goal:


            if  cost_2 + i[2] > cost_2_dic[i[0]]:
                continue
                
            node_check_2(Queue_2, i, path_goal)

                         
        cost_to_successor = i[2]
        
        cost_2_dic[i[0]] = cost_2 + cost_to_successor
        
        new_path = path_2 + [i[1]]
        
        new_cost = cost_2 + cost_to_successor
        
        optimal_cost = 2 * new_cost

        Queue_2.push((i[0], new_path, new_cost), (optimal_cost))


def MM0(problem):
    

    cost_1, cost_2 = 0, 0

    Queue_1 = util.PriorityQueue()
    Queue_2 = util.PriorityQueue()
    
    start_state = problem.getStartState()
                                   
    Queue_1.push((start_state, [], 0), 2 * cost_1)
    
    goal_state = problem.goal
    
    Queue_2.push((goal_state, [], 0), 2 * cost_2)

    path_start = {}
    path_goal = {}
    
    
    
    cost_1_dic = {}
    cost_2_dic = {}
    
    
    
    start_state = problem.getStartState()
    
    
    cost_1_dic[start_state] = cost_1
    
    goal_state = problem.goal
    
    cost_2_dic[goal_state] = cost_2
    
   
    queue_1_empty = Queue_1.isEmpty()
    queue_2_empty = Queue_2.isEmpty()
    
    while (not Queue_1.isEmpty()) and (not Queue_2.isEmpty()):

        Mohil_1 = Queue_1.pop()
        Mohil_2 = Queue_2.pop()
        
        
        
        State_1, path_1, cost_1 = Mohil_1[0], Mohil_1[1], Mohil_1[2]
        State_2, path_2, cost_2 = Mohil_2[0], Mohil_2[1], Mohil_2[2]
        


        if State_1 == State_2:

            return path_1 + Reverse(path_2)
            
            
            
        min_cost = min(cost_1, cost_2)

        if (min_cost == cost_1):
        
            popped_node = Mohil_2
            
            optimal_cost_2 = 2 * cost_2
            
            Queue_2.push(popped_node, optimal_cost_2)
            
            popped_path = Mohil_1[0]
            
            path_start[popped_path] = path_1
#
            util_func(State_1, Queue_1, path_start, cost_1_dic, path_1, problem, cost_1)
                

        else:
        
            popped_node = Mohil_1
            
            optimal_cost_1 = 2 * cost_1
        
            Queue_1.push(popped_node, optimal_cost_1)
            
            popped_path = Mohil_2[0]
            
            path_goal[popped_path] = path_2
            

            util_func2(State_2, Queue_2, path_goal, cost_2, cost_2_dic, problem, path_2)
            
            
            
        if State_1 in path_goal:
        
            path_2 = path_goal[State_1]

            return path_1 + Reverse(path_2)
            
            
        if State_2 in path_start:
        
            path_1 = path_start[State_2]

            return path_1 + Reverse(path_2)


                

    return[]
    
    
    
    
    
    
  ################
  
#  ''' Heuristic bidirectional algorithm code starts here '''
#
#  ##############
        
            
    
def Reverse(p):

        path = []

        for path_2 in p:

            if path_2 == 'East':
                path_reverse = 'West'

            if path_2 == 'North':
                path_reverse = 'South'

            if path_2 == 'West':
                path_reverse = 'East'

            if path_2 == 'South':
                path_reverse = 'North'

            path.append(path_reverse)

        return path[::-1]


def node_check_1(Queue_1, i, path_start):

        if Queue_1.isthere(i[0]):
            node_present = i[0]
            Queue_1.remove_by_value(node_present)


        if i[0] in path_start:
            path_present = i[0]
            del path_start[path_present]

def node_check_2(Queue_2, i, path_goal):

        if Queue_2.isthere(i[0]):
            node_present = i[0]
            Queue_2.remove_by_value(node_present)

        elif i[0] in path_goal:
            path_present = i[0]
            del path_goal[path_present]


def util_func_3(State_1, Queue_1, path_start, cost_1_dic, path_1, problem, cost_1, heuristic):


    for i in problem.getSuccessors(State_1):

        h_1 = heuristic(i[0],problem)

        successor_present_1 = Queue_1.isthere(i[0])

        if successor_present_1:

            cost_to_successor = i[2]

            if  cost_1 + cost_to_successor > cost_1_dic[i[0]]:
                    #
                continue

            node_check_1(Queue_1, i, path_start)



        if i[0] in path_start:

            cost_to_successor = i[2]

            if  cost_1 + cost_to_successor > cost_1_dic[i[0]]:
                    #
                continue

            node_check_1(Queue_1, i, path_start)



        cost_to_successor = i[2]

        cost_1_dic[i[0]] = cost_1 + cost_to_successor

        new_path = path_1 + [i[1]]



        new_cost = h_1 + cost_1 + cost_to_successor

#

        optimal_cost = max(new_cost,2*(cost_1 + cost_to_successor))

        Queue_1.push((i[0], new_path, optimal_cost),(optimal_cost))


def util_func_4(State_2, Queue_2, path_goal, cost_2, cost_2_dic, problem, path_2, heuristic):
    for i in problem.getSuccessors(State_2):

        h_2 = heuristic(i[0],problem)

        successor_present_2 = Queue_2.isthere(i[0])

        if successor_present_2:

            cost_to_successor = i[2]


            if  cost_2 + i[2] > cost_2_dic[i[0]]:
                continue

            node_check_2(Queue_2, i, path_goal)

        if i[0] in path_goal:


            if  cost_2 + i[2] > cost_2_dic[i[0]]:
                continue

            node_check_2(Queue_2, i, path_goal)


        cost_to_successor = i[2]

        cost_2_dic[i[0]] = cost_2 + cost_to_successor

        new_path = path_2 + [i[1]]

        new_cost = h_2 + cost_2 + cost_to_successor



        optimal_cost = max(new_cost,2*(cost_2 + cost_to_successor))

        Queue_2.push((i[0], new_path, optimal_cost),(optimal_cost))


def MM(problem, heuristic=nullHeuristic):


    cost_1, cost_2 = 0, 0

    start_state = problem.getStartState()

    heuristic_1 = heuristic(start_state,problem)

    goal_state = problem.goal

    heuristic_2 = heuristic(goal_state, problem)

    Queue_1 = util.PriorityQueue()
    Queue_2 = util.PriorityQueue()



    Queue_1.push((start_state, [], 0), max(heuristic_1, 2 * cost_1))

    Queue_2.push((problem.goal, [], 0), max(heuristic_2, 2 * cost_2))

    path_start = {}
    path_goal = {}



    cost_1_dic = {}
    cost_2_dic = {}



    start_state = problem.getStartState()


    cost_1_dic[start_state] = cost_1

    goal_state = problem.goal

    cost_2_dic[goal_state] = cost_2


    queue_1_empty = Queue_1.isEmpty()
    queue_2_empty = Queue_2.isEmpty()

    while (not Queue_1.isEmpty()) and (not Queue_2.isEmpty()):

        Mohil_1 = Queue_1.pop()                 #CurrentPopF
        Mohil_2 = Queue_2.pop()                 #CurrentPopB



        State_1, path_1, cost_1 = Mohil_1[0], Mohil_1[1], Mohil_1[2]                     # Statef, pathF, gF
        State_2, path_2, cost_2 = Mohil_2[0], Mohil_2[1], Mohil_2[2]                     # Stateb, pathb, gb



        if State_1 == State_2:

            return path_1 + Reverse(path_2)



        min_cost = min(cost_1, cost_2)

        if (min_cost == cost_1):
        
            popped_node = Mohil_2

            optimal_cost_2 = 2 * cost_2

            Queue_2.push(popped_node, optimal_cost_2)

            popped_path = Mohil_1[0]

            path_start[popped_path] = path_1
#
            util_func_3(State_1, Queue_1, path_start, cost_1_dic, path_1, problem, cost_1, heuristic)


        else:

            popped_node = Mohil_1

            optimal_cost_1 = 2 * cost_1

            Queue_1.push(popped_node, optimal_cost_1)

            popped_path = Mohil_2[0]

            path_goal[popped_path] = path_2


            util_func_4(State_2, Queue_2, path_goal, cost_2, cost_2_dic, problem, path_2, heuristic)



        if State_1 in path_goal:

            path_2 = path_goal[State_1]

            return path_1 + Reverse(path_2)


        if State_2 in path_start:

            path_1 = path_start[State_2]

            return path_1 + Reverse(path_2)




    return[]



    
    
    
    
    
    ########################
    
    
    



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
#mm01 = biDirectionalSearchMM0
mm0 = MM0

mm = MM




