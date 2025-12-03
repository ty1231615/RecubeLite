from pygame import Surface
from pygame.font import Font
from lib.computer import ComputeEnemy
from lib.entity import Entity
from lib.health import Health
from lib.player import Player
from lib.registers import BlockRegister
from lib.session import Session
from lib.config import fonts
from lib.stage import Stage
from lib.view import Design, SessionDesignView
from lib.position import Pos
from lib.util import safe_change_grid
from lib.view import SessionDesignView
from lib.item import Item,ItemBox
from lib.sessions.itemBox import NormalItemBox

import random,pygame

class ItemSessionDesign(SessionDesignView):
    def __init__(self, blockDesign: Design, player: Surface, enemy_font: pygame.font.Font, enemy_text:str, blockPadding: int, gameOverFont: Font, resultTextFont: Font, upperNoticeFont: Font, SupportItemBoxDesign:Surface, AssistItemBoxDesign:Surface) -> None:
        super().__init__(blockDesign, player, enemy_font, enemy_text, blockPadding, gameOverFont, resultTextFont, upperNoticeFont)
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

class ItemSession(Session):
    ITEM_BOX_BLOCK = "block:item_box"
    SUPPORT = ITEM_BOX_BLOCK+".support"
    ASSIST = ITEM_BOX_BLOCK+".assist"
    def __init__(self, surface: Surface, stage: Stage, stageLevel: int, maxStageLevel: int, health: Health, players: list[Player], enemys: list[ComputeEnemy], view: ItemSessionDesign, block_register: BlockRegister, support_items:tuple[Item], assist_items:tuple[Item]) -> None:
        super().__init__(surface, stage, stageLevel, maxStageLevel, health, players, enemys, view, block_register)
        self.__support_item_box = NormalItemBox(support_items)
        self.__selected_item_box_position = Pos(0,0)
        self.__assist_item_box = NormalItemBox(assist_items)
        self.block_register.register(ItemSession.SUPPORT,self.__support_item_box)
        self.block_register.register(ItemSession.ASSIST,self.__assist_item_box)
    def loadLevel(self):
        item_box = [ItemSession.SUPPORT]
        remaining_space = super().loadLevel()
        for index in range(len(item_box)):
            if len(remaining_space) > 0:
                position = random.choice(remaining_space)
                safe_change_grid(self.stage.stage,position.x,position.y,item_box[index-1])
                self.__selected_item_box_position.movePos(position)
                remaining_space.remove(position)
        return remaining_space
    def on_move(self, entity: Entity):
        super().on_move(entity)
        block_data = self.get_block(entity.position)
        if isinstance(block_data,ItemBox):
            if not block_data.selecting:
                if block_data.lottery(self,entity,self.__selected_item_box_position):
                    block_data.valid_select()
    def on_item(self,item:Item,entity:Entity,replace_position:Pos):
        result = item.on_touch(self,entity)
        if result:
            safe_change_grid(self.stage.stage,replace_position.x,replace_position.y,item.replace_block_id)