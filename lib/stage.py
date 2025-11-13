from lib.block import BlockData,BlockRegister
from lib.position import Pos

import random

class Stage:
    def __init__(self,width_size:int,height_size:int,level:int) -> None:
        self.__width_size = width_size
        self.__height_size = height_size
        self.__level = level
        self.__stage = Stage.makeStage(self.__width_size,self.__height_size)
        Stage.makeAroundWall(self.__stage)
    @property
    def stage(self):
        return self.__stage
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self,value):
        if isinstance(value,int):
            self.__level = value
    @property
    def width(self):
        return self.__width_size
    @property
    def height(self):
        return self.__height_size
    def getAirSpace(self,block_register:BlockRegister):
        positions = []
        for y in range(self.height):
            for x in range(self.width):
                if block_register.is_throughable(self.stage[y][x]):
                    positions.append(Pos(x,y))
        return positions
    def resetStage(self):
        self.__stage = Stage.makeStage(self.width,self.height)
        Stage.makeAroundWall(self.__stage)
    def ScatterWall(self,maximum):
        level = self.level
        if level > maximum:
            level = maximum
        for i in range(level):
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            self.stage[y][x] = BlockData.WALL
    def randomPosition(self):
        x = random.randint(0,self.width-1)
        y = random.randint(0,self.height-1)
        return Pos(x,y)
    def createGoal(self,pos:Pos):
        self.stage[pos.y][pos.x] = BlockData.GOAL
    def makeStageDelta(self,delta):
        return [[delta for x in range(self.width)] for y in range(self.height)]

    @classmethod
    def makeStage(cls,width,height):
        return [[BlockData.AIR for i in range(width)] for i in range(height)]
    @classmethod
    def fill_beside(cls,stage,index,block):
        for i in range(len(stage[index])):
            stage[index][i] = block
    @classmethod
    def fill_vertical(cls,stage,index,block):
        for y in range(len(stage)):
            stage[y][index] = block
    @classmethod
    def makeAroundWall(cls,stage):
        Stage.fill_beside(stage,0,BlockData.WALL)
        Stage.fill_beside(stage,len(stage)-1,BlockData.WALL)
        Stage.fill_vertical(stage,0,BlockData.WALL)
        Stage.fill_vertical(stage,len(stage[0])-1,BlockData.WALL)