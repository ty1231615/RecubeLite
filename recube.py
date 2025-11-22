import pygame

import lib.config as config
from lib.sessions.package.difficult import FirstDifficultySession
from lib import config
from lib.progress import Progress
from lib.stage import Stage
from lib.health import Health
from lib.block import BlockData,BlockRegister
from lib.position import Pos
from lib.player import Player
from lib.view import SessionDesignView, Design
from lib.computer import AstarEnemy
from lib.controller import PlayerControleBinder
from lib.particle.camera import CURRENT_CAMERA

pygame.init()

fonts = [
    config.get_font_path("Greek-Freak.ttf"),
    config.get_font_path("kaisoutai.ttf")
]

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
    Health(5,5),
    [
        player
    ],
    [
        AstarEnemy(Pos(0,0),60,1,True),
    ],
    SessionDesignView(
        block_design,
        entity_font.render("▲",True,(250, 177, 47)),
        entity_font.render("▲",True,(221, 3, 3)),
        5,
        pygame.font.SysFont("arial",150),
        pygame.font.SysFont("arial",80),
        pygame.font.Font(str(fonts[1]),150)
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
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False),
    AstarEnemy(Pos(0,0),50,1,False)
    ],
    Progress(0,5,0,1)
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
    ]

session.start()

while runnable:
    screen.fill((255,255,255))
    screen.blit(session.tick(),CURRENT_CAMERA.to_tuple())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnable = False
        if event.type == pygame.KEYDOWN:
            for handler in player_controller:
                if handler.key == event.key:
                    handler.command()
    pygame.display.update()
    clock.tick(config.base_frame_rate)

