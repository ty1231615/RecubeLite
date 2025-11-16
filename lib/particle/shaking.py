from lib.particle.camera import Camera,CURRENT_CAMERA
from lib.task import SimpleTask
from lib.progress import Progress

import random

class ShakingCamera(SimpleTask):
    _MODIFIER_NAMESPACE = "particle:ShakingCamera"
    def __init__(self, progress:Progress, minShake:int, maxShake:int, camera:Camera=CURRENT_CAMERA):
        super().__init__()
        self.__progress = progress
        self.__camera = camera
        self.__min = minShake
        self.__max = maxShake
    def run(self):
        if self.__progress.complete:
            self.Remove()
            return
        self.__camera.x_modifier.add(ShakingCamera._MODIFIER_NAMESPACE,random.randint(self.__min,self.__max))
        self.__camera.y_modifier.add(ShakingCamera._MODIFIER_NAMESPACE,random.randint(self.__min,self.__max))
        self.__progress.next()
    def on_remove(self):
        self.__camera.x_modifier.remove(ShakingCamera._MODIFIER_NAMESPACE)
        self.__camera.y_modifier.remove(ShakingCamera._MODIFIER_NAMESPACE)