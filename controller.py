"""
A controller for a snake game
"""
import pygame, sys
from model import orientation
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
                keys = pygame.key.get_pressed()

                if keys[pygame.K_UP]:
                    print('UP!')
                    self.model.set_snake_orientation(orientation.orientation.NORTH)
                if keys[pygame.K_LEFT]:
                    print('LEFT!')
                    self.model.set_snake_orientation(orientation.orientation.WEST)
                if keys[pygame.K_RIGHT]:
                    print('RIGHT!')
                    self.model.set_snake_orientation(orientation.orientation.EAST)
                if keys[pygame.K_DOWN]:
                    print('DOWN!')
                    self.model.set_snake_orientation(orientation.orientation.SOUTH)
            if self.model.is_game_over():
                self.view.display_end_game()
            else:
                self.view.draw_board()
                pygame.display.update()
                self.model.move_snake()
        pygame.quit()
        


if __name__ == '__main__':
    model = game_board.game_board()
    view = snake_view.snake_view(read_only_game_board.read_only_game_board(model))
    controller = snake_controller(model, view)
    controller.run()
