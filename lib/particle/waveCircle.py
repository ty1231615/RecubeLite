from lib import easing
from lib.progress import Progress
from lib.task import SimpleTask

import pygame

class WaveCircle(SimpleTask):
    def __init__(self,surface:pygame.Surface,center:tuple[int,int], progress: Progress,maxRadius:int,color:tuple[int,int,int],width:int, radiusEasing=easing.easeOutQuart, widthEasing=easing.easeOutQuart) -> None:
        super().__init__()
        self.__surface = surface
        self.center = center
        self.__progress = progress
        self.__maxRadius = maxRadius
        self.color = color
        self.width = width
        self.__radiusEasing = radiusEasing
        self.__widthEasing = widthEasing
    def draw(self):
        pygame.draw.circle(self.__surface,self.color,self.center,self.__radiusEasing(self.__progress.normalize()) * self.__maxRadius, int(self.__widthEasing(1 - self.__progress.normalize()) * self.width))
    def run(self):
        if self.__progress.complete:
            self.Remove()
            return
        self.draw()
        self.__progress.next()
