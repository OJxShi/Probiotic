import pygame, math
from config import *
from camera_script import *

class Collider:
    def __init__(self,point_1,point_2):
        self.line = (point_1,point_2)
        self.normal = self.get_normal()
    
    def collide(self,rect: pygame.Rect):
        if rect.clipline(self.line):
            return self.normal
    
    def get_normal(self):
        x1,y1 = self.line[0]
        x2,y2 = self.line[1]
        angle = math.atan2((y2-y1),(x2-x1))
        return angle

    def reverse_normals(self):
        self.line = (self.line[1],self.line[0])
        self.normal = self.get_normal()

    def draw(self):
        point_1 = (self.line[0][0]-camera.x,self.line[0][1]-camera.y)
        point_2 = (self.line[1][0]-camera.x,self.line[1][1]-camera.y)
        pygame.draw.line(screen,(0,0,0),point_1,point_2)
        pygame.draw.circle(screen,(0,0,0),point_1,5,2)
        pygame.draw.circle(screen,(0,0,0),point_2,5,2)


class ColliderGroup:
    def __init__(self):
        self.lines = []
    
    def collide(self,rect):
        for line in self.lines:
            normal = line.collide(rect)
            if normal:
                return normal