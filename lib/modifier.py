

from typing import Any

class Modifier:
    def __init__(self) -> None:
        self.__modifiers = {}
    def __call__(self, default:int):
        return default + self.total()
    def total(self):
        result = 0
        for modifier in self.__modifiers:
            result += self.__modifiers[modifier]
        return result
    def add(self,key:str,value:int):
        self.__modifiers.update({key:value})
    def remove(self,key):
        if key in self.modifiers:
            del self.__modifiers[key]
    @property
    def modifiers(self):
        return self.__modifiers