from enum import Enum
from lib.block import BlockData
from lib.entity import Entity


class ItemType(Enum):
    Support = 0
    Assist = 1

class Item:
    def __init__(self,item_type:ItemType,name:str,description:str="New Item !",replace_block_id=BlockData.AIR):
        self.__item_type = item_type
        self.__name = name
        self.__description = description
        self.__replace_block_id = replace_block_id
    def on_touch(self,session,entity:Entity) -> bool:
        return False
    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @property
    def item_type(self):
        return self.__item_type
    @property
    def replace_block_id(self):
        return self.__replace_block_id
    
class ItemBox(BlockData):
    def __init__(self,items:tuple[Item]):
        super().__init__(True, False)
        self.__items = items
    def lottery(self,session,entity) -> Item:
        ...
    @property
    def items(self):
        return self.__items