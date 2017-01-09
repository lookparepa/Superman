import arcade

from models import World, Superman 

import pyglet.gl as gl

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800

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
        self.superman_sprite = ModelSprite('images/superman.png', model = self.world.superman)

    def animate(self, delta):
        self.world.animate(delta)

    def draw_kryptonites(self):
        kryptonites = self.world.kryptonites
        for k in kryptonites:
            arcade.draw_rectangle_filled(k.x + k.width//2 , k.y - k.height//2,
							             k.width, k.height,
										 arcade.color.GREEN)
        
    def on_draw(self):

        arcade.set_viewport(self.world.superman.x - SCREEN_WIDTH//2 +200, 
                            self.world.superman.x + SCREEN_WIDTH//2 +200, 
                            0, SCREEN_HEIGHT)

        arcade.start_render()
        self.draw_kryptonites()
        self.superman_sprite.draw()
        
        if not self.world.superman.is_collide_with_kryptonite:
            arcade.draw_text("DISTANCE:"+str(self.world.score), self.world.superman.x + (SCREEN_WIDTH // 2), self.height -30, arcade.color.WHITE, 20)
            
        else:
            arcade.draw_text("HIGH SCORE : "+str(self.world.score), self.world.superman.x + (SCREEN_WIDTH // 2) -650, self.height -200, arcade.color.RED, 30)
            arcade.draw_text("MISSION FAIL", self.world.superman.x + (SCREEN_WIDTH // 2) -750, self.height -300, arcade.color.RED, 60)

        gl.glDisable(gl.GL_TEXTURE_2D)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = SupermanGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
