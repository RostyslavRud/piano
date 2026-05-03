from pygame import*
class Button(Rect):
    def __init__(self, x, y, width, height, command, text = "",):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.command = command
    def draw(self, window, x, y, width, height):
        draw.rect(window, (255, 255, 255), x, y, width, height)
    def action(self, e):
        if e.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(e.pos):
                self.command()
            return None


