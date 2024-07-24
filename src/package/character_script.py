import pygame,math
from animated_sprites_script import AnimatedSprite 

class Character(AnimatedSprite):
    def __init__(self,x:float,y:float,w:int,h:int):
        AnimatedSprite.__init__(self)
        self.x = x
        self.y = y
        self.velo_x = 0
        self.velo_y = 0
        self.hitbox = (0,0,w,h)

        self.mass = 50
        self.gravity = 9.8

    def collide(self,collision_list:list):
        self.x += self.velo_x
        self.y += self.velo_y
        for collider in collision_list:
            normal = collider.collide(self.hitbox)
            if normal:
                x = self.mass*self.gravity*math.cos(normal)
                y = self.mass*self.gravity*math.sin(normal)
                self.velo_x += x
                self.velo_y += y
        
        self.y += self.gravity
    
    def set_gravity(self,gravity):
        self.gravity = gravity
    
    def set_mass(self,mass):
        self.mass = mass