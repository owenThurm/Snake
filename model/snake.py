from orientation import orientation

class snake:

    def __init__(self):
        self.size = 3
        self.alive = True
        self.direction = orientation.EAST
        self.positions = [[5, 7], [6, 7], [7, 7]]

    def grow(self):
        self.size += 1
        self.update_head()

    def set_orientation(self, orientation):
        self.direction = orientation
               
    def move(self):
        del self.positions[0]
        self.update_head()
    
    def update_head(self):
        print('was called')
        head = self.positions[-1]
        if(self.direction == orientation.NORTH):
            self.positions.append([head[0], head[1] + 1])
        if(self.direction == orientation.EAST):
            self.positions.append([head[0] + 1, head[1]])
        if(self.direction == orientation.SOUTH):
            self.positions.append([head[0], head[1] - 1])
        if(self.direction == orientation.WEST):
            self.positions.append([head[0] - 1, head[1]])

    def is_snake_tile(self, tile_position):
        for position in self.positions:
            if(position == tile_position):
                return True
        return False    

