import arcade

from constants import *


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.game_view = game_view
        self.pause_text = arcade.Text("Пауза", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                      arcade.color.WHITE, font_size=40, font_name="Bahnschrift", anchor_x="center")
        self.space_text = arcade.Text("SPACE, чтобы продолжить", SCREEN_WIDTH / 2,
                                      SCREEN_HEIGHT / 2 - 50,
                                      arcade.color.WHITE, font_size=20, font_name="Bahnschrift", anchor_x="center")

    def on_draw(self):
        self.clear()
        self.pause_text.draw()
        self.space_text.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.game_view.audio_playback.play()
            self.window.show_view(self.game_view)
