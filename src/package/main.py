import pygame
from config import *
from collision_script import *
from game_state import GameState

def main():
    running = True
    current_state = GameState()
    while running:
        for event in pygame.event.get():
            current_state.event_handle(event)
            if event.type == pygame.QUIT:
                running = False
        
        current_state.update()

        screen.fill((255,255,255))
        current_state.draw()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()