from lib.item import ItemBox, Item
from lib.entity import Entity
from lib.player import Player
from lib.config import fonts
from lib.position import Pos
from package.sessions.itemSelector import ItemSelection

# annotation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from package.sessions.itemSession import ItemSession


class NormalItemBox(ItemBox):
    def __init__(self, items: tuple[Item]):
        super().__init__(items)
    def lottery(self,session:'ItemSession',entity:Entity,replace_position:Pos) -> bool:
        if isinstance(entity,Player):
            selector = ItemSelection(session,entity,self,replace_position,str(fonts[1]),380,self.items)
            session.task_line_handler.register(ItemSelection.NAMESPACE,selector.CreateTaskLine())
            return True
        return False
