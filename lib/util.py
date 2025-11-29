from lib.particle.waveCircle import WaveCircle
from lib.entity import Entity
from lib import config
import pygame

def safe_change_grid(grid, x, y, new_block):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x] = new_block

def safe_get_grid(grid, x ,y, default=None):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return grid[y][x]
    return default

def maximum(x,y):
    if x > y:
        return y
    return x

def minimum(x,y):
    if x <= y:
        return y
    return x

def frame_to_second(second:int) -> int:
    return config.base_frame_rate * second

def get_difference_base_frame(frame):
    return config.base_frame_rate / frame

def item_image_load(image_name):
    return pygame.image.load("asset/images/item/" + image_name)