#Physics engine

import pygame
import math


pygame.init()  #Starting Pygame
w,h = 1000, 700  #Getting width height

screen = pygame.display.set_mode((w,h)) #Main widnows called screen, width,height is w,h
screen.fill('White')
running = True

#Variable for physics

grav = -3.5
initial_vel = 40
angle = 45
time = 0
x_pos, w_pos = w*.2, h*0.8

circle = pygame.draw.circle(screen, "Blue", (w/2, h/0.8), 20)


#Pygame Loop

while running:
  time +=0.5
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.draw.circle(screen, "Blue", (x_pos, w_pos), 20)
  x_pos = 2*time
  print(x_pos)

  


  pygame.display.flip()
