
from lib.position import Pos

class Entity:
    def __init__(self,position:Pos) -> None:
        self.__position = position
        self.__speed = 1
    @property
    def position(self):
        return self.__position
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self,value):
        if isinstance(value,int):
            self.__speed = value
    def above(self,session):
        new_pos = self.position.above(1)
        for i in range(self.speed):
            if not session.can_move(new_pos):
                return
            new_pos = new_pos.above(1)
        self.position.movePos(self.position.above(self.speed))
    def below(self,session):
        new_pos = self.position.below(1)
        for i in range(self.speed):
            if not session.can_move(new_pos):
                return
            new_pos = new_pos.below(1)
        self.position.movePos(self.position.below(self.speed))
    def right(self,session):
        new_pos = self.position.right(1)
        for i in range(self.speed):
            if not session.can_move(new_pos):
                return
            new_pos = new_pos.right(1)
        self.position.movePos(self.position.right(self.speed))
    def left(self,session):
        new_pos = self.position.left(1)
        for i in range(self.speed):
            if not session.can_move(new_pos):
                return
            new_pos = new_pos.left(1)
        self.position.movePos(self.position.left(self.speed))
    def setSpeed(self,speed):
        self.__speed = speed