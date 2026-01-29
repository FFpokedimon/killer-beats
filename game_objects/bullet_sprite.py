import random
import arcade
from math import sin, cos, atan2, degrees

from constants import *


class Bullet(arcade.Sprite):
    def __init__(self, player_coords):
        super().__init__()
        if random.choice([True, False]):
            self.center_x, self.center_y = (random.choice([-BULLET_WIDTH, BULLET_WIDTH]),
                                            random.randint(-BULLET_WIDTH, SCREEN_HEIGHT + BULLET_WIDTH))
        else:
            self.center_x, self.center_y = (random.randint(-BULLET_WIDTH, SCREEN_WIDTH + BULLET_WIDTH),
                                            random.choice([-BULLET_WIDTH, BULLET_WIDTH]))
        self.angle = atan2(player_coords[1] - self.center_y, player_coords[0] - self.center_x)
        self.timer = 0
        self.speed = BULLET_SPEED
        self.changed_x = cos(self.angle) * self.speed
        self.changed_y = sin(self.angle) * self.speed
        self.angle = degrees(-self.angle)
        self.texture = arcade.load_texture('assets/bullet.png')
        self.scale = 0.1

    def update(self, delta_time):
        self.timer += delta_time
        self.center_x += self.changed_x * delta_time
        self.center_y += self.changed_y * delta_time
        if not -BULLET_WIDTH * 2 < self.center_x < SCREEN_WIDTH + BULLET_WIDTH * 2:
            self.remove_from_sprite_lists()
        elif not -BULLET_WIDTH * 2 < self.center_y < SCREEN_HEIGHT + BULLET_WIDTH * 2:
            self.remove_from_sprite_lists()
