import pygame

class WaveCircle:
    def __init__(self,surface:pygame.Surface,center:tuple[int,int],maxRadius:int,color:tuple[int,int,int],width:int,speed:int) -> None:
        self.__surface = surface
        self.__center = center
        self.__maxRadius = maxRadius
        self.__color = color
        self.__width = width
        self.__speed = speed
        self.__currentRadius = 0
    def run(self):
        if self.__currentRadius < self.__maxRadius:
            pygame.draw.circle(self.__surface,self.__color,self.__center,self.__currentRadius,self.__width)
            self.__currentRadius += self.__speed
    @property
    def currentRadius(self):
        return self.__currentRadius
    @currentRadius.setter
    def currentRadius(self, value):
        self.__currentRadius = value
        if self.__currentRadius > self.__maxRadius:
            self.__currentRadius = self.__maxRadius