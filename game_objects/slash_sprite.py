import random
import arcade
from PIL import Image

from constants import *


class Slash(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x, self.center_y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
        self.angle = random.randint(0, 360)
        self.timer = 0
        self.stage = 0
        self.texture = arcade.texture.Texture(Image.new("RGBA", (self.stage + 1, 4096), "red"))
        self.alpha = 0
        self.damage_state = [False, False]

    def update(self, delta_time):
        self.timer += delta_time
        self.stage = int(self.timer // SLASH_TIME) + 1
        self.alpha = self.stage * 6
        if self.stage >= SLASH_STAGES:
            self.remove_from_sprite_lists()
        elif self.stage >= SLASH_STAGES / 2:
            self.texture = arcade.texture.Texture(
                Image.new("RGBA", (SLASH_STAGES + 1 - self.stage, 4096), (255, (SLASH_STAGES - self.stage) * 5, 0))
            )
        else:
            self.texture = arcade.texture.Texture(
                Image.new("RGBA", (self.stage, 4096), (255, self.stage * 5, 0))
            )
