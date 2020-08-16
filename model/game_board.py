import random
import math
from game_tile import game_tile
from snake import snake
from orientation import orientation

class game_board:

    def __init__(self):
        self.__game_over = False
        self.__snake = snake()
        self.__treat_location = [15, 7]
        self.__update_board()

    def __update_board(self):
        self.board = []
        for i in range(15):
            row = []
            for j in range(20):
                if(self.__snake.is_snake_tile([j, i])):
                    row.append(game_tile.SNAKE)
                elif(self.treat_location[0] == j and self.treat_location[1] == i):
                    row.append(game_tile.TREAT)
                else:
                    row.append(game_tile.EMPTY)
            self.board.append(row)

    def game_state(self):
        for row in self.board:
            for tile in row:
                print(tile.value, end="")
            print()          

    def spawn_treat(self):
        while(self.__snake.is_snake_tile(self.__treat_location)):
            self.treat_location = [random.randrange(0, 20, 1), random.randrange(0, 15, 1)]

    def move_snake(self):
        if(self.__snake_off_board()):
            self.end_game()
        elif(self.__snake_about_to_get_treat()):
            self.__snake.grow()
            self.spawn_treat()
        else:
            self.__snake.move()
        self.__update_board()

    def __snake_off_board(self):
        head = self.__snake.get_head_position()
        if(head[0] >= 20 or head[1] >= 15):
            return True
        return False

    def __snake_eating_self(self):
        return not(len(self.__snake.get_snake_positions()) == len(set(self.__snake.get_snake_positions())))  

    def end_game(self):
        self.game_over = True

    def is_game_over(self):
        return self.game_over

    def __snake_about_to_get_treat(self):
        head = self.__snake.get_head_position()
        if(self.__snake.get_orientation() == orientation.NORTH and self.treat_location == [head[0], head[1] + 1]):
            return True
        elif(self.__snake.get_orientation() == orientation.EAST and self.treat_location == [head[0] + 1, head[1]]):
            return True
        elif(self.__snake.get_orientation() == orientation.SOUTH and self.treat_location == [head[0], head[1] - 1]):
            return True
        elif(self.__snake.get_orientation() == orientation.WEST and self.treat_location == [head[0] - 1, head[1]]):
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
