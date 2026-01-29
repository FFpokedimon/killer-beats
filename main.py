import arcade

from constants import *
from views.game_view import GameView
if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Killer Beats")
    game_view = GameView(2)
    game_view.setup()
    window.show_view(game_view)
    arcade.run()
