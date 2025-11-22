import types

class NotRegistedError(Exception):
    """
    レジスターから参照できなかった場合
    """

class NamespaceRegister:
    def __init__(self):
        self.__registed = {}
    def register(self,key,object):
        self.__registed.update({key:object})
    def get(self,key):
        value = self.__registed.get(key)
        if not value:
            raise NotRegistedError(f"キー値: '{key}' は参照できませんでした")
        return value
    def iter(self):
        for registed in self.__registed:
            yield (registed, self.__registed[registed])

class TypeRegister(NamespaceRegister):
    def __init__(self,required_type:type):
        self.__required_type = required_type
        super().__init__()
    def register(self, key, object):
        if isinstance(object,self.__required_type):
            return super().register(key, object)
        raise TypeError(f"期待されるオブジェクトは {self.__required_type} です {type(object)} は使用できません")
    @property
    def required(self):
        return self.__required_type