
from lib.position import Pos
from lib.modifier import Modifier

class Camera:
    def __init__(self,position:Pos):
        self.__position = position
        self.__x_modifier = Modifier()
        self.__y_modifier = Modifier()
    @property
    def x(self):
        return self.__x_modifier(self.__position.x)
    @property
    def y(self):
        return self.__y_modifier(self.__position.y)
    @property
    def x_modifier(self):
        return self.__x_modifier
    @property
    def y_modifier(self):
        return self.__y_modifier
    def get_position(self):
        return Pos(self.x,self.y)
    def to_tuple(self):
        return (self.x,self.y)

CURRENT_CAMERA = Camera(Pos(0,0))
