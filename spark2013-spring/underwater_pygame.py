import pygame
from pygame.locals import *

monster = pygame.image.load("monster.png")

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Underwater World!")
    clock = pygame.time.Clock()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((200, 200, 0))

    while 1:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.blit(background, (0, 0))
        screen.blit(monster, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
