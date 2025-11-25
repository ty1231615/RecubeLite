from enum import Enum
from lib.block import BlockData

class ItemData:
    def __init__(self,name:str,description:str="New Item !"):
        self.__name = name
        self.__description = description
    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description

class ItemType(Enum):
    Support = 0
    Assist = 1


class Item(BlockData):
    def __init__(self,item_type:ItemType):
        super().__init__(throughable=True)
        self.__item_type = item_type
    def on_touch(self,session,entity):
        ...
    @property
    def item_type(self):
        return self.__item_type
