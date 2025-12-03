
from lib.entity import Entity
from lib.controller import PlayerControleBinder

class Player(Entity):
    def __init__(self, pos) -> None:
        super().__init__(pos)
        self.__controller = []
    @property
    def controller(self):
        return self.__controller
    def set_controller(self, controller:list[PlayerControleBinder]):
        self.__controller = controller
    def add_controle(self,controle:PlayerControleBinder):
        self.__controller.append(controle)
    def remove_controle(self,key):
        for controller in list(self.__controller):
            if controller.key == key:
                self.__controller.remove(controller)