
from enum import Enum
from lib.progress import Progress
from lib.register import NamespaceRegister
import types
import inspect

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
    AFTER_STANDING = 2
    WHILE = 3
    WHILE_AFTER_STANDING = 4

class Task:
    def __init__(self, run:types.FunctionType|types.MethodType|types.LambdaType, taskType, delay:Progress|None=None, repeat:Progress|None=None, repeatDelay:Progress|None=None, complete:bool=False):
        """Avoid mutable default Progress objects in the signature.

        If callers don't supply Progress objects, create fresh instances here.
        """
        self.__type = taskType
        # create fresh Progress instances when None to avoid shared defaults
        self.__delay = delay if delay is not None else Progress(0,0,0,1)
        self.__repeat = repeat if repeat is not None else Progress(0,1,0,1)
        self.__repeatProgress = repeatDelay if repeatDelay is not None else Progress(0,0,0,1)
        self.__run = run
        Task._signature_check(self.__run)
        self.__complete = complete
    @classmethod
    def _signature_check(cls,func):
        func_signature = inspect.signature(func)
        if not len(func_signature.parameters) > 0:
            raise TypeError("タスクされる関数は引数が一つ以上必要です")
    def run(self,taskController):
        return self.__run(taskController)
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

class TaskController:
    def __init__(self,target_task:Task,before_task_result):
        self.__task = target_task
        self.__before_task_result = before_task_result
    @property
    def task(self):
        return self.__task
    @property
    def before_task_return(self):
        return self.__before_task_result
    def complete(self):
        self.__task.complete()


class TaskLine:
    def __init__(self):
        self.__tasks = []
        self.__all_complete = False
        self.__before_return = None
    def reset(self):
        for task in self.__tasks:
            task.reset()
    def type_check(self,obj):
        if not isinstance(obj,Task):
            raise TypeError("タスクオブジェクトのみスケジュールできます")
    def insert(self,index,task):
        self.type_check(task)
        self.__tasks.insert(index,task)
    def add(self,task:Task):
        self.type_check(task)
        self.__tasks.append(task)
    def ticking(self):
        for index, task in enumerate(self.__tasks):
            if not task.is_complete:
                if task.taskType == TaskType.STANDING:
                    if index != 0:
                        break
                    self.task_compute(task)
                elif task.taskType == TaskType.AFTER_STANDING or task.taskType == TaskType.WHILE_AFTER_STANDING:
                    self.task_compute(task)
                    break
                elif task.taskType == TaskType.CONTINUE:
                    self.task_compute(task)
                else:
                    self.task_compute(task)
        self.__all_complete = self.check_all_complete()
    def get_approach_tasks(self):
        for task in self.__tasks:
            yield task
    def check_all_complete(self):
        return all(task.is_complete for task in self.get_approach_tasks())
    def task_compute(self,task:Task,*arg,**kwarg):
        if not task.is_complete:
            taskController = TaskController(task,self.__before_return)
            if task.taskType == TaskType.WHILE or task.taskType == TaskType.WHILE_AFTER_STANDING:
                task.run(taskController)
                return
            if task.delay.complete:
                if task.repeatProgress.complete:
                    _return = task.run(taskController)
                    task.repeat.next()
                    if task.repeat.complete:
                        task.repeat.reset()
                        task.complete()
                        self.__before_return = _return
                        return
                    task.repeatProgress.reset()
                task.repeatProgress.next()
            task.delay.next()
    @property
    def all_complete(self):
        return self.__all_complete

class TaskLineLoader(NamespaceRegister):
    def __init__(self):
        super().__init__()
    def register(self, key, object):
        if isinstance(object,TaskLine):
            return super().register(key, object)
        raise TypeError("TaskLineオブジェクトのみスケジュールできます")
    def tick(self):
        for line in self.iter():
            line[1].ticking()

class TaskLineGenerater: #タスク生成が可能なインターフェイス
    def CreateTaskLine(self) -> TaskLine:
        return TaskLine()