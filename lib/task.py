


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
        if self.delete:
            del self
            return
    def __del__(self):
        if self in SimpleTask._INSTANCE:
            SimpleTask._INSTANCE.remove(self)