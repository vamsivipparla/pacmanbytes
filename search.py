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
            
        if i[0] in path_goal:
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
        
            
    

                  



class BiDirectionalNode:
    def __init__(self, position, actions, cost=0, h=0, pr=0):
        self.pos = position
        self.actions = actions
        self.cost = cost
        self.f = self.cost + h
        self.priority = pr


def Rev(actions):
    """
    Takes the path of actions from backward search, flips it and mirrors the directions to make sense
    from the middle point (where the two frontiers meet) onwards
    :param actions: List of actions to reach to the middle point from goal
    :return: list of actions to reach to the goal from the middle point
    
    
    """
    
    actions_reverse = reversed(actions)
    
    list_reverse = list(reversed(actions))
    
    reversed_actions = list_reverse     # reverse the actions
    
    reverse_directions = {'East': 'West',
    'South': 'North',
    'North': 'South',
    'West': 'East'}
    
    
    reversed_actions = [reverse_directions[i] for i in reversed_actions]  # reverse the directions

    return reversed_actions
    
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
    
def func1(forward_map, position, forward_queue2, presentnode, forward_ffunction, forward_gfunction):
            if position not in forward_map:
                forward_map = forward_map
            
            if position in forward_map:
                
                forward_map.pop(position)
                
            forward_ffunction.noderemove(presentnode)
            
            
            
            forward_queue2[position] = presentnode
            
            forward_gfunction.noderemove(presentnode)

            
            
def func2(node_at_now,presentnode,c_cost,problem,c_action):
                    

                    # else update the cost
                    cost = presentnode.cost + c_cost
                    
                    node_at_now.cost = (cost)
                    
                    heuristic_cost = heuristic(node_at_now.pos, problem)
                    
                    node_at_now.f = node_at_now.cost + heuristic_cost
                    
                    current_action = presentnode.actions[:]
                    
                    updated_action = current_action + [c_action]
                    
                    node_at_now.actions = updated_action
                    
def func3(node_at_now, forward_queue, forward_map, forward_ffunction,forward_gfunction, temp_state):
                f_priority = node_at_now.f
                
                forward_ffunction.push(node_at_now, f_priority)
                
                g_priority = node_at_now.cost
                
                forward_gfunction.push(node_at_now, g_priority)
                
                fwd_priority = node_at_now.priority

                forward_queue.push(node_at_now, fwd_priority)
                
                forward_map[temp_state] = node_at_now
                
                
def func5(forward_map,forward_ffunction,forward_gfunction,forward_queue2, temp_state):

                    if temp_state in forward_map:
                        if temp_state not in forward_queue2:
                            forward_map.pop(temp_state)
                            
                    if temp_state not in forward_map:
                        if temp_state not in forward_queue2:
                            forward_map = forward_map
                            forward_queue2 = forward_queue2
                            
                    if temp_state in forward_queue2:
                        if temp_state not in forward_map:
                            forward_queue2.pop(temp_state)
                            
                    forward_ffunction.noderemove(node_at_now)
                    forward_gfunction.noderemove(node_at_now)
                        
def func7(backward_map, position, backward_queue2, presentnode, backward_ffunction, backward_gfunction):
            
            if position not in backward_map:
                backward_map = backward_map
            
            if position in backward_map:
                backward_map.pop(position)
                
            backward_ffunction.noderemove(presentnode)
          
            backward_queue2[position] = presentnode
            
            backward_gfunction.noderemove(presentnode)
            
def func8(backward_map, temp_state, backward_queue2, backward_ffunction, backward_gfunction):
                    if temp_state in backward_map:
                        if temp_state not in backward_queue2:
                        
                            backward_map.pop(temp_state)
                            
                    if temp_state in backward_queue2:
                        if temp_state not in backward_map:
                        
                            backward_queue2.pop(temp_state)
                            
                    if temp_state not in backward_map:
                        if temp_state not in backward_queue2:
                            backward_map = backward_map
                            backward_queue2 = backward_queue2

                    backward_ffunction.noderemove(node_at_now)
                    backward_gfunction.noderemove(node_at_now)
def func9(presentnode, c_cost, node_at_now, heuristic, problem, list_reverse, c_action):
                    current_cost = presentnode.cost
                    
                    total_cost = current_cost + c_cost
                    
                    node_at_now.cost = total_cost
                    
                    heuristic_cost = heuristic(node_at_now.pos, problem, list_reverse)
                    
                    node_at_now.f = node_at_now.cost + heuristic_cost
                    
                    current_action = presentnode.actions[:]
                    
                    total_action = current_action + [c_action]
                    
                    node_at_now.actions = total_action
                    
