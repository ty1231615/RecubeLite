
from pygame import Surface
from lib.computer import ComputeEnemy
from lib.player import Player
from lib.progress import Progress
from lib.sessions.levelSession import StepWithLevelSession
from lib.stage import Stage
from lib.view import SessionDesignView
from lib.enemy import Enemy
from lib.block import BlockRegister

class FirstDifficultySession(StepWithLevelSession):
    """
    進んだステージに応じて新たな敵が出現する
    """
    def __init__(self, surface: Surface, stage: Stage, stageLevel: int, maxStageLevel: int, players: list[Player], enemys: list[ComputeEnemy], view: SessionDesignView, block_register:BlockRegister, addEnemys:list[ComputeEnemy], levelStepProgress: Progress) -> None:
        super().__init__(surface, stage, stageLevel, maxStageLevel, players, enemys, view, block_register, levelStepProgress, Progress(0, len(addEnemys)-1, 0, 1))
        self.__addEemys = addEnemys
        self.CheckAddEnemy()
    @property
    def addEnemys(self):
        return self.__addEemys
    @addEnemys.setter
    def addEnemys(self, value):
        self.__addEemys = value
        self.GimicStep.max = len(self.__addEemys)
    def gameInit(self):
        super().gameInit()
        self.addenemyInvalidAll()
        self.CheckAddEnemy()
    def addenemyInvalidAll(self):
        for enemy in self.addEnemys:
            enemy.invalid()
    def CheckAddEnemy(self):
        step = self.GimicStep.current
        if step > 0 and step <= len(self.addEnemys):
            new_enemy = self.addEnemys[step]
            new_enemy.active()
            new_enemy.stayProgress.current = self.enemy_stayframe
    def OnGimicStep(self):
        self.CheckAddEnemy()
    def get_enemys(self):
        yield from super().get_enemys()
        for enemy in self.addEnemys:
            if enemy.valid:
                yield enemy