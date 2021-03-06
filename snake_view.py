"""
A view for the Snake game.

"""
import pygame
from time import sleep
from model import game_tile
from model import game_board
pygame.init()

class snake_view:
    """A view for a snake game. Takes in a read-only model"""

    def __init__(self, model):
        self.__WINDOW_WIDTH = 1250
        self.__WINDOW_HEIGHT = 750
        self.__win = pygame.display.set_mode((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT))
        self.__model = model
        self.font = pygame.font.Font('/Users/othurm/desktop/snake/Montserrat.otf', 32) 

    def draw_board(self):
        board = self.__model.get_board()
        for i, row in zip(range(0, len(board)), board):
            for j, tile in zip(range(0, len(row)), row):
                if(tile == game_tile.game_tile.EMPTY):
                    pygame.draw.rect(self.__win, (0, 0, 0), (25*j, 25*i, 25, 25))
                if(tile == game_tile.game_tile.SNAKE):
                    pygame.draw.rect(self.__win, (0, 255, 0), (25*j, 25*i, 25, 25))
                if(tile == game_tile.game_tile.TREAT):
                    pygame.draw.ellipse(self.__win, (0, 0, 255), (25*j, 25*i, 25, 25))
        text = self.font.render('Score: ' + str(self.__model.get_score()), True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        self.__win.blit(text, text_rect)
        sleep(.04)        
        print("finished loop")

    def display_end_game(self):
        text = self.font.render('Game Over!', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1250//2, 750//2)
        self.__win.blit(text, text_rect)
        pygame.display.update()

if __name__ == '__main__':
    view = snake_view(game_board.game_board())
    view.draw_board()