def func10(backward_queue, node_at_now, temp_state, backward_map, backward_ffunction, backward_gfunction):
                backward_queue.push(node_at_now, node_at_now.priority)
                backward_map[temp_state] = node_at_now
                backward_ffunction.push(node_at_now, node_at_now.f)
                backward_gfunction.push(node_at_now, node_at_now.cost)
                


def bidirectional_search2(problem, heuristic=nullHeuristic):

    
    
    
    list_reverse = {'rev': False}
    
    U = float('inf')
    eps = 1

    forward_queue, backward_queue = util.PriorityQueue(), util.PriorityQueue()
    forward_map, backward_map = dict(), dict()
    forward_queue2, backward_queue2 = dict(), dict()

   

    forward_gfunction, backward_gfunction, forward_ffunction, backward_ffunction = util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue(), util.PriorityQueue()
    

                   

    start = problem.getStartState()
    
    

    
    list_reverse['rev'] = False
    
    start_heuristic = heuristic(start, problem, list_reverse)
    
    start_node = BiDirectionalNode(start, [], 0, start_heuristic, 0)
    
    goal = problem.goal
    list_reverse['rev'] = True
    
    goal_heuristic = heuristic(goal, problem, list_reverse)
    goal_node = BiDirectionalNode(goal, [], 0, goal_heuristic, 0)
    
    result = []

    
    forward_priority = start_node.priority
    
    forward_queue.push(start_node, forward_priority)
    
    backward_priority = goal_node.priority
    
    backward_queue.push(goal_node, backward_priority)
    
    
    forward_map[start] = start_node
    backward_map[goal] = goal_node
    
    forward_f = start_node.f
    forward_ffunction.push(start_node, forward_f)
    
    backward_f = goal_node.f
    backward_ffunction.push(goal_node, backward_f)
    
    forward_g = start_node.cost
    forward_gfunction.push(start_node, start_node.cost)
    
    backward_g = goal_node.cost
    backward_gfunction.push(goal_node, goal_node.cost)

    
   

        
    end_f = None
    end_b = None

    # the bidirectional search begins
    
    while not forward_queue.isEmpty():
    
        while not backward_queue.isEmpty():
        
            C = min(forward_queue.checktop().priority, backward_queue.checktop().priority)
            
            if U <= C:
                return result

            
            fwd_f = forward_ffunction.checktop().f
            back_f = backward_ffunction.checktop().f
            
            fwd_g = forward_gfunction.checktop().cost
            back_g = backward_gfunction.checktop().cost
            
            total = fwd_g + back_g + eps
            
            
            if U <= max(C, fwd_f, back_f, total):
            
                fwd_open = len(forward_map)
                back_open = len(backward_map)
                
                open_nodes = fwd_open + back_open + 1
                
                fwd_closed = len(forward_queue2)
                back_closed = len(backward_queue2)
                
                closed_nodes =  fwd_closed + back_closed

                

                return result

            # safe to stop
            

            # begin forward search
            f_priority = forward_queue.checktop().priority
            
            if C == f_priority:
            
                end_f = forward_queue.pop()
                
                presentnode = end_f
                
                position = presentnode.pos

                
                func1(forward_map, position, forward_queue2, presentnode, forward_ffunction, forward_gfunction)
    #
                children = problem.getSuccessors(position)
                
                for c in children:
                
                    temp_state, c_action, c_cost = c
                    node_at_now = None

                    if temp_state in forward_map:
                        if temp_state not in forward_queue2:
                        
                            node_at_now = forward_map[temp_state]
                            
                    elif temp_state in forward_queue2:
                        if temp_state not in forward_map:
                        
                            node_at_now = forward_queue2[temp_state]
                            
                    elif temp_state not in forward_map:
                        if temp_state not in forward_queue2:
                            
                            node_at_now = None

                   
                    
                    
                    if node_at_now is not None:
                        
                        current_cost = presentnode.cost
                        total_cost = current_cost + c_cost
                        
                        cost = node_at_now.cost
                        
                        if cost <= total_cost:
                            continue

                        
                        forward_queue.noderemove(node_at_now)

                        func5(forward_map, forward_ffunction, forward_gfunction, forward_queue2, temp_state)


                        func2(node_at_now,presentnode,c_cost,problem,c_action)
    #

                    elif node_at_now is None:
                    
                        current_action = presentnode.actions[:]
                        
                        new_action = [c_action]
                        
                        total_action = current_action + new_action
                        
                        action_at_nows = total_action
                        
                        current_cost = presentnode.cost
                        
                        new_cost = c_cost
                        
                        total_cost = current_cost + new_cost
                        
                        cost_at_now = total_cost
                        
                        heur = heuristic(temp_state, problem)
                        
                        max_cost = max(heur, cost_at_now)
                        
                        priority_cost = cost_at_now + max_cost

                        this_priority = priority_cost

                        node_at_now = BiDirectionalNode(temp_state, action_at_nows, cost_at_now, heur, this_priority)

                    func3(node_at_now, forward_queue, forward_map, forward_ffunction,forward_gfunction, temp_state)
    #

                    
                    if temp_state in backward_map:
                    
                        back_node = backward_map[temp_state]
                        
                        cost = node_at_now.cost
                        back_cost = back_node.cost
                        
                        cost_2 = cost + back_cost
                        
                        total_cost = cost_2
                        
                        U = min(U, total_cost)

                        back_actions = Rev(back_node.actions)
                        
                        action = node_at_now.actions[:]
                        
                        result = action + back_actions

                        
                       
            # end forward search

            # begin backward search
            else:
                
                
               
    #
                
                
                end_b = backward_queue.pop()
                presentnode = end_b
                
                position = presentnode.pos
                
                func7(backward_map, position, backward_queue2, presentnode, backward_ffunction, backward_gfunction)

    #
                
                children = problem.getSuccessors(position)
                
                for c in children:
                    temp_state, c_action, c_cost = c
                    node_at_now = None
                    
                    if temp_state in backward_map:
                        if temp_state not in backward_queue2:
                        
                            node_at_now = backward_map[temp_state]
                            
                    elif temp_state in backward_queue2:
                        if temp_state not in backward_map:
                        
                            node_at_now = backward_queue2[temp_state]
                            
                    elif temp_state not in backward_map:
                        if temp_state not in backward_queue2:
                            
                            node_at_now = None
                    
                    

                    if node_at_now is not None:
                    
                        current_cost = presentnode.cost
                        total_cost = current_cost + c_cost
                        
                        cost = node_at_now.cost
                        
                        if cost <= total_cost:
                            continue
                       
                        backward_queue.noderemove(node_at_now)
                        
                        func8(backward_map, temp_state, backward_queue2, backward_ffunction, backward_gfunction)
    #

                        list_reverse['rev'] = True
                        func9(presentnode, c_cost, node_at_now, heuristic, problem, list_reverse, c_action)
    #
                    else:
                        current_action = presentnode.actions[:]
                        
                        new_action = [c_action]
                        
                        total_action = current_action + new_action
                        
                        action_at_nows = total_action
                        
                        current_cost = presentnode.cost
                        
                        new_cost = c_cost
                        
                        total_cost = current_cost + new_cost
                        
                        cost_at_now = total_cost
                        
                        list_reverse['rev'] = True
                        
                        heur = heuristic(temp_state, problem, list_reverse)
                        
                        max_cost = max(heur, cost_at_now)
                        
                        priority_cost = cost_at_now + max_cost

                        this_priority = priority_cost

                        node_at_now = BiDirectionalNode(temp_state, action_at_nows, cost_at_now, heur, this_priority)
                        
                        
                        
                        
                    func10(backward_queue, node_at_now, temp_state, backward_map, backward_ffunction, backward_gfunction)
    #

                    if temp_state in forward_map:
                    
                        front_node = forward_map[temp_state]
                        
                        cost = node_at_now.cost
                        front_cost = front_node.cost
                        cost_2 = cost + front_cost
                        
                        total_cost = cost_2
                        
                        U = min(U, total_cost)

                        back_actions = Rev(node_at_now.actions)
                        
                        front_actions = front_node.actions[:]
                        
                        
                        result = front_actions + back_actions

                    
                   
        # end backward search

   
    if end_f is not None:
        if end_b is not None:
        
            back_actions = Rev(end_b.actions)

            return end_f.actions + back_actions





bdmm = bidirectional_search2


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
#mm01 = biDirectionalSearchMM0
mm0 = MM0






