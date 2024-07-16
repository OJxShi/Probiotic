import pygame, json

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE,pygame.RESIZABLE)
screen.set_clip(pygame.Rect(0,0,WIDTH,HEIGHT))
pygame.display.set_caption("Gamig")
clock = pygame.time.Clock()

world_gravity = 9.8

def resize_screen(new_width,new_height):
    global screen
    screen = pygame.display.set_mode((new_width,new_height),pygame.RESIZABLE)
    