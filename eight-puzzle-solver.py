import heapq as heapq

# used for nodes pushed onto queue when path_costs are equal
insertion_counter = 0

# test cases
easy_puzzle = (0, 1, 2,
               4, 5, 3,
               7, 8, 6)

medium_puzzle = (1, 3, 6,
               5, 0, 7,
               4, 8, 2)

hard_puzzle = (7, 1, 2,
               4, 8, 5,
               6, 3, 0)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

class Node:
    def __init__(self, state, path_cost = 0):
        self.state = state
        self.path_cost = path_cost

# general search function made from Dr. Eamonn Keogh's pseudocode on initial assignment
def general_search(puzzle, queueing_function):
    nodes = make_queue(Node(puzzle))
    nodes_expanded = 0
    max_queue_size = 0

    while True:
        if len(nodes) > max_queue_size:
            max_queue_size = len(nodes)
        
        # return "failure" if no more nodes
        if not nodes:
            return "failure"

        node = remove_front(nodes)

        # prints puzzle
        print("\nExpanding next state: ")
        # get the side length of the puzzle
        n = int(len(node.state) ** 0.5)
        for i in range(0, len(node.state), n):
                print(node.state[i:i+n])

        # check if state is the goal state
        if goal_test(node.state):
            print(f"\nNumber of nodes expanded: {nodes_expanded}")
            print(f"Solution depth: {node.path_cost}")
            print(f"Maximum size of queue: {max_queue_size}")
            return node
        
        # expand node according to heuristic
        nodes = queueing_function(nodes, expand(node))
        nodes_expanded += 1

# creates a queue and pushes initial node
def make_queue(node):
    global insertion_counter
    queue = []
    heapq.heappush(queue, (node.path_cost, insertion_counter, node))
    insertion_counter += 1
    return queue

def remove_front(nodes):
    _,_, node = heapq.heappop(nodes)
    return node

def goal_test(state):
    if state == goal_state:
        return True

# get all node's children with the possible moves
def expand(node):
    children = []
    for state in possible_moves(node.state):
        children.append(Node(state, node.path_cost + 1))
    return children

# validates moves that can be done
def possible_moves(state):
    moves = []

    # find the index of the empty spot
    empty_spot = state.index(0)
    # get the side length of the puzzle
    n = int(len(state) ** 0.5)
    
    # move left
    if empty_spot % n != 0:
        moves.append(move(state, empty_spot, empty_spot - 1))
    # move right
    if empty_spot % n != n - 1:
        moves.append(move(state, empty_spot, empty_spot + 1))
    # move up
    if empty_spot >= n:
        moves.append(move(state, empty_spot, empty_spot - n))
    # move down
    if empty_spot < n * (n - 1):
        moves.append(move(state, empty_spot, empty_spot + n))
    
    return moves

def move(state, empty_spot, neighbor):
    new_state = list(state)
    temp = new_state[empty_spot]
    new_state[empty_spot] = new_state[neighbor]
    new_state[neighbor] = temp
    return tuple(new_state)

def uniform_cost_search(nodes, children):
    global insertion_counter
    for child in children:
        # pushes the lowest path cost
        heapq.heappush(nodes, (child.path_cost, insertion_counter, child))
        insertion_counter += 1
    return nodes

def astar_misplaced_tile(nodes, children):
    global insertion_counter
    for child in children:
        h = 0
        for i in range(len(child.state)):
            if (child.state[i] != goal_state[i] and child.state[i] != 0):
                h += 1
        # pushes the lowest sum of the path cost and number of misplaced tiles
        heapq.heappush(nodes, (child.path_cost + h, insertion_counter, child))
        insertion_counter += 1
    return nodes

def astar_manhattan_distance(nodes, children):
    global insertion_counter
    for child in children:
        # get the side length of the puzzle
        n = int(len(child.state) ** 0.5)
        h = 0
        for i in range(len(child.state)):
            if (child.state[i] != goal_state[i] and child.state[i] != 0):
                index = goal_state.index(child.state[i])
                h += abs((index - i) // n) + abs((index - i) % n)
        # pushes the lowest sum of the path cost and the distance from the current node to the goal state
        heapq.heappush(nodes, (child.path_cost + h, insertion_counter, child))
        insertion_counter += 1
    return nodes

def select_algorithm(puzzle):
    algorithm = input("\nChoose an algorithm: '1' for Uniform Cost Search, '2' for A* " +
    "with the Misplaced Tile Heuristic, or '3' for the A* with the Manhattan Distance Heuristic.\n")

    if algorithm == "1":
        general_search(puzzle, uniform_cost_search)
    if algorithm == "2":
        general_search(puzzle, astar_misplaced_tile)
    if algorithm == "3":
        general_search(puzzle, astar_manhattan_distance)

def main():
    puzzle_choice = input("Welcome to the Eight Puzzle Solver!\n" +
                          "Please select '1' if you want a default puzzle or '2' to input a custom puzzle.\n")
    
    # choose a default puzzle
    if puzzle_choice == "1":
        difficulty = input("\nChoose '1' for an easy puzzle, '2' for a medium puzzle, or '3' for a hard puzzle.\n")

        if difficulty == "1":
            select_algorithm(easy_puzzle)
        if difficulty == "2":
            select_algorithm(medium_puzzle)
        if difficulty == "3":
            select_algorithm(hard_puzzle)
    
    # input custom puzzle
    if puzzle_choice == "2":
        first_row = input("Please input the first row separated with spaces (0 as the empty spot): ")

        first_row = first_row.split()
        first_row_int = []

        for i in first_row:
            int_num = int(i)
            first_row_int.append(int_num)

        second_row = input("Please input the second row separated with spaces (0 as the empty spot): ")

        second_row = second_row.split()
        second_row_int = []

        for i in second_row:
            int_num = int(i)
            second_row_int.append(int_num)

        third_row = input("Please input the third row separated with spaces (0 as the empty spot): ")

        third_row = third_row.split()
        third_row_int = []

        for i in third_row:
            int_num = int(i)
            third_row_int.append(int_num)

        custom_puzzle = tuple(first_row_int + second_row_int + third_row_int)
        select_algorithm(custom_puzzle)

if __name__ == "__main__":
    main()