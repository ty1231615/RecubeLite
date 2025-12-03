
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
        new_pos = self.position
        for i in range(self.speed):
            if not session.can_move(new_pos.above(1)):
                break
            self.position.movePos(new_pos.above(1))
            session.on_move(self)
    def below(self,session):
        new_pos = self.position
        for i in range(self.speed):
            if not session.can_move(new_pos.below(1)):
                break
            self.position.movePos(new_pos.below(1))
            session.on_move(self)
    def right(self,session):
        new_pos = self.position
        for i in range(self.speed):
            if not session.can_move(new_pos.right(1)):
                break
            self.position.movePos(new_pos.right(1))
            session.on_move(self)
    def left(self,session):
        new_pos = self.position
        for i in range(self.speed):
            if not session.can_move(new_pos.left(1)):
                break
            self.position.movePos(new_pos.left(1))
            session.on_move(self)
    def setSpeed(self,speed):
        self.__speed = speed