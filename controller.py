import sys
sys.path.insert(1, '/Users/othurm/desktop/snake/model')
import game_board





class snake_controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        game_continues = True
        while(game_continues):
            self.view.repaint()


if __name__ == '__main__':
    model = game_board()
    view = snake_view()
    controller = snake_controller(model, view)
    controller.run()
