import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'Drawing'


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.GOLD)

        self.background = None

    def setup(self):
        self.background = arcade.load_texture("sprite.jpeg")

    def on_draw(self):
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        arcade.draw_point(60, 500, arcade.color.BLUE, 10)

        arcade.draw_line(0, 300, 800, 300, arcade.color.BLUE, 4)

        arcade.draw_text('Chill time', 400, 200, arcade.color.RED_DEVIL, 10)



def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()
