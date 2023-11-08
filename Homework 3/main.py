from copy import deepcopy

class NumberScrabble:
    def __init__(self):
        self.state = [0] * 10  # Index 0 is unused for simplicity
        self.total_moves = 0
        self.player_a = []
        self.player_b = []
        self.turn = 'A'  # 'A' or 'B'
    
    def is_valid_move(self, number):
        return 1 <= number <= 9 and self.state[number] == 0
    
    def make_move(self, number):
        if self.is_valid_move(number):
            self.state[number] = 1
            if self.turn == 'A':
                self.player_a.append(number)
            else:
                self.player_b.append(number)
            self.total_moves += 1
            return True
        return False
    
    def swap_turns(self):
        self.turn = 'B' if self.turn == 'A' else 'A'
    
    def check_win(self, player_moves):
        for i in range(len(player_moves)):
            for j in range(i+1, len(player_moves)):
                for k in range(j+1, len(player_moves)):
                    if player_moves[i] + player_moves[j] + player_moves[k] == 15:
                        return True
        return False
    
    def is_win(self):
        if self.check_win(self.player_a):
            return 'A'
        if self.check_win(self.player_b):
            return 'B'
        return None
    
    def is_draw(self):
        return self.total_moves >= 9
    
    def get_possible_moves(self):
        return [i for i in range(1, 10) if self.state[i] == 0]
    
    def evaluate_heuristic(self):
        # Basic heuristic for demonstration purposes
        return len(self.player_b) - len(self.player_a)
    
    def minmax(self, depth, maximizing_player):
        if depth == 0 or self.is_win() or self.is_draw():
            return self.evaluate_heuristic(), None
        
        if maximizing_player:
            best_value = float('-inf')
            best_move = None
            for move in self.get_possible_moves():
                new_game_state = deepcopy(self)
                new_game_state.make_move(move)
                new_game_state.swap_turns()
                value, _ = new_game_state.minmax(depth - 1, False)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        else:
            best_value = float('inf')
            best_move = None
            for move in self.get_possible_moves():
                new_game_state = deepcopy(self)
                new_game_state.make_move(move)
                new_game_state.swap_turns()
                value, _ = new_game_state.minmax(depth - 1, True)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move

def main():
    game = NumberScrabble()
    
    while True:
        if game.turn == 'A':
            move = int(input(f"[A] choose a number: {game.get_possible_moves()} "))
        else:
            # Bot (player B) makes a move
            _, move = game.minmax(2, True)
            print(f"[B] chooses: {move}")
        
        if game.make_move(move):
            winner = game.is_win()
            if winner:
                print(f"[{winner}] wins the game!")
                break
            elif game.is_draw():
                print(f"Draw. No one wins.")
                break
        else:
            print(f"Invalid move: {move}")
        
        game.swap_turns()

if __name__ == "__main__":
    main()
