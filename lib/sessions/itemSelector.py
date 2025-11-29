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
    def __init__(self,session:Session,font_path,items:tuple[Item]) -> None:
        self.__session = session
        self.__surface = self.__session.surface
        self.__items = items
    def CreateTaskLine(self) -> TaskLine:
        line = TaskLine()

        StartPosition = Pos(self.__surface.get_width() / 2,-200)
        item_padding = self.__surface.get_width() / (len(self.__items) + 1)

        line.add(
            
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
        pass
    def __view(self):
        pass