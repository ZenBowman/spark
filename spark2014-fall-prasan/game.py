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
background = pygame.image.load("court.jpg")
kevin = pygame.image.load("kobe.jpg")
kobejumping = pygame.image.load("kobejumping.jpg")
zombie = pygame.image.load("zombie.gif")
gameover = pygame.image.load("gameOver.jpg")

alive = True
jumping = False
backDown = False
x = 0
y = 5

while (alive == True):
    screen.blit(background, (0,0))

    if jumping == True:
        screen.blit(kobejumping, convert_to_screen_space(x,y))
    else:
        screen.blit(kevin, convert_to_screen_space(x,y))
    
    
    pygame.display.flip()
    time.sleep(0.1)


    if backDown == True:
        y = y + 1
        if y == 5:
            backDown = False

    if jumping == True:
        y = y-1
        if y == 3:
            jumping = False
            backDown = True


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x > 0:
                    x = x - 1
            elif event.key == K_RIGHT:
                if x < 7:
                    x = x + 1
            elif event.key == K_UP:
                if y == 5:
                    y = y -1 
                    jumping = True
            elif event.key == K_BACKSPACE:
                alive = False
