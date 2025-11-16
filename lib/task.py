


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