import pygame
from pygame.locals import *

class Camera():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_focus = 0
        self.y_focus = 0
        self.speed = 1
        
    def focus(self,x,y,speed=1,strx=1,stry=1):
        self.x_focus = x*strx
        self.y_focus = y*stry
        self.speed = speed
    
    def go_to(self,x,y):
        self.x = x
        self.y = y
        self.x_focus = x
        self.y_focus = y
        
    def update(self):
        self.x += (self.x_focus - self.x) * self.speed
        self.y += (self.y_focus - self.y) * self.speed

camera = Camera()