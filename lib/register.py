
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
