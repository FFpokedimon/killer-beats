import arcade
from PIL import Image

from constants import *


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/player.png")
        self.scale = PLAYER_SIZE / 4096
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.speed = PLAYER_SPEED
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100

    def update(self, delta_time):
        self.center_x += self.speed_x * delta_time
        self.center_y += self.speed_y * delta_time
        self.center_x = max(self.width / 2, min(SCREEN_WIDTH - self.width / 2, self.center_x))
        self.center_y = max(self.height / 2, min(SCREEN_HEIGHT - self.height / 2, self.center_y))
