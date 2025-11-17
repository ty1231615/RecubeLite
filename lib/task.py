
from enum import Enum
from lib.progress import Progress
import types

class SimpleTask:
    _INSTANCE = []
    def __init__(self) -> None:
        SimpleTask._INSTANCE.append(self)
        self.__delete = False
    @property
    def delete(self):
        return self.__delete
    def Remove(self):
        self.__delete = True
    def CancelRemove(self):
        self.__delete = False
    def run(self):
        ...
    def on_remove(self):
        ...
    def __del__(self):
        if self in SimpleTask._INSTANCE:
            SimpleTask._INSTANCE.remove(self)
    @classmethod
    def AllInstanceRun(cls):
        for instance in cls._INSTANCE:
            instance.run()
            if instance.delete:
                instance.on_remove()
                del instance

class TaskType(Enum):
    CONTINUE = 0
    STANDING = 1
    STANDING_AFTER = 2

class Task:
    def __init__(self, run:types.FunctionType, taskType, delay:Progress, repeat=Progress(0,1,0,1), repeatDelay=Progress(0,1,0,1), complete:bool=False):
        self.__type = taskType
        self.__delay = delay
        self.__repeat = repeat
        self.__repeatProgress = repeatDelay
        self.__run = run
        self.__complete = complete
    def run(self):
        return self.__run()
    def complete(self):
        self.__complete = True
    def reset(self):
        self.__complete = False
        self.__delay.reset()
        self.__repeat.reset()
    @property
    def delay(self):
        return self.__delay
    @property
    def repeat(self):
        return self.__repeat
    @property
    def repeatProgress(self):
        return self.__repeatProgress
    @property
    def is_complete(self):
        return self.__complete
    @property
    def taskType(self):
        return self.__type

class TaskLine:
    def __init__(self):
        self.__tasks:list[Task] = []
        self.__all_complete = False
    def reset(self):
        for task in self.__tasks:
            task.reset()
    def add(self,task:Task):
        if isinstance(task,Task):
            self.__tasks.append(task)
        else:
            raise TypeError("タスクオブジェクトのみスケジュールできます")
    def ticking(self):
        for index, task in enumerate(self.__tasks):
            if not task.is_complete:
                if task.taskType == TaskType.STANDING:
                    if index != 0:
                        break
                    self.task_compute(task)
                elif task.taskType == TaskType.STANDING_AFTER:
                    self.task_compute(task)
                    break
                elif task.taskType == TaskType.CONTINUE:
                    self.task_compute(task)
        self.__all_complete = self.check_all_complete()
    def check_all_complete(self):
        return all(task.is_complete for task in self.__tasks)
    def task_compute(self,task:Task):
        if not task.is_complete:
            if task.delay.complete:
                if task.repeatProgress.complete:
                    #print(task.repeat.current)
                    #print(task.repeat.complete)
                    task.run()
                    task.repeat.next()
                    if task.repeat.complete:
                        task.complete()
                        return
                    task.repeatProgress.reset()
                task.repeatProgress.next()
            task.delay.next()
    @property
    def all_complete(self):
        return self.__all_complete