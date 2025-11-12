
from lib.computer import ComputeEnemy
from lib.player import Player
from lib.session import Session
from lib.stage import Stage
from lib.view import SessionDesignView
from lib.progress import Progress

import pygame

#use abstract session
class StepWithLevelSession(Session):
    """
    進んだレベルに応じて変化を加えるセッション
    """
    def __init__(self, surface: pygame.Surface, stage: Stage, stageLevel: int, maxStageLevel: int, players: list[Player], enemys: list[ComputeEnemy], view: SessionDesignView, levelStepProgress: Progress, GimicStep: Progress) -> None:
        super().__init__(surface, stage, stageLevel, maxStageLevel, players, enemys, view)
        self.__levelStepProgress = levelStepProgress
        self.__GimicStep = GimicStep
    @property
    def levelStepProgress(self):
        #levelStepで○○回レベルに到達するごとにGimicStepを増加させるような仕組み
        return self.__levelStepProgress 
    @property
    def GimicStep(self):
        #GimicStepでギミック数を管理
        return self.__GimicStep
    def gameInit(self):
        super().gameInit()
        self.levelStepProgress.reset()
        self.GimicStep.reset()
    def goal(self):
        super().goal()
        self.levelStepProgress.next()
        self.OnLevelStepUp()
        if self.levelStepProgress.complete:
            self.levelStepProgress.reset()
            #ギミックの最大ステップ数を増やす
            self.GimicStep.next()
            self.OnGimicStep()
    def OnGimicStep(self):
        """
        ギミックステップが増えたときに呼ばれる関数
        """
    def OnLevelStepUp(self):
        """
        レベルが上がったときに呼ばれる関数
        """