
import pygame

class PlayerControleBinder:
    def __init__(self,key,command):
        self.__key = key
        self.__command = command
    @property
    def key(self):
        return self.__key
    @property
    def command(self):
        return self.__command