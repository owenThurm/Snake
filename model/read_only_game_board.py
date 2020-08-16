

class read_only_game_board:

    def __init__(self, game_board):
        self.__game_board = game_board


    def get_board(self):
        return self.__game_board.get_board()

    def is_game_over(self):
        return self.__game_board.is_game_over()

    
    
