from pygame import Surface
from pygame.font import Font
from lib.computer import ComputeEnemy
from lib.entity import Entity
from lib.health import Health
from lib.player import Player
from lib.registers import BlockRegister
from lib.session import Session
from lib.stage import Stage
from lib.view import Design, SessionDesignView
from lib.block import BlockData
from lib.view import SessionDesignView
from lib.item import Item,ItemBox

class ItemSessionDesign(SessionDesignView):
    def __init__(self, blockDesign: Design, player: Surface, enemy: Surface, blockPadding: int, gameOverFont: Font, resultTextFont: Font, upperNoticeFont: Font, SupportItemBoxDesign:Surface, AssistItemBoxDesign:Surface) -> None:
        super().__init__(blockDesign, player, enemy, blockPadding, gameOverFont, resultTextFont, upperNoticeFont)
        self.__support_item_box_design = SupportItemBoxDesign
        self.__assit_item_box_design = AssistItemBoxDesign
        self.blockDesigns.register(ItemSession.SUPPORT,self.SupportItemBoxDesign)
        self.blockDesigns.register(ItemSession.ASSIST,self.AssistItemBoxDesign)
    @property
    def SupportItemBoxDesign(self):
        return self.__support_item_box_design
    @property
    def AssistItemBoxDesign(self):
        return self.__assit_item_box_design

class NormalItemBox(ItemBox):
    def __init__(self, items: tuple[Item]):
        super().__init__(items)
    def lottery(self,session:Session):
        pass

class ItemSession(Session):
    ITEM_BOX_BLOCK = "block:item_box"
    SUPPORT = ITEM_BOX_BLOCK+".support"
    ASSIST = ITEM_BOX_BLOCK+".assist"
    def __init__(self, surface: Surface, stage: Stage, stageLevel: int, maxStageLevel: int, health: Health, players: list[Player], enemys: list[ComputeEnemy], view: ItemSessionDesign, block_register: BlockRegister) -> None:
        super().__init__(surface, stage, stageLevel, maxStageLevel, health, players, enemys, view, block_register)
        self.__support_item_box = ItemBox()
        self.__assist_item_box = ItemBox()
        self.block_register.register(ItemSession.SUPPORT,self.__support_item_box)
        self.block_register.register(ItemSession.ASSIST,self.__assist_item_box)
    def on_move(self, entity: Entity):
        super().on_move(entity)
        block_data = self.get_block(entity.position)
        if isinstance(block_data,Item):
            pass