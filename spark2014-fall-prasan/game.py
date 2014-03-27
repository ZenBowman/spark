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
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("grid.png")
kevin = pygame.image.load("kevin.jpg")
zombie = pygame.image.load("zombie.gif")
gameover = pygame.image.load("gameOver.jpg")

alive = True
x = 0
y = 0

zombieX = 0
zombieY = 5

while (alive == True):
    screen.blit(background, (0,0))
    screen.blit(background, (600,0))
    screen.blit(background, (0, 300))
    screen.blit(background, (600, 300))

    screen.blit(kevin, convert_to_screen_space(x,y))
    screen.blit(zombie, convert_to_screen_space(zombieX, zombieY))

    # this is where we check if the zombie and kevin are in the same
    # place
    if (x == zombieX) and (y == zombieY):
        screen.blit(gameover, (0,0))
        alive = False
        pygame.display.flip()
        time.sleep(3.0)

    pygame.display.flip()
    time.sleep(1.0)
    
    if y > zombieY:
        zombieY += 1
    elif y < zombieY:
        zombieY -= 1
    if x > zombieX:
        zombieX += 1
    elif x < zombieX:
        zombieX -= 1

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x > 0:
                    x = x - 1
            elif event.key == K_RIGHT:
                if x < 7:
                    x = x + 1
            elif event.key == K_DOWN:
                if y < 5:
                    y = y + 1
            elif event.key == K_UP:
                if y > 0:
                    y = y -1 
