"""
A controller for a snake game
"""
import pygame, sys
from model import game_board
from model import read_only_game_board
import snake_view
from pygame.locals import*

pygame.init()

class snake_controller:
    """A controller for a snake game"""

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        """runs a game of snake"""
        game_continues = True
        while game_continues:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_continues = False

            self.view.draw_board()
        pygame.quit()


if __name__ == '__main__':
    model = game_board.game_board()
    view = snake_view.snake_view(read_only_game_board.read_only_game_board(model))
    controller = snake_controller(model, view)
    controller.run()
