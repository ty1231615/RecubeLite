
import math

class Pos:
    def __init__(self,x,y) -> None:
        self.__x = x
        self.__y = y
        self.__lock = False
    def value_error(self):
        raise ValueError("整数以外は適切ではありません")
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,value):
        if not self.__lock:
            if isinstance(value,int):
                self.__x = value
            else:
                self.value_error()
        else:
            raise Exception("このPositionはロックされています")
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,value):
        if not self.__lock:
            if isinstance(value,int):
                self.__y = value
            else:
                self.value_error()
        else:
            raise Exception("このPositionはロックされています")
    def above(self,increase):
        return Pos(self.x,self.y - increase)
    def below(self,increase):
        return Pos(self.x,self.y + increase)
    def right(self,increase):
        return Pos(self.x + increase, self.y)
    def left(self,increase):
        return Pos(self.x - increase,self.y)
    def move(self,x,y):
        self.x = x
        self.y = y
    def lock(self):
        self.__lock = True
    def unlock(self):
        self.__lock = False
    def movePos(self,pos):
        if isinstance(pos,Pos):
            self.x = pos.x
            self.y = pos.y
    def plus(self,x,y):
        return Pos(self.x + x, self.y + y)
    def equals(self,pos):
        if isinstance(pos,Pos):
            return pos.x == self.x and pos.y == self.y
        return False
    def toTuple(self):
        return (self.x,self.y)
    def distanceTo(self, to) -> float:
        if isinstance(to, Pos):
            return math.sqrt(pow(to.x - self.x,2) + pow(to.y - self.y,2))
        raise TypeError("引数にはPosが期待されます")
    def subtract(self,pos):
        if isinstance(pos,Pos):
            return Pos(self.x - pos.x, self.y - pos.y)
        raise TypeError("引数にはPosが期待されます")
    def multiple(self,x,y):
        return Pos(self.x * x, self.y * y)
    def copy(self):
        return Pos(self.x,self.y)
