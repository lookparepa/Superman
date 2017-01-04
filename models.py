import arcade.key
from random import randint

GRAVITY = -2
MAX_VX = 3
ACCX = 1
JUMP_VY = 25

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class Man(Model):
    def __init__(self, world, x, y, base_y):
        super().__init__(world, x, y, 0)
        self.vx = 0
        self.vy = 0

        self.is_jump = False

        self.base_y = base_y

    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.vy = JUMP_VY
            self.count = 0
            
    def animate(self, delta):
        if self.vx < MAX_VX:
            self.vx += ACCX
        
        self.x += self.vx
        self.y += -5

        if self.is_jump:
            self.y += self.vy
            self.vy = self.vy + GRAVITY
            self.count += 1

            if self.count == 15:
                self.vy = 0
                self.is_jump = False
            
class Kryptonite(Model):
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y 
        

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.man = Man(self, 0 , 300 , 0)

        self.kryptonite = Kryptonite(self, 400, 400)
        

    def animate(self, delta):
        self.man.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.man.jump()