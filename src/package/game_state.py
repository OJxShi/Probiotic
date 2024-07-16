import pygame
from pygame.locals import *
from config import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

class GameState():
    def __init__(self):
        self.next_state = None
        
    def enter(self):
        self.next_state = None
                
    def event_handle(self,event):
        pass
        
    def update(self):
        pass
        
    def draw(self):
        pass
        
    def exit(self):
        active_keys.clear()

active_keys = set()