import arcade

from constants import *
from views.pause_view import PauseView
from views.end_view import EndScreenView
from game_objects.bullet_sprite import Bullet
from game_objects.player_sprite import Player
from game_objects.slash_sprite import Slash
from music_analysis import get_wav_duration


class GameView(arcade.View):
    def __init__(self, song, drums, menu_view):
        super().__init__()
        self.background_color = BACKGROUND_COLOR
        self.texture = arcade.load_texture('assets/background.png')
        self.song = song
        self.beats = drums
        self.menu_view = menu_view

    def setup(self):
        self.pressed = set()
        self.timer = 0
        self.count = 0

        self.player = Player()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

        self.slashes = arcade.SpriteList()
        self.slash_timer = 0

        self.bullets = arcade.SpriteList()
        self.bullet_timer = 0
        self.bullet_frequency = BULLET_FREQUENCY

        self.audio = arcade.load_sound(f'assets/songs/wav/{TRACK_LIST[self.song]}.wav')
        self.duration = get_wav_duration(f'assets/songs/wav/{TRACK_LIST[self.song]}.wav') + 1
        self.playing = False

        self.timer_text = arcade.Text("0.00", 0, 0, font_size=20, font_name="Bahnschrift",
                                      color=tuple(map(lambda x: 255 - x, BACKGROUND_COLOR[:-1])))
        self.timer_text.x = SCREEN_WIDTH // 2 - self.timer_text.content_size[0] // 2
        self.timer_text.y = SCREEN_HEIGHT - self.timer_text.content_size[1]
        self.health_text = arcade.Text(f'Health: {self.player.health}', 10, 0, font_size=20, font_name="Bahnschrift",
                                       color=tuple(map(lambda x: 255 - x, BACKGROUND_COLOR[:-1])))
        self.health_text.y = SCREEN_HEIGHT - self.health_text.content_size[1]
        self.count_text = arcade.Text(f'Count: {self.count}', 0, 0, font_size=20, font_name="Bahnschrift",
                                      color=tuple(map(lambda x: 255 - x, BACKGROUND_COLOR[:-1])))
        self.count_text.x = SCREEN_WIDTH - self.count_text.content_size[0] - 10
        self.count_text.y = SCREEN_HEIGHT - self.count_text.content_size[1]

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture,
                                 arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player_list.draw()
        self.slashes.draw()
        self.bullets.draw()
        self.timer_text.draw()
        self.health_text.draw()
        self.count_text.draw()

    def on_update(self, delta_time):
        self.timer += delta_time
        self.timer_text.text = f'{self.timer:.2f}'
        self.timer_text.x = SCREEN_WIDTH // 2 - self.timer_text.content_size[0] // 2

        if arcade.key.A in self.pressed:
            self.player.speed_x = -self.player.speed
        if arcade.key.D in self.pressed:
            self.player.speed_x = self.player.speed
        if arcade.key.S in self.pressed:
            self.player.speed_y = -self.player.speed
        if arcade.key.W in self.pressed:
            self.player.speed_y = self.player.speed

        if self.timer >= 5 and not self.playing:
            self.audio_playback = arcade.play_sound(self.audio)
            self.playing = True
        elif self.playing:
            self.slash_timer += delta_time
            self.bullet_timer += delta_time

            if self.playing and self.beats and self.slash_timer >= self.beats[0]:
                self.slashes.append(Slash())
                self.count += SLASH_COUNT
                del self.beats[0]

            if self.playing and self.bullet_timer >= self.bullet_frequency:
                self.bullets.append(Bullet((self.player.center_x, self.player.center_y)))
                self.count += BULLET_COUNT
                self.bullet_timer = 0

            self.count_text.text = f'Count: {self.count}'
            self.count_text.x = SCREEN_WIDTH - self.count_text.content_size[0] - 10
            self.bullet_frequency /= BULLET_FREQUENCY_ACCEL

            if arcade.check_for_collision_with_list(self.player, self.slashes):
                for slash in range(len(self.slashes)):
                    if self.slashes[slash].damage_state and SLASH_DAMAGE_TIME[0] < self.slashes[slash].timer < \
                            SLASH_DAMAGE_TIME[1]:
                        if arcade.check_for_collision(self.player, self.slashes[slash]):
                            self.slashes[slash].damage_state = False
                            self.player.health -= SLASH_DAMAGE
                            self.health_text.text = f'Health: {self.player.health}'
                            break

            if arcade.check_for_collision_with_list(self.player, self.bullets):
                for bullet in range(len(self.bullets)):
                    if arcade.check_for_collision(self.player, self.bullets[bullet]):
                        self.bullets[bullet].remove_from_sprite_lists()
                        self.player.health -= BULLET_DAMAGE
                        self.health_text.text = f'Health: {self.player.health}'
                        break

            if self.player.health <= 0 or self.timer > self.duration:
                self.audio_playback.pause()
                end_view = EndScreenView(self.menu_view, self.count)
                self.window.show_view(end_view)

            self.slashes.update()
            self.bullets.update()

        self.player_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.audio_playback.pause()
            pause_view = PauseView(self)
            self.window.show_view(pause_view)
        else:
            self.pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.pressed.remove(key)
        if key == arcade.key.W or key == arcade.key.S:
            self.player_list[0].speed_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_list[0].speed_x = 0
