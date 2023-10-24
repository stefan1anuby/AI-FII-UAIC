import copy

class Board:

    def __init__(self, initial_state , last_move = -1):
        self.state = initial_state
        self.last_move = last_move

    def is_goal(self):
        current_state = [item for sublist in self.state for item in sublist if item != 0]
        return current_state == [1, 2, 3, 4, 5, 6, 7, 8]
    
    def possible_moves(self):
        moves = []
        
        # searches for position of 0
        for index, row in enumerate(self.state):
            if 0 in row:
                x0,y0 = index, row.index(0)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

        for direction in directions:
            x,y = (x0 + direction[0], y0 + direction[1])
            if 0 <= x < 3 and 0 <= y < 3:
                if self.last_move != self.state[x][y]:
                    moves.append((x,y))
        return moves
    
    def make_move(self, pos):
        x,y = pos

        #verifici sa nu faci mutare cu "conflicte"
        if self.last_move == self.state[x][y]:
            return None
        
        x0,y0 = [(index, row.index(0)) for index, row in enumerate(self.state) if 0 in row][0]

        self.last_move = self.state[x][y]
        
        new_state = copy.deepcopy(self.state)
        new_state[x0][y0], new_state[x][y] = new_state[x][y], new_state[x0][y0]
        
        return Board(new_state,self.last_move)
    
    def print_state(self , message = "The state is :"):
        print(message)
        [[[print(self.state[i][j], end=" ") for j in range(len(self.state[0]))] and print(" ")] for i in range(len(self.state))]

def iddfs(root, max_depth):
    for depth in range(max_depth):
        found = dls(root, depth)
        if found is not None:
            return found
    return None

def dls(node, depth):
    if depth == 0 and node.is_goal():
        return node
    elif depth > 0:
        for move in node.possible_moves():
            next_node = node.make_move(move)
            found = dls(next_node, depth - 1)
            if found is not None:
                return found
    return None

def greedy_search(puzzle, heuristic_func):
    visited = set()
    queue = [puzzle]

    while queue:
        current_state = min(queue, key=heuristic_func)
        queue.remove(current_state)

        if current_state.is_goal():
            return current_state

        for move in current_state.possible_moves():
            next_state = current_state.make_move(move)
            if str(next_state.state) not in visited:
                visited.add(str(next_state.state))
                queue.append(next_state)

    return None

def manhattan_distance(board):
        distance = 0
        for i in range(3):
            for j in range(3):
                if board.state[i][j] == 0:
                    continue
                correct_i, correct_j = (board.state[i][j]-1) // 3, (board.state[i][j]-1) % 3
                distance += abs(correct_i - i) + abs(correct_j - j)
        return distance

def hamming_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board.state[i][j] == 0:
                continue
            if board.state[i][j] != i * 3 + j + 1:
                distance += 1
    return distance

def main():
    print("Calling main")

if __name__ == '__main__':
    main()