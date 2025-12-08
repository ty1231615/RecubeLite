
from lib.entity import Entity
from lib.enemy import Enemy
from lib.progress import Progress
from lib.position import Pos
from lib.block import BlockData
from lib import util
from package.registers import BlockRegister

import heapq

def astar(grid, start, goal, block_register:BlockRegister):
    """
    2次元グリッド上のA*アルゴリズム
    
    Parameters:
        grid  : 2次元リスト（0: 通過可能, 1: 障害物）
        start : (x, y) スタート座標（タプル）
        goal  : (x, y) ゴール座標（タプル）
    
    Returns:
        path  : スタートからゴールまでの座標リスト（見つからない場合は空リスト）
    """
    # 方向（上下左右）
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # ヒューリスティック関数（マンハッタン距離）
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    # 優先度付きキュー (f, g, 現在位置, 経路)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start, [start]))
    
    # 訪問済みセット
    visited = set()
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        if current in visited:
            continue
        visited.add(current)
        
        # ゴール到達
        if current == goal:
            return path
        
        # 隣接セル探索
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            # 範囲チェック
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                # 通行可能かつ未訪問
                if block_register.is_throughable(grid[ny][nx]) and (nx, ny) not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (new_f, new_g, (nx, ny), path + [(nx, ny)]))
    
    # 経路が見つからない場合
    return []

class ComputeEnemy(Enemy):
    def __init__(self, position: Pos,computeSpeed:int, attackDamage:int, valid:bool) -> None:
        super().__init__(position,attackDamage,valid)
        self.__speed = computeSpeed
        self.__first_speed = computeSpeed
        self.__moveProgress = Progress(0,self.__speed,0,1)
        self.__stayProgress = Progress(0,200,0,-1)
    @property
    def ComputeSpeed(self):
        return self.__speed
    @property
    def firstSpeed(self):
        return self.__first_speed
    @property
    def moveProgress(self):
        return self.__moveProgress
    @property
    def stayProgress(self):
        return self.__stayProgress
    def setComputeSpeed(self,speed):
        self.__speed = speed
        self.__moveProgress.max = self.__speed
    def IncreaseComputeSpeed(self,speed):
        self.__moveProgress.max = self.__moveProgress.max + speed
        self.__speed = self.__moveProgress.max
    def moveNextStep(self,session):
        self.position.movePos(self.nextStep(session))
    def nextStep(self,session) -> Pos:
        return self.position

class AstarEnemy(ComputeEnemy):
    def __init__(self,position:Pos, computeSpeed, attackDamage:int, valid: bool) -> None:
        super().__init__(position,computeSpeed,attackDamage,valid)
    def nextStep(self, session):
        if not self.stayProgress.startline:
            self.stayProgress.next()
            return self.position
        if self.moveProgress.complete:
            self.moveProgress.reset()
            nearPlayer = session.getNearPlayer(self.position)
            if nearPlayer:
                grid = session.get_stage_with_obstacles()
                util.safe_change_grid(grid,self.position.x, self.position.y, BlockData.AIR)
                root = astar(grid,self.position.toTuple(),nearPlayer.position.toTuple(),session.block_register)
                if 1 < len(root):
                    self.position.move(*root[1])
                    session.on_move(self)
        self.moveProgress.next()
        return self.position
