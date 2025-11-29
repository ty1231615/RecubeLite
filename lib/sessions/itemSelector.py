from lib.position import Pos
from lib.progress import Progress
from lib.task import Task,TaskType,TaskLine,TaskController,TaskLineGenerater
from lib.animation.keyframe import PositionKeyFrame
from lib.session import Session
from lib.item import Item
from lib import util
import pygame

#アイテムボックスのアイテムを選択するタスク
class ItemSelection(TaskLineGenerater):
    def __init__(self,session:Session,font_path,padding:int,items:tuple[Item]) -> None:
        self.__session = session
        self.__surface = self.__session.surface
        self.__items = items
        self.__center_position = Pos(0,0)
        self.__padding = 0
    def CreateTaskLine(self) -> TaskLine:
        line = TaskLine()

        StartPosition = Pos(self.__surface.get_width() / 2,-200)
        self.__center_position = StartPosition
        self.__padding = self.__surface.get_width() / (len(self.__items) + 1)

        line.add(
            Task(
                self.__view,
                TaskType.WHILE,
            )
        )

        line.add(
            PositionKeyFrame(
                StartPosition,
                StartPosition.plus(0,400),
                self.__position_setter,
                TaskType.AFTER_STANDING,
                repeat=Progress(0,util.frame_to_second(1),0,1)
            )
        )

        

        return line
    def __position_setter(self,pos:Pos):
        self.__center_position = pos
    def __view(self,controller:TaskController):
        for index, item in enumerate(self.__items):
            self.__surface.blit(pygame.transform.scale(item.image,(self.__padding,self.__padding)),(self.__center_position.x - self.__padding * int(index / len(self.__items)),self.__center_position.y))