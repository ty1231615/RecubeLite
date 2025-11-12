
from lib.entity import Entity

class Player(Entity):
    def __init__(self, pos) -> None:
        super().__init__(pos)