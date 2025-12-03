

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
    def increase(self,key:str,value:int):
        self.__modifiers[key] += value
    def increase_with_create(self,key:str,value:int):
        if key in self.__modifiers:
            self.increase(key,value)
        else:
            self.add(key,value)
    def remove(self,key):
        if key in self.modifiers:
            del self.__modifiers[key]
    def clear(self):
        """Clear all modifiers."""
        self.modifiers.clear()
    @property
    def modifiers(self):
        return self.__modifiers