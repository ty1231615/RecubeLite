from lib.particle.waveCircle import WaveCircle
from lib.progress import Progress
from lib import easing
from lib.register import NamespaceRegister

import pygame

class Design(NamespaceRegister):
    def __init__(self) -> None:
        self.__designs = {}
    def register(self,key,design:pygame.Surface):
        if isinstance(design,pygame.Surface):
            self.__designs.update({key:design})
        else:
            raise TypeError(f"{design} は不適切なオブジェクトです")
    def get(self,key) -> pygame.Surface:
        return self.__designs[key]

class SessionDesignView:
    def __init__(self, blockDesign: Design, player: pygame.Surface, enemy: pygame.Surface, blockPadding: int, gameOverFont: pygame.font.Font, resultTextFont: pygame.font.Font, upperNoticeFont: pygame.font.Font) -> None:
        self.__block_design = blockDesign
        self.__player_design = player
        self.__enemy_design = enemy
        self.__block_padding = blockPadding
        self.__game_over_font = gameOverFont
        self.__result_text_font = resultTextFont
        self.__upper_notice_font = upperNoticeFont
    def playerWaveParticle(self,surface:pygame.Surface, center: tuple[int,int], maxTime,color:tuple[int,int,int]):
        delta = (self.playerDesign.get_width() + self.playerDesign.get_height()) / 2
        return WaveCircle(surface,center,Progress(0, maxTime, 0, 1), delta * 15, color, delta * 5)
    @property
    def blockDesigns(self):
        return self.__block_design
    @property
    def playerDesign(self):
        return self.__player_design
    @property
    def enemyDesign(self):
        return self.__enemy_design
    @property
    def blockPadding(self):
        return self.__block_padding
    @property
    def gameOverFont(self):
        return self.__game_over_font
    @property
    def resultTextFont(self):
        return self.__result_text_font
    @property
    def upperNoticeFont(self):
        return self.__upper_notice_font