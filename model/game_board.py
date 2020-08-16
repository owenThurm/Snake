import random
import math
from game_tile import game_tile


class game_board:

    def __init__(self):
        initial_treat_x = random.randrange(0, 20, 1)
        initial_treat_y = random.randrange(0, 15, 1)
        self.board = []
        for i in range(15):
            row = []
            for j in range(20):
                if(i == initial_treat_x and j == initial_treat_y):
                    row.append(game_tile.TREAT)
                else:
                    row.append(game_tile.EMPTY)
            self.board.append(row)

if __name__ == "__main__":
    snake_game = game_board()
    print(snake_game.board)                       
