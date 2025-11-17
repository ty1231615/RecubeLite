from lib.position import Pos
from lib.progress import Progress
from lib.animation.keyframe import PositionKeyFrame
from lib.task import Task,TaskLine,TaskType,TaskLineGenerater
from lib import easing
from lib import util

import pygame

class UpperNotice(TaskLineGenerater):
    NAMESPACE = "notice:upper"
    def __init__(self,draw_surface:pygame.Surface, draw_text: pygame.Surface,startPosition:Pos, under: int):
        self.__start_pos = startPosition
        self.__target_pos = startPosition.plus(0,under)
        self.__draw_surface = draw_surface
        self.__draw_target = draw_text
    def CreateTaskLine(self):
        line = TaskLine()

        line.add(
            PositionKeyFrame(
                self.__start_pos,
                self.__target_pos,
                self.valueSetter,
                TaskType.AFTER_STANDING,
                easing_format=easing.easeOutQuart,
                repeat=Progress(0,util.frame_to_second(1),0,1)
            )
        )

        line.add(
            PositionKeyFrame(
                self.__target_pos,
                self.__start_pos,
                self.valueSetter,
                TaskType.AFTER_STANDING,
                easing_format=easing.ease_out_expo,
                repeat=Progress(0,util.frame_to_second(1),0,1)
            )
        )

        return line
    def valueSetter(self,newPos:Pos):
        self.__draw_surface.blit(self.__draw_target,newPos.toTuple())
        