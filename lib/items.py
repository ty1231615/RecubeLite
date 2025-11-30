from lib.item import Item,ItemType
from lib.session import Session
from lib.particle.shaking import ShakingCamera
from lib.progress import Progress
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

class StunOrb(Item):
    def __init__(self, name="Stun orb", image_name = "stun_orb.png", description = "エネミーを一時的にスタンさせる"):
        super().__init__(ItemType.Support, name, image_name, description)
    def on_touch(self, session:Session, entity:Entity):
        if isinstance(entity,Player):
            for enemy in session.get_enemys():
                enemy.stayProgress.current = 145
            session.player_wave_particle(entity,(245, 200, 87),20,6)
            ShakingCamera(Progress(0,40,0,1),-5,5)
            return True
        return False