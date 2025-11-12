


def safe_change_grid(grid, x, y, new_block):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x] = new_block