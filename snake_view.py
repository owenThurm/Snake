"""
A view for the Snake game.

"""
import pygame
from model import game_tile
pygame.init()

class snake_view:
    """A view for a snake game. Takes in a read-only model"""

    def __init__(self, model):
        self.__WINDOW_WIDTH = 1000
        self.__WINDOW_HEIGHT = 700
        self.__win = pygame.display.set_mode((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT))
        self.__model = model

    def draw_board(self):
        board = self.__model.get_board()
        for i, row in zip(range(0, len(board)), board):
            for j, tile in zip(range(0, len(row)), row):
                print(i)
                print(j)
                if(tile == game_tile.game_tile.EMPTY):
                    pygame.draw.rect(self.__win, (255, 0, 0), (25*i, 25*j, 25, 25))
                pygame.display.update()
        print("finished loop")