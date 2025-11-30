from lib.item import Item,ItemType
from lib.session import Session
from lib.entity import Entity
from lib.player import Player

class HealOrb(Item):
    def __init__(self,name="Healing orb",desc="回復することができるオーブ",image_name="heal_orb.png"):
        super().__init__(ItemType.Support,name,description=desc,image_name=image_name)
    def on_touch(self, session:Session, entity:Entity):
        if isinstance(entity,Player):
            session.health.heal(1)
            session.notice_health()
            if isinstance(entity,Player):
                session.player_wave_particle(entity,(61, 182, 177),10,3)
            return True
        return False