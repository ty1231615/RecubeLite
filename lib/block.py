from lib.register import TypeRegister
from enum import Enum

class BlockData:
    AIR = "block:air"
    WALL = "block:wall"
    GOAL = "block:goal"
    def __init__(self,throughable:bool=False,is_goal=False):
        self.__throughable = throughable
        self.__is_goal = is_goal
    @property
    def throughable(self):
        return self.__throughable
    @property
    def is_goal(self):
        return self.__is_goal