from lib.item import Item,ItemType
from lib.progress import Progress
from lib.entity import Entity
from lib.player import Player
from lib.block import BlockData
from package.particle.shaking import ShakingCamera

# annotation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from package.sessions.itemSession import ItemSession
    from lib.session import Session


class HealOrb(Item):
    def __init__(self, name="Healing orb", namespace:str="item:heal_orb", desc="回復することができるオーブ", image_name="heal_orb.png", replace_block_id=BlockData.AIR):
        super().__init__(ItemType.Support, name, namespace, image_name, desc, replace_block_id)
    def on_touch(self, session:'ItemSession', entity:Entity):
        if isinstance(entity,Player):
            session.health.heal(1)
            session.notice_health()
            if isinstance(entity,Player):
                session.player_wave_particle(entity,(61, 182, 177),10,3)
            return True
        return False

class StunOrb(Item):
    def __init__(self, name="Stun orb", namespace="item:stun_orb", image_name = "stun_orb.png", description = "エネミーを一時的にスタンさせる", replace_block_id=BlockData.AIR):
        super().__init__(ItemType.Support, name, namespace, image_name, description, replace_block_id)
    def on_touch(self, session:'ItemSession', entity:Entity):
        if isinstance(entity,Player):
            for enemy in session.get_enemys():
                enemy.stayProgress.current = 145
            session.player_wave_particle(entity,(245, 200, 87),20,6)
            ShakingCamera(Progress(0,40,0,1),-5,5)
            return True
        return False

class SlowOrb(Item):
    def __init__(self, power:int, name: str="Slow Orb", namespace:str="item:slow_orb", image_name: str = "slow_orb.png", description: str = "エネミーの移動速度を少し下げる", replace_block_id=BlockData.AIR):
        super().__init__(ItemType.Assist, name, namespace, image_name, description, replace_block_id)
        self.__power = power
    @property
    def power(self):
        return self.__power
    def on_touch(self, session:'ItemSession', entity: Entity) -> bool:
        if isinstance(entity,Player):
            for enemy in session.get_enemys():
                enemy.moveProgress.MAX_MODIFIER.increase_with_create(self.namespace,self.power)
            session.player_wave_particle(entity,(140, 0, 255),20,2)
            return True
        return False

class ReductionBlockOrb(Item):
    def __init__(self, reduction:int, name="Reduction Block Orb", namespace="item:reduction_block_orb", image_name = "reduction_block_orb.png", description = "次のステージでのブロック生成量を下げる", replace_block_id = BlockData.AIR):
        super().__init__(ItemType.Support, name, namespace, image_name, description, replace_block_id)
        self.__reduction_count = reduction
    def on_touch(self, session:'Session', entity):
        if isinstance(entity,Player):
            session.stage.levelModifier.increase_with_create(self.namespace, -self.__reduction_count)
            ShakingCamera(Progress(0,20,0,1),-15,15)
            return True
        return False