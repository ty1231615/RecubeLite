from lib.block import BlockData
from lib.register import TypeRegister

class ItemData:
    def __init__(self,name:str,description:str="New Item !"):
        self.__name = name
        self.__description = str
    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description

class Item(BlockData):
    def __init__(self, throughable = False):
        super().__init__(throughable)

class ItemRegister(TypeRegister):
    def __init__(self):
        super().__init__(Item)
    def get(self, key) -> Item:
        return super().get(key)