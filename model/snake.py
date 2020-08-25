from orientation import orientation

class snake:

    def __init__(self):
        self.__size = 3
        self.__direction = orientation.EAST
        self.__positions = [[5, 7], [6, 7], [7, 7]]

    def grow(self):
        self.__size += 1
        self.__update_head()

    def set_orientation(self, orientation):
        self.__direction = orientation
               
    def get_orientation(self):
        return self.__direction

    def move(self):
        del self.__positions[0]
        self.__update_head()

    def get_head_position(self):
        return self.__positions[-1]

    def get_snake_positions(self):
        return self.__positions
    
    def __update_head(self):
        head = self.__positions[-1]
        if(self.__direction == orientation.NORTH):
            self.__positions.append([head[0], head[1] + 1])
        elif(self.__direction == orientation.EAST):
            self.__positions.append([head[0] + 1, head[1]])
        elif(self.__direction == orientation.SOUTH):
            self.__positions.append([head[0], head[1] - 1])
        elif(self.__direction == orientation.WEST):
            self.__positions.append([head[0] - 1, head[1]])

    def is_snake_tile(self, tile_position):
        for position in self.__positions:
            if(position == tile_position):
                return True
        return False    

