

from typing import Any

class Modifier:
    def __init__(self) -> None:
        self.__modifiers = {}
    def total(self):
        result = 0
        for modifier in self.__modifiers:
            result += self.__modifiers[modifier]
        return result
    def add(self,key:str,value:int):
        self.__modifiers.update({key:value})
    def remove(self,key):
        self.__modifiers.pop(key)