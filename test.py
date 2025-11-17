
from lib.progress import Progress
from lib.task import Task,TaskLine,TaskType
from lib import util
import pygame

clock = pygame.time.Clock()

line = TaskLine()

line.add(
    Task(
        lambda: print("Hello"),
        TaskType.AFTER_STANDING,
        Progress(0,60,0,1),
    )
)

line.add(
    Task(
        lambda: print("World"),
        TaskType.AFTER_STANDING,
        Progress(0,util.frame_to_second(1),0,1)
    )
)

line.add(
    Task(
        lambda: print("TOU!!"),
        TaskType.AFTER_STANDING,
        Progress(0,60,0,1)
    )
)

while True:
    clock.tick(60)
    line.ticking()

    