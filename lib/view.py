from lib.progress import Progress
from lib import easing
from lib.register import TypeRegister
from package.particle.waveCircle import WaveCircle

import pygame

class Design(TypeRegister):
    def __init__(self):
        super().__init__(pygame.Surface)
    def get(self, key) -> pygame.Surface:
        return super().get(key)

class SessionDesignView:
    def __init__(self, blockDesign: Design, player: pygame.Surface, enemy: pygame.font.Font, enemy_text:str, blockPadding: int, gameOverFont: pygame.font.Font, resultTextFont: pygame.font.Font, upperNoticeFont: pygame.font.Font) -> None:
        self.__block_design = blockDesign
        self.__player_design = player
        self.__enemy_font = enemy
        self.__enemy_text = enemy_text
        self.__block_padding = blockPadding
        self.__game_over_font = gameOverFont
        self.__result_text_font = resultTextFont
        self.__upper_notice_font = upperNoticeFont
    def playerWaveParticle(self,surface:pygame.Surface, center: tuple[int,int], maxTime,color:tuple[int,int,int],maxRadiusDelta:float|int,WaveWidthDelta:float|int):
        delta = (self.playerDesign.get_width() + self.playerDesign.get_height()) / 2
        return WaveCircle(surface,center,Progress(0, maxTime, 0, 1), int(delta * maxRadiusDelta), color, int(delta * WaveWidthDelta))
    @property
    def blockDesigns(self):
        return self.__block_design
    @property
    def playerDesign(self):
        return self.__player_design
    @property
    def enemyFont(self):
        return self.__enemy_font
    @property
    def enemyText(self):
        return self.__enemy_text
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