from pygame import Surface
from pygame.font import Font
from lib.computer import ComputeEnemy
from lib.health import Health
from lib.player import Player
from lib.registers import BlockRegister
from lib.session import Session
from lib.stage import Stage
from lib.view import Design, SessionDesignView
from lib.block import BlockData
from lib.view import SessionDesignView

class ItemBox(BlockData):
    def __init__(self):
        super().__init__(True, False)
        self.__is_item_box = True
    @property
    def is_item_box(self):
        return self.__is_item_box

class ItemSessionDesign(SessionDesignView):
    def __init__(self, blockDesign: Design, player: Surface, enemy: Surface, blockPadding: int, gameOverFont: Font, resultTextFont: Font, upperNoticeFont: Font, SupportItemBoxDesign:Surface, AssistItemBoxDesign:Surface) -> None:
        super().__init__(blockDesign, player, enemy, blockPadding, gameOverFont, resultTextFont, upperNoticeFont)
        self.__support_item_box_design = SupportItemBoxDesign
        self.__assit_item_box_design = AssistItemBoxDesign
    @property
    def SupportItemBoxDesign(self):
        return self.__support_item_box_design
    @property
    def AssistItemBoxDesign(self):
        return self.__assit_item_box_design

class ItemSession(Session):
    ITEM_BOX_BLOCK = "block:item_box"
    SUPPORT = ITEM_BOX_BLOCK+".support"
    ASSIST = ITEM_BOX_BLOCK+".assist"
    def __init__(self, surface: Surface, stage: Stage, stageLevel: int, maxStageLevel: int, health: Health, players: list[Player], enemys: list[ComputeEnemy], view: ItemSessionDesign, block_register: BlockRegister) -> None:
        super().__init__(surface, stage, stageLevel, maxStageLevel, health, players, enemys, view, block_register)