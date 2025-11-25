from lib.item import Item,ItemType
from lib.session import Session
from lib.entity import Entity
from lib.player import Player

class HealOrb(Item):
    def __init__(self):
        super().__init__(ItemType.Support)
    def on_touch(self, session:Session, entity:Entity):
        session.health.heal(1)
        session.notice_health()
        if isinstance(entity,Player):
            session.player_wave_particle(entity,(61, 182, 177),10,3)