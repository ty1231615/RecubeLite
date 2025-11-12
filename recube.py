import pygame

from lib.session import Session
from lib.sessions.package.difficult import FirstDifficultySession
from lib.progress import Progress
from lib.stage import Stage
from lib.block import Block
from lib.position import Pos
from lib.player import Player
from lib.view import SessionDesignView, Design
from lib.computer import AstarEnemy
from lib.controller import PlayerControleBinder

pygame.init()

screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
runnable = True

block_font = pygame.font.SysFont("arial",50)
entity_font = pygame.font.SysFont("arial",55)

block_design = Design()
block_design.add(Block.AIR, block_font.render("□",True,(0,0,0)))
block_design.add(Block.WALL, block_font.render("■",True,(0,0,0)))
block_design.add(Block.GOAL, block_font.render("■",True,(168, 251, 211)))

player = Player(Pos(0,0))

session = FirstDifficultySession(
    screen,
    Stage(20,10,1),
    40,
    50,
    [
        player
    ],
    [
        AstarEnemy(Pos(0,0),60,True),
    ],
    SessionDesignView(
        block_design,
        entity_font.render("▲",True,(250, 177, 47)),
        entity_font.render("▲",True,(221, 3, 3)),
        10,
        pygame.font.SysFont("arial",150),
        pygame.font.SysFont("arial",80)
    ),
    [
    AstarEnemy(Pos(0,0),55,False),
    AstarEnemy(Pos(0,0),50,False),
    AstarEnemy(Pos(0,0),35,False),
    AstarEnemy(Pos(0,0),30,False),
    AstarEnemy(Pos(0,0),25,False)
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
    screen.blit(session.tick(),(0,0))
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnable = False
        if event.type == pygame.KEYDOWN:
                for handler in player_controller:
                    if handler.key == event.key:
                        handler.command()
