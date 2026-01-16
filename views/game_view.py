import arcade
from pyglet.graphics import Batch

from constants import *
from game_objects.player_sprite import Player
from game_objects.slash_sprite import Slash


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.WHITE

    def setup(self):
        self.pressed = set()
        self.player = arcade.SpriteList()
        self.player.append(Player())
        self.slashes = arcade.SpriteList()
        self.slash_timer = 0

    def on_draw(self):
        self.clear()
        self.player.draw()
        self.slashes.draw()

    def on_update(self, delta_time):
        if arcade.key.A in self.pressed:
            self.player[0].speed_x = -self.player[0].speed
        if arcade.key.D in self.pressed:
            self.player[0].speed_x = self.player[0].speed
        if arcade.key.S in self.pressed:
            self.player[0].speed_y = -self.player[0].speed
        if arcade.key.W in self.pressed:
            self.player[0].speed_y = self.player[0].speed

        self.slash_timer += delta_time
        if self.slash_timer >= SLASH_FREQUENCY:
            self.slash_timer = 0
            self.slashes.append(Slash())
        if arcade.check_for_collision_with_list(self.player[0], self.slashes):
            print("ракета не лететь, ракета ломаться")

        self.player.update()
        self.slashes.update()

    def on_key_press(self, key, modifiers):
        self.pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.pressed.remove(key)
        if key == arcade.key.W or key == arcade.key.S:
            self.player[0].speed_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player[0].speed_x = 0
