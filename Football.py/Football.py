# Michael Goodman
# Football Ravens for life 
# Not sure yet though 

import pygame 
#import sys 

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True 
while running: 
      screen.fill((0,0,0))

      for event in pygame.event.get():
            if event.type == pygame.event.QUIT:
                  running = False
