from lib.block import BlockData
from lib.register import NamespaceRegister

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


class ItemRegister(NamespaceRegister):
    def __init__(self):
        super().__init__()
    def register(self, key, object):
        if isinstance(object,ItemData):
            return super().register(key, object)
    def get(self, key) -> ItemData:
        return super().get(key)
