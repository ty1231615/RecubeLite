from lib.task import Task,TaskType,TaskLine,TaskController
from lib.position import Pos
from lib.progress import Progress
from lib import easing

import types

class PositionKeyFrame(Task):
    def __init__(self, fromPosition:Pos, targetPosition:Pos, valueSetter: types.FunctionType|types.MethodType|types.LambdaType, taskType, delay=Progress(0,0,0,1), easing_format: types.FunctionType = easing.no_easing, repeat=Progress(0,0,0,1), repeatDelay=Progress(0,0,0,1), complete = False):
        super().__init__(self.step, taskType, delay, repeat, repeatDelay, complete)
        self.__easing_format = easing_format #Progressを (0.0 ~ 1.0) にnormalizeした進捗をこの関数を用いてフォーマットする
        self.__value_setter = valueSetter #算出された数値を渡す関数 (一つ目の引数にデータを渡す)
        self.__from_position = fromPosition
        self.__target_value = targetPosition
    def step(self,controller:TaskController):
        normalize_progress = self.__easing_format(self.repeat.normalize()) #normalizeデータを同時にeasingフォーマットを適応する
        to_vec:Pos = self.__target_value.subtract(self.__from_position)
        self.__value_setter(to_vec.multiple(normalize_progress,normalize_progress).plus(self.__from_position.x,self.__from_position.y))

