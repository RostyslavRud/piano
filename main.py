from pygame import*
from pygame.examples.audiocapture import sounds

from settings import Win_Width, Win_Height, White, Keys
from keys import create_key_rects, draw_keys

init()
keys_list = list(Keys.keys())
pressed = set()
key_rects = create_key_rects()
window = display.set_mode((Win_Width, Win_Height))
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    window.fill(White)
    draw_keys(window, key_rects, pressed)
    display.update()

    if e.type == KEYDOWN:
        k =key.name(e.key)
        if k in sounds:
            sounds[k].play()
            pressed.add(keys_list.index(k))

    if e.type == KEYUP:
        k =key.name(e.key)
        if k in Keys:
            pressed.discard(keys_list.index(k))
    if e.type == MOUSEBUTTONDOWN:
        for i, r in enumerate(key_rects):
            if r.collidepoint(e.pos):
                sounds[keys_list[i]].play()
                pressed.add(i)
    if e.type == MOUSEBUTTONUP:
        for i, r in enumerate(key_rects):
            if i in pressed and r.collidepoint(e.pos):
                pressed.remove(i)

