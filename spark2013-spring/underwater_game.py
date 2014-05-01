import random
import sys 
import pygame
from pygame.locals import *

player_position = (3,3)
game_monster = (0,0)
game_difficulty = 9
game_treasure = (random.randint(6,game_difficulty), random.randint(6,game_difficulty))
game_monster_2 = (9,9)
power_up_teleporter = ((random.randint(0,game_difficulty), random.randint(0,game_difficulty)),
                       (random.randint(0,game_difficulty), random.randint(0,game_difficulty)))

game_pits = [
    (random.randint(0, game_difficulty), random.randint(0,game_difficulty)),
    (random.randint(0, game_difficulty), random.randint(0,game_difficulty)),
    (random.randint(0, game_difficulty), random.randint(0,game_difficulty)),
    (random.randint(0, game_difficulty), random.randint(0,game_difficulty)),
    (random.randint(0, game_difficulty), random.randint(0,game_difficulty))
]

def to_physical(position):
    return (position[0] * 50, position[1] * 50)

def draw(position):
    global player_position
    global game_monster
    global game_treasure
    global game_monster_2
    global game_pits
    global power_up_teleporter 
    if position == player_position:
        screen.blit(hero, to_physical(position))
    elif (position == game_monster) or (position == game_monster_2):
        screen.blit(monster, to_physical(position))
    elif (position == game_treasure):
        screen.blit(treasure_image, to_physical(position))
    elif (position in game_pits):
        screen.blit(cave_image, to_physical(position))
    elif (position == power_up_teleporter[0]):
        screen.blit(teleporter_entrance_image, to_physical(position))
    elif (position == power_up_teleporter[1]):    
        screen.blit(teleporter_exit_image, to_physical(position))
    


def check():
    global player_position
    global game_monster
    global game_treasure
    global game_monster_2
    global game_pits
    if player_position == power_up_teleporter[0]:
        player_position = power_up_teleporter[1]
        teleport_sound.play()
    elif player_position == power_up_teleporter[1]:
        player_position = power_up_teleporter[0]
        teleport_sound.play()
    elif (player_position == game_monster) or (player_position == game_monster_2):
        game_over_sound.play()
        return "game over"
    
    elif player_position == game_treasure:
        game_win_sound.play()
        return "game win"
    elif player_position in game_pits:
        falling_down.play()
        return "game over"
    
    return "running"

def clamp(position): 
    if position[0] < 0:
        position = (0, position[1]) 
    elif position[0] > game_difficulty:
        position = (game_difficulty, position[1])
    if position[1] > game_difficulty:
        position = (position[0], game_difficulty)
    elif position[1] < 0:
        position = (position[0], 0)
    return position


def monster_move(monster_position):
    if monster_position[0] < player_position[0]:
        new_monster_position = (monster_position[0] + 1, monster_position[1])
    elif monster_position[0] > player_position[0]:
        new_monster_position = (monster_position[0] - 1, monster_position[1])
    elif monster_position[1] < player_position[1]:
        new_monster_position = (monster_position[0], monster_position[1] + 1)
    elif monster_position > player_position[1]:
        new_monster_position = (monster_position[0], monster_position[1] - 1)

    if new_monster_position in game_pits:
        return monster_position
    else:
        return new_monster_position
     

def move(position, direction):
    if direction == "left":
        position = (position[0] - 1, position[1])
    elif direction == "right": 
        position = (position[0] + 1, position[1])
    elif direction == "up": 
        position = (position[0], position[1] - 1)
    elif direction == "down":
        position = (position[0], position[1] + 1)
    return position

def draw_game_board():
    screen.blit(background, (0, 0))
    screen.blit(background_image, (0,0))
        
    for j in range(game_difficulty+1):
        for i in range(game_difficulty+1): 
            position_to_check = (i, j)
            draw(position_to_check)
        

    if game_status == "game over":
        screen.blit(game_over_image, (100,100))
    if game_status == "game win":
        screen.blit(game_win_image, (100,100))

    pygame.display.flip()
    

def action_for(event):
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            return "left"
        elif event.key == K_RIGHT:
            return "right"
        elif event.key == K_UP:
            return "up"
        elif event.key == K_DOWN:
            return "down"

    return None
    

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Underwater World!")
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((200, 200, 0))

monster = pygame.image.load("monster.gif")
hero = pygame.image.load("hero.png")
treasure_image = pygame.image.load("game_treasure.png")
cave_image = pygame.image.load("cave.gif")
teleporter_entrance_image = pygame.image.load("teleporter_exit.jpg")
teleporter_exit_image = pygame.image.load("teleporter_entrance.jpg")
background_image = pygame.image.load("underwater_world.jpg")
game_over_image = pygame.image.load("game_over.png")
game_status = "running"
game_win_image = pygame.image.load("you_won.gif")
game_over_sound = pygame.mixer.Sound("no-mercy.wav")
game_win_sound = pygame.mixer.Sound("game-win.wav")
teleport_sound = pygame.mixer.Sound("teleport-sound.wav")
falling_down = pygame.mixer.Sound("fallin-down.wav")
game_background_sound = pygame.mixer.Sound("background-music.wav")

game_background_sound.set_volume(0.2)
game_background_sound.play(loops=-1)

while True:
    clock.tick(60)
    input = None
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        action = action_for(event)
        if action is not None:
            input = action
        
    draw_game_board()

    if game_status == "running":
        if input is not None:
            player_position = move(player_position, input)
            game_monster = monster_move(game_monster)
            player_position = clamp(player_position)
            game_monster = clamp(game_monster)
            game_monster_2 = monster_move(game_monster_2)
            game_monster_2 = clamp(game_monster_2)
            game_status = check()

pygame.mixer.quit()        
            

                        

