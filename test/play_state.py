import pygame
from package.game_state import GameState
from package.collision_script import Collider,ColliderPolygon
from package.character_script import Player

player = Player()

class PlayState(GameState):
    def __init__(self):
        GameState.__init__(self)
        self.room = [
            ColliderPolygon([(0,300),(400,400),(400,600),(800,600),(800,0),(0,0)])
        ]
        player.set_pos(200,200)
    
    def event_handle(self,event):
        GameState.event_handle(self,event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.set_pos(event.pos[0],event.pos[1])
        
    
    def update(self):
        player.input(self.active_keys)
        for wall in self.room:
            player.collide(wall)
        player.update()

    def draw(self,screen):
        screen.fill((255,255,255))
        for wall in self.room:
            wall.draw(screen)
        player.draw(screen)