from enum import Enum
from lib.block import BlockData
from lib.entity import Entity
from lib.util import item_image_load
import pygame


class ItemType(Enum):
    Support = 0
    Assist = 1

class Item:
    def __init__(self,item_type:ItemType,name:str, namespace:str,image_name:str="no_image.jpg",description:str="New Item !",replace_block_id:str=BlockData.AIR):
        self.__item_type = item_type
        self.__name = name
        self.__namespace = namespace
        self.__description = description
        self.__image = item_image_load(image_name)
        self.__replace_block_id = replace_block_id
    def on_touch(self,session,entity:Entity) -> bool:
        return False
    @property
    def name(self):
        return self.__name
    @property
    def namespace(self):
        return self.__namespace
    @property
    def description(self):
        return self.__description
    @property
    def item_type(self):
        return self.__item_type
    @property
    def image(self):
        return self.__image
    @property
    def replace_block_id(self):
        return self.__replace_block_id
    
class ItemBox(BlockData):
    def __init__(self,items:tuple[Item], selecting=False):
        super().__init__(True, False)
        self.__items = items
        self.__selecting = selecting
    def valid_select(self):
        self.__selecting = True
    def invalid_select(self):
        self.__selecting = False
    @property
    def selecting(self):
        return self.__selecting
    def lottery(self,session,entity,replace_position) -> bool:
        ...
    @property
    def items(self):
        return self.__items