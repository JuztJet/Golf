#Physics engine

import pygame
import math


pygame.init()  #Starting Pygame
w,h = 350, 570  #Getting width height

screen = pygame.display.set_mode((w,h)) #Main widnows called screen, width,height is w,h
screen.fill('White')
running = True
line = False
clock = pygame.time.Clock()
#Variable for physics
mouse_pos = pygame.mouse.get_pos()




#v_velocity = initial_vel*math.sin(math.radians(angle))
#h_velocity = initial_vel*math.cos(math.radians(angle))

time = 0


air_resistance = 3

#angle = math.degrees(math.asin(1)*((y_pos-mouse_pos[0])/(x_pos-mouse_pos[1])))
#Pygame Loop
class Golf_Ball:
  def __init__(self, grav, x_pos, y_pos, colour, mass):
    self.grav = grav #-3.5
    self.initial_vel = 0
    self.resultant = 0
    self.fired = True
    self.hit_time=0
    self.held_down=False
    self.line = False
    self.boundary_pos = 0
    self.fired_resultant =0
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.colour = colour
    self.vertical_displacement = 0
    self.horizontal_displacement = 0
    self.rect = pygame.Rect((x_pos-10, y_pos-10), (20,20))
    self.mass = mass
  def mouse_click_manager(self):
    if pygame.mouse.get_pressed()[0] == True:
    
      if self.rect.collidepoint(mouse_pos):
      
        
        if self.line == False and self.held_down ==False:
          self.held_down = True
          self.line = True
      if self.line and self.held_down==False and self.resultant<=150:
          self.held_down = True
          self.line = False
          print("Hit")
          self.fired_resultant = self.resultant*0.023
          self.initial_vel = int(round((((self.fired_resultant)/self.mass)*1), 0))
          print(self.initial_vel, "m/s", self.fired_resultant)
    elif pygame.mouse.get_pressed()[0] == False:
      self.held_down = False
  def line_manager(self):
    if self.line:
      
      if abs(self.x_pos-mouse_pos[0])!= 0:
        self.angle = math.degrees(math.atan(abs(self.y_pos-mouse_pos[1])/abs(self.x_pos-mouse_pos[0])))
      elif abs(self.x_pos-mouse_pos[0])==0:
        self.angle = 90
      
      
      self.resultant = math.sqrt(abs(self.x_pos-mouse_pos[0])**2+abs(self.y_pos-mouse_pos[1])**2)
      if self.resultant<=150:
        self.boundary_pos= mouse_pos
      if self.resultant>150:
        pygame.draw.line(screen, "Red", (self.x_pos, self.y_pos), self.boundary_pos, 3)
      else:  
        pygame.draw.line(screen, "Black", (self.x_pos, self.y_pos), mouse_pos, 3)
    
    
  def update(self):
    
    pygame.draw.circle(screen, "Blue", (self.rect.centerx, self.rect.centery), 10)
    self.mouse_click_manager()
    self.line_manager()
golf_ball = Golf_Ball(-3.5, w*.2, h*.8, "White", 0.04593)
while running:
  #Event Loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
          running = False

  #Time increase
  time +=0.5
  mouse_pos = pygame.mouse.get_pos()

  screen.fill('White') 
  
  
  grass = pygame.draw.rect(screen, 'Green', ((0+10, 0+10),(w-20, h-20)))
  

    

  golf_ball.update()
    
  
  #pygame.mouse.set_pos([50,50])
    #print("X-y displacement: ",abs(x_pos-mouse_pos[0]),abs(y_pos-mouse_pos[1]),"Angle:", round(angle, 1), 'Resultant: ', round(resultant,1), 'Speed', round(initial_vel*0.3))
  fired = False
  
  

  #print(round(pygame.time.get_ticks()/1000, 0))
  clock.tick(60)
  
  pygame.display.flip()



