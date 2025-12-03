
from lib.entity import Entity
from lib.progress import Progress
from lib.controller import PlayerControleBinder

class Player(Entity):
    def __init__(self, pos, moveSpeed) -> None:
        super().__init__(pos)
        self.__controller = []
        self.__MSP_ABOVE = Progress(moveSpeed,moveSpeed,0,1)
        self.__MSP_BELOW = Progress(moveSpeed,moveSpeed,0,1)
        self.__MSP_LEFT = Progress(moveSpeed,moveSpeed,0,1)
        self.__MSP_RIGHT = Progress(moveSpeed,moveSpeed,0,1)
    @property
    def controller(self):
        return self.__controller
    @property
    def MSP_ABOVE(self):
        return self.__MSP_ABOVE
    @property
    def MSP_BELOW(self):
        return self.__MSP_BELOW
    @property
    def MSP_LEFT(self):
        return self.__MSP_LEFT
    @property
    def MSP_RIGHT(self):
        return self.__MSP_RIGHT
    def change_speed(self,speed:int):
        self.__MSP_ABOVE.max = speed
        self.__MSP_BELOW.max = speed
        self.__MSP_LEFT.max = speed
        self.__MSP_RIGHT.max = speed
    def set_controller(self, controller:list[PlayerControleBinder]):
        self.__controller = controller
    def add_controle(self,controle:PlayerControleBinder):
        self.__controller.append(controle)
    def remove_controle(self,key):
        for controller in list(self.__controller):
            if controller.key == key:
                self.__controller.remove(controller)
    def moveStep(self,progress:Progress) -> bool:
        if progress.complete:
            progress.reset()
            return True
        progress.next()
        return False
    def msp_above(self, session):
        if self.moveStep(self.__MSP_ABOVE):
            return self.above(session)
    def msp_below(self, session):
        if self.moveStep(self.__MSP_BELOW):
            return self.below(session)
    def msp_left(self, session):
        if self.moveStep(self.__MSP_LEFT):
            return self.left(session)
    def msp_right(self, session):
        if self.moveStep(self.__MSP_RIGHT):
            return self.right(session)