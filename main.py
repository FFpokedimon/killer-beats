import arcade

from constants import *
from views.menu_view import MenuView

if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Killer Beats")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
