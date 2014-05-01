import pygame
import time
import random
from pygame.locals import *

time_that_monster_moved = 0.0

def draw_game_board(your_position, monster_position):
    screen.blit(background, (0,0))
    screen.blit(hero, (your_position[0]*100, your_position[1]*100))
    
    if monster_alive == True:
        screen.blit(monster, (monster_position[0]*100, monster_position[1]*100))
    if bullet_moving == True:
        screen.blit(bullet, (bullet_position[0]*100, bullet_position[1]*100))
    pygame.display.flip()

def accept_player_input():
    global your_position
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                shoot()
            elif event.key == K_UP:
                your_position[1] -= 1
            elif event.key == K_DOWN:
                your_position[1] += 1

def shoot():
    global your_position
    global monster_position
    global monster_alive
    global bullet_moving
    global bullet_position
    if your_position[1] == monster_position[1]:
        bullet_position[0]=your_position[0]
        bullet_position[1] = your_position [1]
        bullet_moving = True


def move():
    global time_that_monster_moved
    global monster_alive
    global bullet_moving
    current_time = pygame.time.get_ticks()
    if monster_alive and (current_time-time_that_monster_moved) > speed:
        monster_position[0] = monster_position[0] - 1
        check()
        time_that_monster_moved = current_time
        bullet_position[0] = bullet_position[0] + 1
        check()

def check():
    global monster
    global score, hero, speed
    global monster_alive
    global bullet_moving
    global game_background_sound
    global bullet, background
    if bullet_position == monster_position:
      monster_alive = False
      bullet_moving = False
      score = score +1
      if score == 20:
        speed=400
        hero = pygame.image.load("dark harry.png")
        monster = pygame.image.load("stash.png")
        game_background_sound.stop()
        game_background_sound = pygame.mixer.Sound("dark-harry.wav")
        game_background_sound.play(loops=-1)
        bullet = pygame.image.load("dark orb.png")
        background = pygame.image.load("cave.png")
      if score == 35:
        speed=350
        hero = pygame.image.load("red.png")
        monster = pygame.image.load("mewthree")
        game_background_sound.stop()
        game_background_sound = pygame.mixer.Sound("pokemon.wav")
        game_background_sound.play(loops=-1)
        bullet = pygame.image.load("pokeball.png")
        background = pygame.image.load("pokebattle.png")
      if score == 50:
        speed = 200
        hero = pygame.image.load("powerful harry.png")
        monster = pygame.image.load("hydra.png")
        game_background_sound.stop()
        game_background_sound = pygame.mixer.Sound('final-battle.wav')
        game_background_sound.play(loops=-1)
        bullet = pygame.image.load("ultra blast.png")
        background = pygame.image.load("space.png")
      print score
      respawn()


def respawn():
    global monster_alive
    global monster_position
    monster_alive=True
    monster_position[0]=4
    monster_position[1]=random.randint(0,4)

score = 0
speed = 500
my_p0 = 0
my_p1 = 0

bad_p0 = 4
bad_p1 = 4
your_position = [int(my_p0), int(my_p1)]
bullet_position = [int(my_p0), int(my_p1)]
monster_position = [int(bad_p0), int(bad_p1)]

monster_alive = True
bullet_moving = False

pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.image.load("brick.png")

monster = pygame.image.load("monster.gif")
hero = pygame.image.load("noob harry.png")
bullet = pygame.image.load("magic.png")


game_background_sound = pygame.mixer.Sound("boss-select.wav")
game_background_sound.set_volume(0.2)
game_background_sound.play(loops=-1)

while not monster_position[0] == 0:
    draw_game_board(your_position, monster_position)
    move()
    accept_player_input()

