
from lib.modifier import Modifier

class Progress:
    def __init__(self,current:int,max:int,min:int,increase:int) -> None:
        self.__current = current
        self.__max = max
        self.__min = min
        self.__increase = increase
        self.__current_modifier = Modifier()
        self.__max_modifier = Modifier()
        self.__min_modifier = Modifier()
        self.__increase_modifier = Modifier()
        self.__complete = False
        self.__startline = False
        self.check()
        self.act()
    @property
    def CURRENT_MODIFIER(self):
        return self.__current_modifier
    @property
    def MAX_MODIFIER(self):
        return self.__max_modifier
    @property
    def MIN_MODIFIER(self):
        return self.__min_modifier
    @property
    def INCREASE_MODIFIER(self):
        return self.__increase_modifier
    def next(self):
        self.__current += self.__increase
        self.act()
    def back(self):
        self.__current -= self.__increase
        self.act()
    def check(self):
        # 最大値が最小値を下回ってはいけないのでその場合は最小値で固定する
        if self.min > self.max:
            self.max = self.min
    def _check_max(self, max, min):
        if max < min:
            return min
        return max
    def _check_min(self, min, max):
        if min > max:
            return max
        return min
    def act(self):
        if self.current > self.max:
            self.__current = self.max
            self.__complete = True
            return
        elif self.current < self.min:
            self.__current = self.min
            self.__startline = True
            return
        if self.current == self.max:
            self.__complete = True
        else:
            self.__complete = False
        if self.current == self.min:
            self.__startline = True
        else:
            self.__startline = False
    def reset(self):
        self.current = self.min
    def reset_modifier(self):
        self.CURRENT_MODIFIER.clear()
        self.MAX_MODIFIER.clear()
        self.MIN_MODIFIER.clear()
    @classmethod
    def Normalize(cls,max,min,current):
        # protect against division by zero when max == min
        denom = (max - min)
        if denom == 0:
            # if no range, return 1.0 when at or beyond max, otherwise 0.0
            return 1.0 if current >= max else 0.0
        return (current - min) / denom
    def normalize(self):
        return Progress.Normalize(self.max,self.min,self.current)
    @property
    def complete(self):
        self.act()
        return self.__complete
    @complete.setter
    def complete(self,value):
        if isinstance(value,bool):
            self.__complete = value
        else:
            raise TypeError("ブール値が期待されます")
    @property
    def startline(self):
        self.act()
        return self.__startline
    @startline.setter
    def startline(self,value):
        if isinstance(value,bool):
            self.__startline = value
        else:
            raise TypeError("ブール値が期待されます")
    @property
    def current(self):
        self.check()
        return self.__current_modifier(self.__current)
    @current.setter
    def current(self,value):
        if isinstance(value,int):
            self.__current = value
    @property
    def max(self):
        return self._check_max(self.MAX_MODIFIER(self.__max),self.__min)
    @max.setter
    def max(self,value):
        if isinstance(value,int):
            self.__max = value
            self.check()
    @property
    def min(self):
        return self._check_min(self.MIN_MODIFIER(self.__min),self.__max)
    @min.setter
    def min(self,value):
        if isinstance(value,int):
            self.__min = value
            self.check()
    @property
    def increase(self):
        return self.INCREASE_MODIFIER(self.__increase)
    @increase.setter
    def increase(self,value):
        if isinstance(value,int):
            self.__increase = value