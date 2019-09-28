import pygame, sys

from pygame.locals import *

class Start(object):
	
    def __init__(self):
        # Constants
        WINDOWWIDTH = 448 #(16 * 28) (row numbers range from 0 - 27)
        WINDOWHEIGHT = 512 #(16 * 32) (column numbers range from 0 - 31)

        # Colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        # Initialize window
        window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        window.fill(BLACK)
        
        # Initialize font
        font = pygame.font.Font("../font/minecraft.ttf", 36)

        # Create Title
        pacman_title = pygame.image.load("../sprites/pyman_title.png")
        pacman_title_rect = pacman_title.get_rect()
        pacman_title_rect.centerx = WINDOWWIDTH/2
        pacman_title_rect.centery = 128

        # Create Start Button
        start = pygame.Surface((192, 48))
        start_rect = start.get_rect()
        start_rect.centerx = WINDOWWIDTH/2
        start_rect.centery = 320

        # Create Exit Button
        quit = pygame.Surface((96, 48))
        quit_rect = quit.get_rect()
        quit_rect.centerx = WINDOWWIDTH/2
        quit_rect.centery = 408

        window.blit(pacman_title, pacman_title_rect)
        
        # Create Start Text
        start_text = font.render("START", True, GREEN)
        start_text_rect = start_text.get_rect()
        start_text_rect.centerx = start_rect.centerx
        start_text_rect.centery = start_rect.centery
        
        # Create Quit Text
        quit_text = font.render("QUIT", True, RED)
        quit_text_rect = quit_text.get_rect()
        quit_text_rect.centerx = quit_rect.centerx
        quit_text_rect.centery = quit_rect.centery
        
        window.blit(start_text, start_text_rect)
        window.blit(quit_text, quit_text_rect)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if quit_rect.collidepoint(x, y):
                        pygame.quit()
                        sys.exit()
                    elif start_rect.collidepoint(x, y):
                        return