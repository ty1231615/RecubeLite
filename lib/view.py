from lib.particle.waveCircle import WaveCircle
from lib.progress import Progress
from lib import easing

import pygame

class Design:
    def __init__(self) -> None:
        self.__designs = {}
    def add(self,key,design:pygame.Surface):
        self.__designs.update({key:design})
    def get(self,key) -> pygame.Surface:
        return self.__designs[key]

class SessionDesignView:
    def __init__(self,blockDesign:Design,player: pygame.Surface, enemy: pygame.Surface,blockPadding:int,gameOverFont:pygame.font.Font, resultTextFont:pygame.font.Font) -> None:
        self.__blockDesign = blockDesign
        self.__playerDesign = player
        self.__enemyDesign = enemy
        self.__blockPadding = blockPadding
        self.__gameOverFont = gameOverFont
        self.__resultTextFont = resultTextFont
    def playerWaveParticle(self,surface:pygame.Surface, center: tuple[int,int], maxTime,color:tuple[int,int,int]):
        delta = (self.playerDesign.get_width() + self.playerDesign.get_height()) / 2
        return WaveCircle(surface,center,Progress(0, maxTime, 0, 1), delta * 15, color, delta * 5)
    @property
    def blockDesigns(self):
        return self.__blockDesign
    @property
    def playerDesign(self):
        return self.__playerDesign
    @property
    def enemyDesign(self):
        return self.__enemyDesign
    @property
    def blockPadding(self):
        return self.__blockPadding
    @property
    def gameOverFont(self):
        return self.__gameOverFont
    @property
    def resultTextFont(self):
        return self.__resultTextFont