import random
import arcade
from PIL import Image

from constants import *


class Slash(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.current_stage = 1
        self.timer = 0
        self.int_timer = self.timer
        self.alpha = 0
        self.texture = arcade.texture.Texture(Image.new("RGBA", (self.stage, 4096), "red"))
        self.center_x, self.center_y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
        self.angle = random.randint(0, 360)

    def update(self, delta_time):
        self.timer += delta_time
        self.current_stage = int(self.timer // SLASH_TIME)
        self.alpha = self.stage * 10
        if self.stage >= SLASH_STAGES:
            self.kill()
        elif self.stage < self.current_stage:
            self.stage += 1
            self.texture = arcade.texture.Texture(Image.new("RGBA", (SLASH_STAGES + 1 - self.stage, 4096), "red"))
