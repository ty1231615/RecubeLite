
from lib.modifier import Modifier
from lib import util
from dataclasses import dataclass

class Health:
    def __init__(self,hitPoint:int,MaxHitPoint:int):
        self.__hp = hitPoint
        self.__max_hp = MaxHitPoint
        self.__hp_modifier = Modifier()
        self.__max_hp_modifier = Modifier()
        self.__dead = False
    def damage(self,value:int):
        self.__hp -= value
    def heal(self,value:int):
        self.__hp += value
    def get_hit_point(self):
        result = util.minimum(util.maximum(self.__hp_modifier(self.__hp),self.__max_hp_modifier(self.__max_hp)),0)
        if result <= 0:
            self.__dead = True
        else:
            self.__dead = False
        return result
    def is_dead(self):
        return self.__dead
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if isinstance(value,int):
            self.__hp = value
        else:
            raise ValueError("整数のみヒットポイントとして扱えます")
    @property
    def hp_modifier(self):
        return self.__hp_modifier
    @property
    def max_hp(self):
        return self.__max_hp
    @property
    def max_hp_modifier(self):
        return self.__max_hp_modifier