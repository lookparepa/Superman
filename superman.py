import arcade

from models import World, Man

import pyglet.gl as gl

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

class ModelSprite(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class SupermanGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.man_sprite = ModelSprite('images/superman.png', model = self.world.man)
        self.kryptonite_sprite = ModelSprite('images/kryptonite.png', model = self.world.kryptonite)
    
    def animate(self, delta):
        self.world.animate(delta)

    def on_draw(self):

        arcade.set_viewport(self.world.man.x - SCREEN_WIDTH/2, self.world.man.x + SCREEN_WIDTH/2, 0, SCREEN_HEIGHT)

        arcade.start_render()
        
        self.man_sprite.draw()
        self.kryptonite_sprite.draw()

        gl.glDisable(gl.GL_TEXTURE_2D)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = SupermanGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
