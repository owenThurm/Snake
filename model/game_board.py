import random
import math
from model import game_tile
from model import snake
from model import orientation

class game_board:

    def __init__(self):
        self.__game_over = False
        self.__snake = snake.snake()
        self.__treat_location = [15, 7]
        self.__board = []
        self.__update_board()

    def get_board(self):
        return tuple(tuple(row) for row in self.__board)

    def set_snake_orientation(self, orientation):
        self.__snake.set_orientation(orientation)

    def __update_board(self):
        self.__board = []
        for i in range(30):
            row = []
            for j in range(50):
                if(self.__snake.is_snake_tile([j, i])):
                    row.append(game_tile.game_tile.SNAKE)
                elif(self.__treat_location[0] == j and self.__treat_location[1] == i):
                    row.append(game_tile.game_tile.TREAT)
                else:
                    row.append(game_tile.game_tile.EMPTY)
            self.__board.append(row)

    def game_state(self):
        for row in self.__board:
            for tile in row:
                print(tile.value, end="")
            print()          

    def spawn_treat(self):
        while(self.__snake.is_snake_tile(self.__treat_location)):
            self.__treat_location = [random.randrange(0, 50, 1), random.randrange(0, 30, 1)]

    def move_snake(self):
        if(self.__snake_off_board() or self.__snake_eating_self()):
            self.end_game()
        elif(self.__snake_about_to_get_treat()):
            self.__snake.grow()
            self.spawn_treat()
        else:
            self.__snake.move()
        self.__update_board()

    def __snake_off_board(self):
        head = self.__snake.get_head_position()
        if(head[0] >= 50 or head[1] >= 30 or head[0] < 0 or head[1] < 0):
            return True
        return False

    def __snake_eating_self(self):
        return not(len(self.__snake.get_snake_positions()) == len(set(self.__snake.get_snake_positions())))  

    def end_game(self):
        self.__game_over = True

    def is_game_over(self):
        return self.__game_over

    def __snake_about_to_get_treat(self):
        head = self.__snake.get_head_position()
        if(self.__snake.get_orientation() == orientation.orientation.NORTH and self.__treat_location == [head[0], head[1] + 1]):
            return True
        elif(self.__snake.get_orientation() == orientation.orientation.EAST and self.__treat_location == [head[0] + 1, head[1]]):
            return True
        elif(self.__snake.get_orientation() == orientation.orientation.SOUTH and self.__treat_location == [head[0], head[1] - 1]):
            return True
        elif(self.__snake.get_orientation() == orientation.orientation.WEST and self.__treat_location == [head[0] - 1, head[1]]):
            return True
        else:
            return False

if __name__ == "__main__":
    snake_game = game_board()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
    snake_game.move_snake()
    snake_game.game_state()
