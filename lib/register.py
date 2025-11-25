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
    def __init__(self,required_value_type:type,required_key_type:type=str):
        self.__required_value_type = required_value_type
        self.__required_key_type = required_key_type
        super().__init__()
    def register(self, key, object):
        if isinstance(key,self.__required_key_type):
            if isinstance(object,self.__required_value_type):
                return super().register(key, object)
            else:
                raise TypeError(f"登録できるオブジェクトは {self.__required_value_type} です {type(object)} は使用できません")
        else:
            raise TypeError(f"キー値には {self.__required_key_type} が必要です {type(key)} は使用できません")
    @property
    def required(self):
        return self.__required_value_type