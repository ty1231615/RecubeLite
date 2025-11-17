import pathlib

base_frame_rate = 60



def get_font_path(name):
    return pathlib.Path(f"asset/fonts/{name}")