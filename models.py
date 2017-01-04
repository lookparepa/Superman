import arcade.key
from random import randint, random

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
    
    def __init__(self, world, x, y, vx, vy):
        super().__init__(world, x, y, 0)
        self.vx = vx
        self.vy = vy
        self.angle = randint(0,359)
    
    def random_direction(self):
        self.vx = 5 * random()
        self.vy = 5 * random()

    def animate(self, delta):
        self.x += self.vx
        self.y += self.vy
        self.angle += 1

        

class World:
    NUM_KRYP = 8

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.man = Man(self, 0 , 300 , 0)

        # self.kryptonite = Kryptonite(self, 400, 400)
        self.kryptonite_list = []
        for i in range(World.NUM_KRYP):
            kryptonite = Kryptonite(self, 0, 0, 0, 0)
            kryptonite.random_direction()
            self.kryptonite_list.append(kryptonite)
        

    def animate(self, delta):
        self.man.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.man.jump()