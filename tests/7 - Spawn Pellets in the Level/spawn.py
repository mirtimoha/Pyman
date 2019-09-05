import os, sys, pygame

from pygame.locals import *

# initialize pygame
pygame.init()
mainClock = pygame.time.Clock()

# constants
WINDOWWIDTH = 448 #(16 * 28) (row numbers range from 0 - 27)
WINDOWHEIGHT = 512 #(16 * 32) (column numbers range from 0 - 31)

# 

# colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# initialize window
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

# set background
background = pygame.image.load('../../sprites/pacman-level.png')
windowSurface.blit(background, (0, 0))

# goes through the entire map and outlines which 16x16 areas are black
# and which ones are not
# this identifies where Pacman and Pellets can and cannot spawn
x = 0
y = 0
while y < WINDOWHEIGHT:
    while x < WINDOWWIDTH:
        selected_area = pygame.Rect(x, y, 16, 16)
        cropped_image = background.subsurface(selected_area)
        if pygame.transform.average_color(cropped_image)[:3] == BLACK:
            pygame.draw.rect(windowSurface, GREEN, selected_area)
        else:
            pygame.draw.rect(windowSurface, RED, selected_area)
            
        x += 16
    y += 16
    x = 0
    
            
# update display
pygame.display.update()
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()