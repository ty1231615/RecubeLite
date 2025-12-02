
from lib.entity import Entity
from lib.color import TransferColor

class Enemy(Entity):
    def __init__(self, pos, AttackDamage:int, valid:bool, color=TransferColor(221, 3, 3, 111, 0, 255)) -> None:
        super().__init__(pos)
        self.__valid = valid
        self.__color = color
        self.__damage = AttackDamage
    @property
    def damage(self):
        return self.__damage
    @property
    def valid(self):
        return self.__valid
    @property
    def color(self):
        return self.__color
    def active(self):
        self.__valid = True
    def invalid(self):
        self.__valid = False