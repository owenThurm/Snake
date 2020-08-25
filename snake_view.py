"""
A view for the Snake game.

"""
import pygame
pygame.init()

class snake_view:

    def __init__(self):
        self.__WINDOW_WIDTH = 1000
        self.__WINDOW_HEIGHT = 700
        self.__win = pygame.display.set_mode((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT))
        


if __name__ == '__main__':
    snake_view = snake_view()



