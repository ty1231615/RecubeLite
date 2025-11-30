from lib.position import Pos
from lib.progress import Progress
from lib.task import Task,TaskType,TaskLine,TaskController,TaskLineGenerater
from lib.controller import PlayerControleBinder
from lib.animation.keyframe import PositionKeyFrame
from lib.session import Session
from lib.player import Player
from lib.item import Item
from lib import easing
from lib import util
import pygame

#アイテムボックスのアイテムを選択するタスク
class ItemSelection(TaskLineGenerater):
    NAMESPACE = "selector:item_selection"
    SELECT_KEY = [
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_8,
        pygame.K_9,
        pygame.K_0
    ]
    def __init__(self,session:Session, select_player:Player, font_path:str, movement_height:int, items:tuple[Item], description_color=(226, 133, 46)) -> None:
        self.__session = session
        self.__surface = self.__session.surface
        self.__items = items
        self.__movement_height = movement_height
        self.__center_position = Pos(0,0)
        self.__padding = 0
        self.__font = None
        self.__font_path = font_path
        self.__description_color = description_color
        self.__select_player = select_player
        self.__selected = False
    def CreateTaskLine(self) -> TaskLine:
        line = TaskLine()
        self.__padding = self.__surface.get_width() / (len(self.__items)+1)
        StartPosition = Pos(self.__surface.get_width() / 2,-self.__padding-self.__padding / 13)
        TargetPosition = StartPosition.plus(0,self.__movement_height)
        self.__center_position = StartPosition.copy()
        self.__font = pygame.font.Font(self.__font_path,int(self.__padding / 13))

        line.add(
            Task(
                self.__view,
                TaskType.WHILE,
            )
        )

        line.add(
            Task(
                self.__bind_selecter,
                TaskType.CONTINUE
            )
        )

        line.add(
            PositionKeyFrame(
                StartPosition,
                TargetPosition,
                self.__position_setter,
                TaskType.AFTER_STANDING,
                repeat=Progress(0,util.frame_to_second(0.5),0,1),
                easing_format=easing.ease_out_expo
            )
        )

        line.add(
            Task(
                self.__select_check,
                TaskType.WHILE_AFTER_STANDING
            )
        )

        line.add(
            PositionKeyFrame(
                TargetPosition,
                StartPosition,
                self.__position_setter,
                TaskType.AFTER_STANDING,
                repeat=Progress(0,util.frame_to_second(1),0,1),
                easing_format=easing.easeOutQuart
            )
        )

        return line
    def __position_setter(self,pos:Pos):
        self.__center_position = pos.copy()
    def __view(self,controller:TaskController):
        for index, item in enumerate(self.__items):
            blit_pos = Pos(self.__padding * (index) + self.__padding / 2,self.__center_position.y)
            self.__surface.blit(pygame.transform.scale(item.image,(self.__padding / 1.5,self.__padding / 1.5)),blit_pos.plus(self.__padding / 5, self.__padding / 5).toTuple())
            description = self.__font.render(item.description,True,self.__description_color)
            self.__surface.blit(description,description.get_rect(center=blit_pos.plus(self.__padding/2,self.__padding).toTuple()))
    def __bind_selecter(self,controller:TaskController):
        for index in range(len(self.__items)):
            self.__select_player.add_controle(PlayerControleBinder(ItemSelection.SELECT_KEY[index],lambda i=index: self.__select(i)))
    def __select_check(self,controller:TaskController):
        if self.__selected:
            controller.complete()
    def __select(self,index):
        print(index)
        self.__session.on_item(self.__items[index],self.__select_player)
        for index in range(len(self.__items)):
            self.__select_player.remove_controle(ItemSelection.SELECT_KEY[index])
        self.__selected = True