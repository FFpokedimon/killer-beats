import arcade

from constants import *
from game_objects.bullet_sprite import Bullet
from game_objects.player_sprite import Player
from game_objects.slash_sprite import Slash


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = BACKGROUND_COLOR

    def setup(self):
        self.pressed = set()

        self.player = Player()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

        self.slashes = arcade.SpriteList()
        self.slashes.append(Slash())

        self.bullets = arcade.SpriteList()
        self.bullets.append(Bullet((self.player.center_x, self.player.center_y)))

        self.health_text = arcade.Text(f'Health: {self.player.health}', 10, SCREEN_HEIGHT, font_size=20,
                                       color=tuple(map(lambda x: 255 - x, BACKGROUND_COLOR[:-1])))
        self.health_text.y = self.health_text.y - self.health_text.content_size[1]

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.slashes.draw()
        self.bullets.draw()
        self.health_text.draw()

    def on_update(self, delta_time):
        if arcade.key.A in self.pressed:
            self.player.speed_x = -self.player.speed
        if arcade.key.D in self.pressed:
            self.player.speed_x = self.player.speed
        if arcade.key.S in self.pressed:
            self.player.speed_y = -self.player.speed
        if arcade.key.W in self.pressed:
            self.player.speed_y = self.player.speed

        if self.slashes[-1].timer >= SLASH_FREQUENCY:
            self.slashes.append(Slash())
        elif self.slashes[-1].timer >= SLASH_DAMAGE_TIME[1]:
            self.slashes[-1].damage_state[0] = False
        elif self.slashes[-1].timer >= SLASH_DAMAGE_TIME[0]:
            self.slashes[-1].damage_state[0] = True

        if self.bullets[-1].timer >= BULLET_FREQUENCY:
            self.bullets.append(Bullet((self.player.center_x, self.player.center_y)))

        if arcade.check_for_collision_with_list(self.player, self.slashes):
            for slash in range(len(self.slashes)):
                if not self.slashes[slash].damage_state[1] and self.slashes[slash].damage_state[0]:
                    if arcade.check_for_collision(self.player, self.slashes[slash]):
                        self.slashes[slash].damage_state[0] = False
                        self.slashes[slash].damage_state[1] = True
                        self.player.health -= SLASH_DAMAGE
                        if self.player.health <= 0:
                            exit()
                        self.health_text.text = f'Health: {self.player.health}'
                        break

        if arcade.check_for_collision_with_list(self.player, self.bullets):
            for bullet in range(len(self.bullets)):
                if arcade.check_for_collision(self.player, self.bullets[bullet]):
                    self.bullets[bullet].remove_from_sprite_lists()
                    self.player.health -= BULLET_DAMAGE
                    if self.player.health <= 0:
                        exit()
                    self.health_text.text = f'Health: {self.player.health}'
                    break

        self.player_list.update()
        self.slashes.update()
        self.bullets.update()

    def on_key_press(self, key, modifiers):
        self.pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.pressed.remove(key)
        if key == arcade.key.W or key == arcade.key.S:
            self.player_list[0].speed_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_list[0].speed_x = 0
