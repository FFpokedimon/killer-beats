import arcade
from constants import *
from views.game_view import GameView
from music_analysis import get_drum_timestamps


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.title_text = arcade.Text("KILLER BEATS", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                                      arcade.color.WHITE, font_size=50, font_name="Bahnschrift", anchor_x="center")
        self.instructions_text = arcade.Text("Нажмите 1-5 для выбора трека", SCREEN_WIDTH / 2,
                                             SCREEN_HEIGHT / 2,
                                             arcade.color.WHITE, font_size=25, font_name="Bahnschrift",
                                             anchor_x="center")
        self.quit_text = arcade.Text("ESC для выхода", SCREEN_WIDTH / 2,
                                     SCREEN_HEIGHT / 2 - 50,
                                     arcade.color.GRAY, font_size=15, font_name="Bahnschrift", anchor_x="center")

    def on_draw(self):
        self.clear()
        self.title_text.draw()
        self.instructions_text.draw()
        self.quit_text.draw()

    def on_key_press(self, key, modifiers):
        if key in [arcade.key.KEY_1, arcade.key.NUM_1]:
            beats = get_drum_timestamps(TRACK_LIST[0])
            game_view = GameView(0, beats, self)
            game_view.setup()
            self.window.show_view(game_view)
        elif key in [arcade.key.KEY_2, arcade.key.NUM_2]:
            beats = get_drum_timestamps(TRACK_LIST[1])
            game_view = GameView(1, beats, self)
            game_view.setup()
            self.window.show_view(game_view)
        elif key in [arcade.key.KEY_3, arcade.key.NUM_3]:
            beats = get_drum_timestamps(TRACK_LIST[2])
            game_view = GameView(2, beats, self)
            game_view.setup()
            self.window.show_view(game_view)
        elif key in [arcade.key.KEY_4, arcade.key.NUM_4]:
            beats = get_drum_timestamps(TRACK_LIST[3])
            game_view = GameView(3, beats, self)
            game_view.setup()
            self.window.show_view(game_view)
        elif key in [arcade.key.KEY_5, arcade.key.NUM_5]:
            beats = get_drum_timestamps(TRACK_LIST[4])
            game_view = GameView(4, beats, self)
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.ESCAPE:
            arcade.close_window()
