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

class BlockRegister(TypeRegister):
    def __init__(self):
        super().__init__(BlockData)
    def get(self, key) -> BlockData:
        return super().get(key)
    def is_throughable(self,key) -> bool:
        return self.get(key).throughable
    def is_goal(self,key) -> bool:
        return self.get(key).is_goal
    @classmethod
    def DefaultRegister(cls):
        instance = cls()
        instance.register(BlockData.AIR,BlockData(throughable=True))
        instance.register(BlockData.WALL,BlockData(throughable=False))
        instance.register(BlockData.GOAL,BlockData(throughable=True,is_goal=True))
        return instance