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
hoop=pygame.image.load("hoop.jpg")
durant=pygame.image.load("durant.jpg")
lebron=pygame.image.load ("lebron.jpg")

game_background_sound = pygame.mixer.Sound("dribble.wav")
blocked = pygame.mixer.Sound("blocked.wav")
swoosh = pygame.mixer.Sound("swoosh.wav")

swoosh.set_volume(10.6)
game_background_sound.set_volume(0.8)
game_background_sound.play(loops=-1)

alive = True
jumping = False
backDown = False
x = 0
y = 5
score=0
lebronx= 4
lebrony= 5

durantx= 6
duranty= 5
while (alive == True):
    screen.blit(background, (0,0))
    screen.blit (hoop, convert_to_screen_space(7,3))
    if jumping == True:
        screen.blit(kobejumping, convert_to_screen_space(x,y))
    else:
        screen.blit(kevin, convert_to_screen_space(x,y))

    screen.blit(durant,convert_to_screen_space(durantx,duranty))
    screen.blit(lebron,convert_to_screen_space(lebronx,lebrony))
    if (x==7) and (y==3) :
       score = score+1
       swoosh.play()
       x=0
       y=5
       jumping = False
       backDown = False

    if ((x==durantx) and (y==duranty)) or ((x==lebronx) and (y==lebrony)):
       x=0
       y=5
       jumping = False
       backDown = False
       score = score - 1
       blocked.play()

    duranty=duranty-0.5
    if duranty== 0:
       duranty=5
  
    b = pygame.Surface((100, 100))
    b = b.convert()
    b.fill((200, 200, 200))
           
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render(str(score), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = 50
    b.blit(text, textpos)
    screen.blit(b, (0, 0))

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
