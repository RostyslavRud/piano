from pygame import *
class Slider:
    def __init__(self, x, y, width, min_val, max_val, step=1, initial=None, label = "", value_to_text= None):
        self.track_rect = Rect(x, y, width, 6)
        self.handle_radius = 10
        self.min = float(min_val)
        self.max = float(max_val)
        self.step = float(step)
        if initial is not None:
            self.value = float(initial)
        else:
            self.value = float(min_val)
        self.label = label
        self.value_to_text = value_to_text
        self.dragging = False

        self._hit_rect = Rect(0,0, self.handle_radius*2+8, self.handle_radius*2+8 )
        def set_on_change(self, cb):
            self.on_change = cb
        def _clamp(self, v: float) -> float:
            v = max(self.min, min(self.max, v))
            if self.step > 0:
                v = round(v / self.step) * self.step
            return max(self.min, min(self.max, v))
        def _pos_to_val(self, px: int) -> float:
            ratio = (px - self.tracl_rect.left) / self.track_rect.width
            return self._clamp(self.min + ratio * (self.max - self.min))
        def val_to_pos(self) -> int:
            if self.max == self.min:
                return self.track_rect.left
            ratio = (self.value - self.min) / (self.max - self.min)
            return int(self.track_rect.left + ratio * self.track_rect.width)
        def draw(self, window, font = None):
            draw.rect(window, (210, 210, 210), self.track_rect, border_radious = 3)
            draw.rect(window, (60, 60, 60), self.track_rect, 1,  border_radious=3)

            hx = self.val_to_pos()
            hy = self.track_rect_centery()
            draw.circle(window, (40, 40, 40), (hx, hy), self.handle_radius)

            if font and self.label:
                if callable(self.value_to_text):
                    vtxt = self.value_to_text(self.value)
                else:
                    vtxt = f"{int(self.value)}"
                text  = font.render(f"{self.label}: {vtxt}", True, (0,0,0))
                window.blit(text, (self.track_rect.left, self.track_rect.top - 28))
            self._hit_rect_center = (hx, hy)
        def handle_event(self, event):
            old = self.value
            if event.type == MOUSEBUTTONDOWN:
                if self.track.rect.collidepoint(event.pos) or self._hit_rect_collidepoint(event.pos):
                    self.dragging = True
                    self.value = self._pos_to_val(event.pos[0])
            elif event.type == MOUSEMOTION and self.dragging:
                self.value = self._pos_to_val(event.pos[0])
            elif event.type == MOUSEBUTTONUP and self.dragging:
                self.dragging = False
                self.value = self.pos_to_val(event.pos[0])
            if self.value != old and hasattr(self, "on_change") and self.on_change:
                self.on_change(self.value)
