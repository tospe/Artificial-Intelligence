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
import copy

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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # initialize the search tree using the initial state of problem
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = []

    while not stack.isEmpty():
        # choose a leaf node for expansion
        state, actions = stack.pop()
        if state not in visited:
            visited.append(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                stack.push((successor, actions + [action]))
    return False

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    # initialize the search tree using the initial state of problem
    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    visited = []

    while not queue.isEmpty():
        # choose a leaf node for expansion
        state, actions = queue.pop()

        # if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(state):
            return actions

        # expand the node and add the resulting nodes to the search tree
        if state not in visited:
            visited.append(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    queue.push((successor, actions + [action]))
    return False

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #create a dictionary with the values
    info = dict()
    info['state'] = problem.getStartState()
    info['heuristicValue'] = 0 + heuristic(info['state'],problem)
    info['actionGetHere'] = ''
    
    #dictionary will be on the stack LIFO, it is the path to take
    stateStack = util.Stack()
    stateStack.push(info)
    
    #priority queue with the stacks, prioritized by the heuristic value 
    pQueue = util.PriorityQueue()
    pQueue.push(stateStack, info['heuristicValue'])

    isDone = 0
    winner = util.Stack()
    while not pQueue.isEmpty():
        bestPathOption = pQueue.pop()
        aux = bestPathOption.pop()
        presentState = aux['state']
        presentStateCost = aux['heuristicValue'] - heuristic(presentState,problem)
        # print("\n \n presentState")
        # print(aux)

        if problem.isGoalState(presentState):
            # print("ganhou")
            # print(presentState)
            # print(bestPathOption.list)
            bestPathOption.push(aux)
            winner.list = bestPathOption.list
            #print(bestPathOption.list)
            # pQueue.push(bestPathOption, info['heuristicValue'])
            
            # print("winner")
            # print(winner.list)
            break

        for successor, action, stepCost in problem.getSuccessors(presentState):
            # print("sucessor")
            # print(successor)
            if not any(i['state'] == successor for i in bestPathOption.list) and problem.getStartState() != successor:
                info = dict()
                info['state'] = successor
                info['heuristicValue'] = presentStateCost + stepCost + heuristic(info['state'],problem)
                info['actionGetHere'] = action
                
                #Create the copy operator
                reversedPath = util.Stack()
                while not bestPathOption.isEmpty():
                    item = bestPathOption.pop()
                    reversedPath.push(item)

                newPathOption = util.Stack()
                while not reversedPath.isEmpty():
                    item = reversedPath.pop()
                    bestPathOption.push(item)
                    newPathOption.push(item)

                newPathOption.push(aux)
                newPathOption.push(info)
                
                pQueue.push(newPathOption, info['heuristicValue'])
                
                if problem.isGoalState(info['state']):
                    isDone += 1
        isDone +=1

    actions = []
    bestPathOption = pQueue.pop()

    while not winner.isEmpty():
        info = winner.pop()
        if info['state'] != problem.getStartState():
            actions.insert(0, info['actionGetHere'])
    
    # while not bestPathOption.isEmpty():
    #     info = bestPathOption.pop()
    #     print(info)
    #     if info['state'] != problem.getStartState():
    #         actions.insert(0, info['actionGetHere'])
    print("actions to take")
    print(actions)
    return actions



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
