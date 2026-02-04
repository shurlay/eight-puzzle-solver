import heapq as heapq

test_puzzle = [[0, 1, 2],
               [4, 5, 3],
               [7, 8, 6]]

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

class Node:
    def __init__(self, state, path_cost = 0):
        self.state = state
        self.path_cost = path_cost
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def general_search(puzzle, queueing_function):
    nodes = make_queue(Node(puzzle))

    while True:
        if not nodes:
            return "failure"
        
        node = remove_front(nodes)

        if goal_test(node.state):
            return node
        
        nodes = queueing_function(nodes, expand(node, puzzle.operators))

def make_queue(node):
    queue = []
    heapq.heappush(queue, node)
    return queue

def remove_front(nodes):
    node = heapq.heappop(nodes)
    return node

def goal_test(state):
    if state == goal_state:
        return True

def possible_moves(state):
    moves = []
    empty_spot = state.index(0)
    # finish this


def select_algorithm(puzzle):
    algorithm = input("Choose an algorithm: '1' for Uniform Cost Search, '2' for A* " +
    "with the Misplaced Tile Heuristic, or '3' for the A* with the Manhattan Distance Heuristic.\n")

    if algorithm == "1":
        general_search(puzzle, 0)

def main():
    select_algorithm(test_puzzle)