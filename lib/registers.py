
from lib.register import TypeRegister
from lib.block import BlockData
from lib.item import Item

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

class ItemRegister(TypeRegister):
    def __init__(self):
        super().__init__(Item)
    def get(self, key) -> Item:
        return super().get(key)