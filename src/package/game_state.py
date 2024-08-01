import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

class GameState():
    def __init__(self):
        self.next_state = None
        self.active_keys = set(())
        
    def enter(self):
        self.next_state = None
                
    def event_handle(self,event):
        if event.type == pygame.KEYDOWN:
            self.active_keys.add(event.key)
        elif event.type == pygame.KEYUP:
            self.active_keys.remove(event.key)
        
    def update(self):
        pass
        
    def draw(self,screen:pygame.Surface):
        pass

    def change_state(self,next_state):
        self.next_state = next_state
    
    def get_next_state(self):
        if self.next_state == None:
            return self
        else:
            return self.next_state

    def exit(self):
        active_keys.clear()

active_keys = set()