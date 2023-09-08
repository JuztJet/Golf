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
angle = 65
fired = True

v_velocity = initial_vel*math.sin(math.radians(angle))
h_velocity = initial_vel*math.cos(math.radians(angle))

time = 0

x_pos, y_pos = w*.2, h*0.8

vertical_displacement = 0
horizontal_displacement = 0

horizontal_resistance = 0.2
vertical_resistance = 0.2


#Pygame Loop

while running:
  #Event Loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #Time increase
  time +=0.5

  

  #Changing x_pos and y_pos
   
  horizontal_displacement = h_velocity*time
  vertical_displacement = -1 *((v_velocity*time) + ((grav*(time**2))/2))
  # horizontal_resistance = horizontal_displacement*0.3
  # vertical_resistance = vertical_displacement*0.3

  x_pos = horizontal_displacement - horizontal_resistance
  y_pos = vertical_displacement + 500 - horizontal_resistance
  
  if y_pos >= 500:
    y_pos = 500
  print(y_pos)
  #Draw circle
  pygame.draw.circle(screen, "Blue", (x_pos, y_pos), 20)
  fired = False

  


  pygame.display.flip()


