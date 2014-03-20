import pygame
import time
import random
import time
from pygame.locals import *

def convert_to_screen_space(x, y):
    new_x = x * 100
    new_y = y * 100
    return new_x, new_y

pygame.init()
screen = pygame.display.set_mode((600,300))
background = pygame.image.load("grid.png")
kevin = pygame.image.load("kevin.jpg")

x = 0
y = 0

while 1:
    screen.blit(background, (0,0))
    screen.blit(kevin, convert_to_screen_space(x,y))
    pygame.display.flip()
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x > 0:
                    x = x - 1
            elif event.key == K_RIGHT:
                if x < 5:
                    x = x + 1
            elif event.key == K_DOWN:
                if y < 2:
                    y = y + 1
            elif event.key == K_UP:
                if y > 0:
                    y = y -1 
