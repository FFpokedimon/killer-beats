import arcade
from constants import *


class EndScreenView(arcade.View):
    def __init__(self, menu_view, count):
        super().__init__()
        self.background_color = (139, 0, 0)
        self.menu_view = menu_view
        self.message_text = arcade.Text(f'Счет: {count}', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                                        arcade.color.WHITE, font_size=40, font_name="Bahnschrift", anchor_x="center")
        self.return_text = arcade.Text("Нажмите R для возврата в меню", SCREEN_WIDTH / 2,
                                       SCREEN_HEIGHT / 2 - 20,
                                       arcade.color.LIGHT_GRAY, font_size=20, font_name="Bahnschrift",
                                       anchor_x="center")
        self.quit_text = arcade.Text("ESC для выхода", SCREEN_WIDTH / 2,
                                     SCREEN_HEIGHT / 2 - 60,
                                     arcade.color.GRAY, font_size=15, font_name="Bahnschrift", anchor_x="center")

    def on_draw(self):
        self.clear()
        self.message_text.draw()
        self.return_text.draw()
        self.quit_text.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.window.show_view(self.menu_view)
        elif key == arcade.key.ESCAPE:
            arcade.close_window()
