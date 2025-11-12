
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
        if self.__current > self.__max:
            self.__current = self.__max
            self.__complete = True
            return
        elif self.__current < self.__min:
            self.__current = self.__min
            self.__startline = True
            return
        if self.__current == self.__max:
            self.__complete = True
        else:
            self.__complete = False
        if self.__current == self.__min:
            self.__startline = True
        else:
            self.__startline = False
    def reset(self):
        self.current = self.min
    def normalize(self):
        return (self.current - self.min) / (self.max - self.min)
    @property
    def complete(self):
        self.act()
        return self.__complete
    @property
    def startline(self):
        self.act()
        return self.__startline
    @property
    def current(self):
        self.check()
        self.act()
        return self.__current + self.CURRENT_MODIFIER.total()
    @current.setter
    def current(self,value):
        if isinstance(value,int):
            self.__current = value
    @property
    def max(self):
        return self._check_max(self.__max + self.MAX_MODIFIER.total(),self.__min)
    @max.setter
    def max(self,value):
        if isinstance(value,int):
            self.__max = value
            self.check()
    @property
    def min(self):
        return self._check_min(self.__min + self.MIN_MODIFIER.total(),self.__max)
    @min.setter
    def min(self,value):
        if isinstance(value,int):
            self.__min = value
            self.check()
    @property
    def increase(self):
        return self.__increase + self.INCREASE_MODIFIER.total()
    @increase.setter
    def increase(self,value):
        if isinstance(value,int):
            self.__increase = value