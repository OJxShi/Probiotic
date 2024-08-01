import os
import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

demo_directory = os.path.dirname(os.path.abspath(__file__))
root_directory = os.path.dirname(demo_directory)
source_directory = os.path.join(root_directory, "src")
sys.path.insert(0, source_directory)

from play_state import PlayState

def main():
    current_state = PlayState()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            current_state.event_handle(event)
        
        current_state.update()

        screen.fill((0, 0, 0))
        current_state.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()