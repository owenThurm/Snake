import random
import math
from game_tile import game_tile
from snake import snake

class game_board:

    def __init__(self):
        self.snake = snake()
        self.init_board()

    def init_board(self):
        initial_treat_x = random.randrange(0, 20, 1)
        initial_treat_y = random.randrange(0, 15, 1)
        self.board = []
        for i in range(15):
            row = []
            for j in range(20):
                if(self.snake.is_snake_tile([j, i])):
                    row.append(game_tile.SNAKE)
                elif(i == initial_treat_x and j == initial_treat_y):
                    row.append(game_tile.TREAT)
                else:
                    row.append(game_tile.EMPTY)
            self.board.append(row)

    def game_state(self):
        for row in self.board:
            for tile in row:
                print(tile.value, end="")
            print()            

if __name__ == "__main__":
    snake_game = game_board()
    snake_game.game_state()     
    snake_game.snake.grow()
    snake_game.game_state()            
