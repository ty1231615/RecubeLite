from lib.stage import Stage
from lib.player import Player
from lib.computer import ComputeEnemy
from lib.view import SessionDesignView
from lib.position import Pos
from lib.block import BlockData,BlockRegister
from lib.task import SimpleTask
from lib.progress import Progress
from lib.health import Health
from lib import config
from lib.particle.shaking import ShakingCamera
from lib import util

import pygame
import random
import copy

class Session:
    LEVEL_MODIFIER = "LevelModifier"
    def __init__(self,surface:pygame.Surface,stage:Stage, stageLevel:int, maxStageLevel:int, health:Health, players:list[Player],enemys:list[ComputeEnemy],view:SessionDesignView,block_register:BlockRegister) -> None:
        self.__stage = stage
        self.__defaut_stage_level = stageLevel
        self.__maxStageLevel = maxStageLevel
        self.__health = health
        self.__default_health_data = (health.hp,health.max_hp)
        self.__players = players
        self.__goal_position = Pos(0,0)
        self.__enemys = enemys
        self.__view = view
        self.__surface = surface
        self.__render_details:list[list[Pos]] = self.__stage.makeStageDelta(Pos(0,0))
        self.__block_register = block_register
        self.enemy_stayframe = 120
        self.__stay_clock = Progress(0, 1000, 0, -1) #プログレスが1以上ならtickで何も行わない
    def gameInit(self):
        self.__count_stage = 1
        self.__health = Health(self.__default_health_data[0],self.__default_health_data[1])
        self.__game_over = False
        self.__stage.level = self.__defaut_stage_level
    def start(self):
        self.loadLevel()
        self.all_player_wave_particle()
    def createStage(self):
        self.stage.resetStage()
        self.stage.ScatterWall(self.__maxStageLevel)
        self.__render_details = self.__stage.makeStageDelta(Pos(0,0))
    def check_restart(self):
        if self.__game_over:
            self.restart()
    def restart(self):
        self.gameInit()
        self.loadLevel()
        self.all_player_wave_particle()
    def all_player_wave_particle(self):
        for player in self.get_players():
            self.player_wave_particle(player)
    def player_wave_particle(self,player:Player):
        particle_pos = util.safe_get_grid(self.__render_details,player.position.x,player.position.y)
        if particle_pos:
            particle_pos = Pos(particle_pos.x,particle_pos.y)
            #プレイヤーの中心になるようにパーティクルの位置を調整
            particle_pos.x = particle_pos.x + int(self.view.playerDesign.get_width() / 2)
            particle_pos.y = particle_pos.y + int(self.view.playerDesign.get_height() / 2)
            self.view.playerWaveParticle(self.__surface,particle_pos.toTuple(),30, (255, 128, 64))
    def stay_shake(self,frame):
        self.stay_clock.current = frame
        ShakingCamera(Progress(0,frame,0,1),20,40)
    def loadLevel(self):
        self.createStage()
        self.draw_stage()
        positions = self.stage.getAirSpace(self.__block_register)
        for player in self.__players:
            position = random.choice(positions)
            player.position.movePos(position)
            positions.remove(position)
        if len(self.__players) != 0: #プレイヤーがいる場合のみゴールを作成
            self.__goal_position = self.decide_arrive_goal_positions(random.choice(self.__players).position,100)
            self.stage.createGoal(self.__goal_position)
        for enemy in self.get_enemys():
            position = random.choice(positions)
            enemy.position.movePos(position)
            positions.remove(position)
            #ステージのレベルごとのコンピューターの計算速度を更新
            current_level = self.stage.level
            enemy.moveProgress.MAX_MODIFIER.add(Session.LEVEL_MODIFIER,-current_level)
            enemy.stayProgress.current = self.enemy_stayframe
    def tick(self) -> pygame.Surface:
        #この関数を毎フレーム呼び出す
        if self.__game_over:
            self.draw_game_over()
            return self.__surface
        self.compute_enemys() #敵の移動計算
        self.draw_enemys() #敵の描画
        self.draw_players() #プレイヤーの描画
        self.draw_stage() #マップの描画
        self.check_goal() #ゴール到達の確認
        self.check_damage() #ダメージの確認
        SimpleTask.AllInstanceRun() #シンプルタスクの実行
        return self.__surface
    def arrive_position(self,position:Pos,step:int=100,visited=[]) -> list[Pos]:
        if step <= 0:
            return visited
        for pos in reversed(visited):
            if position.equals(pos):
                return visited
        if not self.can_move(position):
            return visited
        visited.append(position)
        self.arrive_position(position.above(1),step-1,visited)
        self.arrive_position(position.below(1),step-1,visited)
        self.arrive_position(position.left(1),step-1,visited)
        self.arrive_position(position.right(1),step-1,visited)
        return visited
    def decide_arrive_goal_positions(self,fromPosition:Pos,step:int=100) -> Pos:
        arrive_positions = self.arrive_position(fromPosition,step,[])
        if fromPosition in arrive_positions:
            arrive_positions.remove(fromPosition)
        if len(arrive_positions) == 0:
            return fromPosition
        return random.choice(arrive_positions)
    def can_move(self,position:Pos) -> bool:
        if not self.stay_clock.startline:
            return False
        if 0 <= position.x < self.stage.width and 0 <= position.y < self.stage.height:
            block = self.stage.stage[position.y][position.x]
            if self.block_register.is_throughable(block): #移動可能なブロックであるかどうか
                return True
        return False
    def goal(self):
        self.__count_stage += 1
        self.stage.level += 1
        self.loadLevel()
        self.all_player_wave_particle()
    def check_damage(self):
        for player in self.get_players():
            for enemy in self.get_enemys():
                if player.position.equals(enemy.position):
                    self.health.damage(enemy.damage)
                    print(self.health.get_hit_point())
                    if self.health.is_dead():
                        self.__game_over = True
                        return
                    self.loadLevel()
                    self.stay_shake(config.base_frame_rate / 5)
                    return
    def check_goal(self):
        for player in self.get_players():
            if self.__goal_position.equals(player.position):
                self.goal()
                return
    def draw_game_over(self):
        self.__surface.fill((0,0,0))
        game_over_text = self.__view.gameOverFont.render("YOU DIED",True,(255,0,0))
        self.__surface.blit(game_over_text,(self.__surface.get_width() / 2 - game_over_text.get_width() / 2,self.__surface.get_height() / 5))
        result_text = self.__view.resultTextFont.render(f"STAGE REACHED: {self.__count_stage}",True,(255,255,255))
        self.__surface.blit(result_text,(self.__surface.get_width() / 2 - result_text.get_width() / 2,self.__surface.get_height() / 2))
    def draw_stage(self):
        for y in range(len(self.stage.stage)):
            for x in range(len(self.stage.stage[y])):
                no_draw = False
                for entity in self.entity_itereter():
                    if entity.position.equals(Pos(x,y)):
                        no_draw = True
                if no_draw:
                    continue
                block = self.stage.stage[y][x]
                blockSurface = self.__view.blockDesigns.get(block)
                rect = self.__surface.blit(blockSurface,((x+1) * self.__view.blockPadding + blockSurface.get_width() * x,1 + y * self.__view.blockPadding + blockSurface.get_height() * (y+1)))
                self.__render_details[y][x] = Pos(rect.x,rect.y)
    def draw_players(self):
        for player in self.get_players():
            pos = self.__render_details[player.position.y][player.position.x]
            self.__surface.blit(self.__view.playerDesign, (pos.x,pos.y))
    def draw_enemys(self):
        for enemy in self.get_enemys():
            pos = self.__render_details[enemy.position.y][enemy.position.x]
            self.__surface.blit(self.__view.enemyDesign, (pos.x, pos.y))
    def compute_enemys(self):
        for enemy in self.get_enemys():
            enemy.moveNextStep(self)
    def entity_itereter(self):
        for player in self.get_players():
            yield player
        yield from self.get_enemys()
    def get_players(self):
        for player in self.__players:
            yield player
    def get_enemys(self):
        for enemy in self.__enemys:
            if enemy.valid:
                yield enemy
    def getNearPlayer(self,fromPosition:Pos):
        if 0 < len(self.__players): #プレイヤーがいなければ終了する
            nearPlayer = self.__players[0]
            near_distance = fromPosition.distanceTo(nearPlayer.position)
            for player in self.__players:
                distance = fromPosition.distanceTo(player.position)
                if distance < near_distance:
                    near_distance = distance
                    nearPlayer = player
            return nearPlayer
        return
    def get_stage_with_obstacles(self):
        grid = copy.deepcopy(self.stage.stage)
        for entity in self.get_enemys():
            grid[entity.position.y][entity.position.x] = BlockData.WALL
        return grid
    @property
    def stage(self):
        return self.__stage
    @property
    def health(self):
        return self.__health
    @property
    def players(self):
        return self.__players
    @property
    def enemys(self):
        return self.__enemys
    @property
    def view(self):
        return self.__view
    @property
    def block_register(self):
        return self.__block_register
    @property
    def stay_clock(self):
        return self.__stay_clock