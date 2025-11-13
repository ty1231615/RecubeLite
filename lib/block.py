from lib.register import NamespaceRegister
from enum import Enum

class BlockData:
    AIR = "block:air"
    WALL = "block:wall"
    GOAL = "block:goal"
    def __init__(self,throughable:bool=False):
        self.__throughable = throughable
    @property
    def throughable(self):
        return self.__throughable

class BlockRegister(NamespaceRegister):
    def __init__(self):
        super().__init__()
    def register(self, key, object):
        if isinstance(object,BlockData):
            return super().register(key, object)
    def get(self, key) -> BlockData:
        return super().get(key)
    def is_throughable(self,key) -> bool:
        return self.get(key).throughable
    @classmethod
    def DefaultRegister(cls):
        instance = cls()
        instance.register(BlockData.AIR,BlockData(True))
        instance.register(BlockData.WALL,BlockData(False))
        instance.register(BlockData.GOAL,BlockData(True))
        return instance