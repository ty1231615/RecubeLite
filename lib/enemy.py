
from lib.entity import Entity

class Enemy(Entity):
    def __init__(self, pos, AttackDamage:int, valid:bool) -> None:
        super().__init__(pos)
        self.__valid = valid
        self.__damage = AttackDamage
    @property
    def damage(self):
        return self.__damage
    @property
    def valid(self):
        return self.__valid
    def active(self):
        self.__valid = True
    def invalid(self):
        self.__valid = False