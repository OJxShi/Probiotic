import pygame,math
from .animated_sprites_script import AnimatedSprite 

class Character(AnimatedSprite):
    def __init__(self,x:float=0,y:float=0,w:int=100,h:int=100):
        AnimatedSprite.__init__(self)
        self.x = x
        self.y = y
        self.velo_x = 0
        self.velo_y = 0
        self.hitbox = pygame.Rect(0,0,w,h)

        self.mass = 50
        self.gravity = 9.8
    
    def set_pos(self,x,y):
        self.x = x
        self.y = y
        self.align()
    
    def set_gravity(self,gravity):
        self.gravity = gravity
    
    def set_mass(self,mass):
        self.mass = mass
    
    def align(self):
        AnimatedSprite.align(self)
        self.hitbox.center = self.x, self.y

    def collide(self,collider):
        self.velo_y += self.gravity
        self.x += self.velo_x
        self.y += self.velo_y
        self.align()
        
        offset = collider.collide(self.hitbox)
        if offset:
            self.x += offset[0]
            self.y += offset[1]
            #more advanced movement + friction coming... soon
            self.velo_x = 0
            self.velo_y = 0
        self.align()
    
    def update(self):
        AnimatedSprite.update(self)


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.actions = {
            pygame.K_LEFT:"walk_left",
            pygame.K_RIGHT:"walk_right",
            pygame.K_UP:"jump"
        } # To be implemented: easy way to add actions and bind to different keys...
    
    def input(self,input):        
        if pygame.K_LEFT in input:
            self.x -= 10
        if pygame.K_RIGHT in input:
            self.x += 10
        if pygame.K_UP in input:
            self.velo_y = -15