class NumberScrabble:
    def __init__(self):
        self.state = [0] * 10   # chosen numbers
        self.total_moves = 0    # total number of moves / used for draw check
        self.player_a = []      # numbers chosen by a
        self.player_b = []      # numbers chosen by b
        self.turn = 0           # 0 = a | 1 = b
    
    def is_valid_move(self, number):
        return 1 <= number <= 9 and self.state[number] == 0
    
    def get_possible_moves(self):
        return [i for i in range(1, 10) if self.state[i] == 0]
    
    def make_move(self, number):
        if self.is_valid_move(number):
            self.state[number] = 1
            
            match (self.turn):
                case 0:
                    self.player_a.append(number)
                case 1:
                    self.player_b.append(number)
                    
            self.total_moves += 1
            return True
        return False
    
    def swap_turns(self):
        self.turn = not self.turn
    
    def is_win(self):
        match (self.turn):
            case 0:
                playerToCheck = self.player_a
            case 1:
                playerToCheck = self.player_b
        
        for i in range(len(playerToCheck)):
            for j in range(i+1, len(playerToCheck)):
                for k in range(j+1, len(playerToCheck)):
                    if playerToCheck[i] + playerToCheck[j] + playerToCheck[k] == 15:
                        return True
        return False
    
    def is_draw(self):
        return self.total_moves == 9

def main():
    game = NumberScrabble()
    
    while (True):
        match (game.turn):
            case 0:
                move = int(input(f"[A] choose a number: {game.get_possible_moves()} "))
            case 1:
                move = int(input(f"[B] choose a number: {game.get_possible_moves()} "))
                
        if game.make_move(move):
            if game.is_win():
                match (game.turn):
                    case 0:
                        print(f"[A] wins the game!")
                    case 1:
                        print(f"[B] wins the game!")
                break
            if game.is_draw():
                print(f"Draw. No one wins.")
                break
            else:
                game.swap_turns()

if __name__ == "__main__":
    main()