
from lib.particle.waveCircle import WaveCircle
from lib.entity import Entity

def safe_change_grid(grid, x, y, new_block):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x] = new_block

def safe_get_grid(grid, x ,y, default=None):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return grid[y][x]
    return default