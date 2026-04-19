from pygame import draw
from settings import  Black

def draw_key_effect(window, rect, is_pressed = False):
    base_color = (220, 220, 220) if not is_pressed else (170, 220, 255)
    border_color = Black

    draw.rect(window, base_color, rect, border_radius=8)
    draw.rect(window, border_color, rect,2, border_radius=8)