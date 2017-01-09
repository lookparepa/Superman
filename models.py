import arcade.key
from random import randint, random

GRAVITY = -1
MAX_VX = 3
ACCX = 2
JUMP_VY = 15


class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class Superman(Model):
    def __init__(self, world, x, y, ground_y):
        super().__init__(world, x, y, 0)
        self.vx = 0
        self.vy = 0
        
        self.is_jump = False
        self.is_collide_with_kryptonite =False
        self.ground_y = ground_y

    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.vy = JUMP_VY
            self.count = 0
    
    def collide_with_kryptonite(self):
        kryptonites = self.world.kryptonites
        for k in kryptonites:
            if self.x >=  k.x and self.x <= k.x+k.width:
                if self.y >= k.y-k.height and self.y <= k.y:
                    self.is_collide_with_kryptonite = True
            
    def animate(self, delta):
        if self.vx < MAX_VX:
            self.vx += ACCX
        
        self.collide_with_kryptonite()
        
        if self.is_collide_with_kryptonite == True:
            self.y -= 10
        
        self.x += self.vx
        self.y += -1

        if self.is_jump:
            self.y += self.vy
            self.vy = self.vy + GRAVITY
            self.count += 1

            if self.count == 15:
                self.vy = 0
                self.is_jump = False

class Kryptonites:
    def __init__(self, world, x, y, width, height):
        self.world = world
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0
        self.superman = Superman(self, 0, 500 , 0)
        self.kryptonites = []
        init = 150

        for i in range(1,250):
            self.kryptonites.append(Kryptonites(self, init, 700, 200, 50))
            self.kryptonites.append(Kryptonites(self, init, randint(250,500), 150,600))
            init += 150
		
        self.kryptonites.append(Kryptonites(self, 15150, 900, 50, 10000))
        self.kryptonites.append(Kryptonites(self, 15150, 600, 50, 400))

    def animate(self, delta):
        self.superman.animate(delta)
        if self.superman.x %49 == 0:
            if not self.superman.is_collide_with_kryptonite:
                self.score += 1

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.superman.jump()