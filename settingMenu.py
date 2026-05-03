from pygame import*
class SettingsMenu:
    def __init__(self, window_rect, initial_volume, initial_keys, min_keys, max_keys, on_change, on_back):
        self.window_rect = window_rect
        self.on_change = on_change
        self.on_back = on_back

        cx = window_rect.centerx
        top = 140

        back_idle = transform.scale(image.load('assets/images/buttons/exit_unhover.png'), (48, 48))

        back_hover = transform.scale(image.load('assets/images/buttons/exit_hover.png'), (48, 48))

    def _on_volume(self,v):
        if self.on_change:
            self.on_change(float(v), int(self.keys_slider.value))
    def _on_keys(self, v):
        if self.on_change:
            self.on_change(float(self.volume_slider.value), int(v))
    def _back(self):
        if self.on_back:
            self.on_back()
    def handle_event(self, event):
        self.back_btn.handle_event(event)
        self.volume_slider.handle_event(event)
        self.keys_slider.handle_event(event)
    def draw(self, window, font):
        title = font.render("Налаштування", True, (0,0,0))
        window.blit(title, title.get_rect(center=(self.window_rect.centerx, 80)))

        self.back_btn.draw(window, font)
        self.volume_slider.draw(window, font)
        self.keys_slider.draw(window, font)
