import pygame

import lib.config as config
from lib.sessions.package.difficult import FirstDifficultySession
from lib import config
from lib.progress import Progress
from lib.stage import Stage
from lib.health import Health
from lib.block import BlockData
from lib.registers import BlockRegister
from lib.position import Pos
from lib.player import Player
from lib.items import HealOrb,StunOrb,SlowOrb,ReductionBlockOrb
from lib.view import Design
from lib.sessions.itemSession import ItemSessionDesign
from lib.computer import AstarEnemy
from lib.controller import PlayerControleBinder
from lib.particle.camera import CURRENT_CAMERA

pygame.init()

screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
runnable = True

block_font = pygame.font.SysFont("arial",40)
entity_font = pygame.font.SysFont("arial",45)

block_design = Design()
block_design.register(BlockData.AIR, block_font.render("□",True,(0,0,0)))
block_design.register(BlockData.WALL, block_font.render("■",True,(0,0,0)))
block_design.register(BlockData.GOAL, block_font.render("■",True,(0, 70, 255)))

player = Player(Pos(0,0))
player.setSpeed(1)

block_register = BlockRegister.DefaultRegister()

session = FirstDifficultySession(
    screen,
    Stage(32,19,1),
    100,
    500,
    Health(5,1000),
    [
        player
    ],
    [
        AstarEnemy(Pos(0,0),60,1,True),
    ],
    ItemSessionDesign(
        block_design,
        entity_font.render("▲",True,(250, 177, 47)),
        entity_font,
        "▲",
        5,
        pygame.font.SysFont("arial",150),
        pygame.font.SysFont("arial",80),
        pygame.font.Font(str(config.fonts[1]),150),
        entity_font.render("■",True,(0, 126, 110)),
        entity_font.render("■",True,(191, 26, 26))
    ),
    block_register,
    [
    AstarEnemy(Pos(0,0),55,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),35,1,False),
    AstarEnemy(Pos(0,0),30,1,False),
    AstarEnemy(Pos(0,0),25,1,False),
    AstarEnemy(Pos(0,0),20,1,False),
    AstarEnemy(Pos(0,0),15,1,False),
    AstarEnemy(Pos(0,0),10,1,False),
    #これ以降は一定の速度のエネミーを配置
    AstarEnemy(Pos(0,0),15,1,False),
    AstarEnemy(Pos(0,0),14,1,False),
    AstarEnemy(Pos(0,0),13,1,False),
    AstarEnemy(Pos(0,0),12,1,False),
    AstarEnemy(Pos(0,0),11,1,False),
    AstarEnemy(Pos(0,0),10,1,False),
    AstarEnemy(Pos(0,0),9,1,False),
    AstarEnemy(Pos(0,0),8,1,False),
    AstarEnemy(Pos(0,0),7,1,False),
    AstarEnemy(Pos(0,0),6,1,False),
    AstarEnemy(Pos(0,0),5,1,False),
    AstarEnemy(Pos(0,0),4,1,False),
    ],
    Progress(0,5,0,1),
    (HealOrb(),StunOrb(),SlowOrb(5),ReductionBlockOrb(4)),
    ()
)

session.gameInit()

player_controller = [
        PlayerControleBinder(pygame.K_w,lambda: player.above(session)),
        PlayerControleBinder(pygame.K_s,lambda: player.below(session)),
        PlayerControleBinder(pygame.K_a,lambda: player.left(session)),
        PlayerControleBinder(pygame.K_d,lambda: player.right(session)),
        #矢印でも操作できるようにする
        PlayerControleBinder(pygame.K_UP,lambda: player.above(session)),
        PlayerControleBinder(pygame.K_DOWN,lambda: player.below(session)),
        PlayerControleBinder(pygame.K_LEFT,lambda: player.left(session)),
        PlayerControleBinder(pygame.K_RIGHT,lambda: player.right(session)),
        #スペースでリロード
        PlayerControleBinder(pygame.K_SPACE,lambda: session.check_restart()),
        #ESCでポーズ
        PlayerControleBinder(pygame.K_ESCAPE,lambda: session.switch_pause())
    ]

player.set_controller(player_controller)

session.start()

while runnable:
    screen.fill((255,255,255))
    screen.blit(session.tick(),CURRENT_CAMERA.to_tuple())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnable = False
        if event.type == pygame.KEYDOWN:
            for player in session.get_players():
                for handler in player.controller:
                    if handler.key == event.key:
                        handler.command()
    pygame.display.update()
    clock.tick(config.base_frame_rate)

