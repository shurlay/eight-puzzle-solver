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

def general_search(puzzle, queueing_function):
    nodes = make_queue(Node(puzzle))

    while True:
        if not nodes:
            return "failure"
        
        node = remove_front(nodes)

        if goal_test(node.state):
            return node
        
        nodes = queueing_function(nodes, expand(node))

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

def expand(node):
    children = []
    for state in possible_moves(node.state):
        children.append(Node(state, node.path_cost + 1))
    return children

def possible_moves(state):
    moves = []
    empty_spot = state.index(0)
    n = int(len(state) ** 0.5)

    if empty_spot % n != 0:
        moves.append.move(state, empty_spot, empty_spot - 1)
    if empty_spot % n != n - 1:
        moves.append.move(state, empty_spot, empty_spot + 1)
    if empty_spot >= n:
        moves.append.move(state, empty_spot, empty_spot - n)
    if empty_spot < n * (n - 1):
        moves.append.move(state, empty_spot, empty_spot + n)
    
    return moves

def move(state, empty_spot, neighbor):
    new_state = list(state)
    temp = new_state[empty_spot]
    new_state[empty_spot] = new_state[neighbor]
    new_state[neighbor] = temp
    return tuple(new_state)

def select_algorithm(puzzle):
    algorithm = input("Choose an algorithm: '1' for Uniform Cost Search, '2' for A* " +
    "with the Misplaced Tile Heuristic, or '3' for the A* with the Manhattan Distance Heuristic.\n")

    if algorithm == "1":
        general_search(puzzle, uniform_cost_search)
    if algorithm == "2":
        general_search(puzzle, misplaced_title)
    if algorithm == "3":
        general_search(puzzle, manhattan_distance)

def main():
    select_algorithm(test_puzzle)