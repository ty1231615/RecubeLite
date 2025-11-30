from pygame import Surface

from lib.item import Item
from lib.sessions.itemSession import ItemSession,ItemSessionDesign
from lib.computer import ComputeEnemy
from lib.player import Player
from lib.progress import Progress
from lib.stage import Stage
from lib.view import SessionDesignView
from lib.registers import BlockRegister
from lib.health import Health

class FirstDifficultySession(ItemSession):
    """
    進んだステージに応じて新たな敵が出現する
    """
    def __init__(self, surface: Surface, stage: Stage, stageLevel: int, maxStageLevel: int, health: Health, players: list[Player], enemys: list[ComputeEnemy], view: ItemSessionDesign, block_register:BlockRegister, addEnemys:list[ComputeEnemy], enemySpawnProgress: Progress, support_items:tuple[Item], assist_items:tuple[Item]) -> None:
        super().__init__(surface, stage, stageLevel, maxStageLevel, health, players, enemys, view, block_register, support_items, assist_items)
        self.__enemy_spawn_progress = enemySpawnProgress
        self.__enemy_spawn_step = Progress(0,len(addEnemys)-1,0,1)
        self.__addEemys = addEnemys
        self.CheckAddEnemy()
    @property
    def addEnemys(self):
        return self.__addEemys
    @addEnemys.setter
    def addEnemys(self, value):
        self.__addEemys = value
        self.enemy_spawn_step.max = len(self.__addEemys)
    def gameInit(self):
        super().gameInit()
        self.InvalidAllnewEnemy()
        self.enemy_spawn_progress.reset()
        self.enemy_spawn_step.reset()
    def InvalidAllnewEnemy(self):
        for enemy in self.addEnemys:
            enemy.invalid()
    def CheckAddEnemy(self):
        step = self.enemy_spawn_step.current
        if step >= 0 and step <= len(self.addEnemys):
            new_enemy = self.addEnemys[step]
            new_enemy.active()
            new_enemy.stayProgress.current = self.enemy_stayframe
    def goal(self):
        super().goal()
        self.enemy_spawn_progress.next()
        if self.enemy_spawn_progress.complete:
            self.CheckAddEnemy()
            if not self.enemy_spawn_step.complete:
                self.enemy_spawn_step.next()
            self.enemy_spawn_progress.reset()
    def get_enemys(self):
        yield from super().get_enemys()
        for enemy in self.addEnemys:
            if enemy.valid:
                yield enemy
    @property
    def enemy_spawn_progress(self):
        return self.__enemy_spawn_progress
    @property
    def enemy_spawn_step(self):
        return self.__enemy_spawn_step