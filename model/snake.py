from model import orientation

class snake:

    def __init__(self):
        self.__size = 3
        self.__direction = orientation.orientation.EAST
        self.__positions = [[5, 7], [6, 7], [7, 7]]

    def grow(self):
        self.__size += 1
        self.__update_head()

    def set_orientation(self, snake_orientation):
        if not self.__opposite_directions(snake_orientation):    
            self.__direction = snake_orientation

    def __opposite_directions(self, snake_orientation):
        return (snake_orientation == orientation.orientation.NORTH and self.__direction == orientation.orientation.SOUTH) or (snake_orientation == orientation.orientation.SOUTH and self.__direction == orientation.orientation.NORTH) or (snake_orientation == orientation.orientation.EAST and self.__direction == orientation.orientation.WEST) or (snake_orientation == orientation.orientation.WEST and self.__direction == orientation.orientation.EAST)
               
    def get_orientation(self):
        return self.__direction

    def move(self):
        del self.__positions[0]
        self.__update_head()

    def get_head_position(self):
        return self.__positions[-1]

    def get_snake_positions(self):
        return tuple(tuple(row) for row in self.__positions)
    
    def __update_head(self):
        head = self.__positions[-1]
        if(self.__direction == orientation.orientation.NORTH):
            self.__positions.append([head[0], head[1] - 1])
        elif(self.__direction == orientation.orientation.EAST):
            self.__positions.append([head[0] + 1, head[1]])
        elif(self.__direction == orientation.orientation.SOUTH):
            self.__positions.append([head[0], head[1] + 1])
        elif(self.__direction == orientation.orientation.WEST):
            self.__positions.append([head[0] - 1, head[1]])

    def is_snake_tile(self, tile_position):
        for position in self.__positions:
            if(position == tile_position):
                return True
        return False    

