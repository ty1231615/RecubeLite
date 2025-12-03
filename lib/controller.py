from lib.progress import Progress
import pygame

class PlayerControleBinder:
    def __init__(self,key,command,hold=False):
        self.__key = key
        self.__hold = hold
        self.__command = command
        self.__progress = Progress(0,0,0,0)
    def setProgresser(self,progress:Progress):
        self.__progress = progress
        return self
    def resetProgress(self):
        self.__progress.current = self.__progress.max
        self.__progress.complete = True
    @property
    def key(self):
        return self.__key
    @property
    def command(self):
        return self.__command
    @property
    def moveProgress(self):
        return self.__progress
    @property
    def is_hold(self):
        return self.__hold