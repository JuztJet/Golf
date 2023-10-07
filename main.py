#Physics engine

import pygame
import math


pygame.init()  #Starting Pygame
w,h = 350, 570  #Getting width height

screen = pygame.display.set_mode((w,h)) #Main widnows called screen, width,height is w,h
screen.fill('White')
running = True
line = False
dt = 1
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
    self.x_vel, self.y_vel = 0,0
    self.resultant = 0
    self.fired = True
    self.hit_time=0
    self.held_down=False
    self.line = False
    self.boundary_pos = [(), (), ()]
    self.fired_resultant =0
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.colour = colour
    self.vertical_displacement = 0
    self.horizontal_displacement = 0
    self.rect = pygame.Rect((self.x_pos-10, self.y_pos-10), (20,20))
    self.mass = mass
    self.angle = 0
    self.shoot = False
    self.resistance = .2
    self.velocity_constant = 0.005
  def mouse_click_manager(self):
    if pygame.mouse.get_pressed()[0] == True:
    
      if self.rect.collidepoint(mouse_pos):
      
        
        if self.line == False and self.held_down ==False:
          self.held_down = True
          self.line = True
      if self.line and self.held_down==False and self.resultant<=190:
          self.held_down = True
          self.line = False
          print("Hit")
          self.fired_resultant = self.resultant*self.velocity_constant
          self.initial_vel = int(round((((self.fired_resultant)/self.mass)*1), 0))
          print(self.initial_vel, "m/s", self.fired_resultant)
          self.shoot = True

    elif pygame.mouse.get_pressed()[0] == False:
      self.held_down = False
  def line_manager(self):
    if self.line:
      
      if abs(self.x_pos-mouse_pos[0])!= 0:
        self.angle = math.degrees(math.atan(abs(self.y_pos-mouse_pos[1])/abs(self.x_pos-mouse_pos[0])))
        if mouse_pos[1]<self.y_pos:
          self.angle = self.angle*-1
        if mouse_pos[0]<self.x_pos:
          self.angle= abs(self.angle-90) +90
      elif abs(self.x_pos-mouse_pos[0])==0:
        self.angle = 90
      
      
      self.resultant = math.sqrt(abs(self.x_pos-mouse_pos[0])**2+abs(self.y_pos-mouse_pos[1])**2)
      if self.resultant<=190:
        self.boundary_pos[0]= mouse_pos


      if self.resultant>190:
        pygame.draw.line(screen, "Red", (self.x_pos, self.y_pos), self.boundary_pos[0], 3)
      elif self.resultant>120:
        pygame.draw.line(screen, "Orange", (self.x_pos, self.y_pos), mouse_pos, 3)
      elif self.resultant >70:
        pygame.draw.line(screen, "Yellow", (self.x_pos, self.y_pos), mouse_pos, 3)

      else:  
        pygame.draw.line(screen, "Black", (self.x_pos, self.y_pos), mouse_pos, 3)
  def shooting(self):
    print('\nInitial Velocity = ', self.initial_vel, '\nTheta = ', self.angle)
    self.x_vel = self.initial_vel * (math.cos(math.radians(self.angle)))
    self.y_vel = self.initial_vel * (math.sin(math.radians(self.angle)))
    print(self.x_vel, self.y_vel)
    self.x_pos -= self.x_vel
    self.y_pos -= self.y_vel
    self.initial_vel -= self.resistance
    if self.initial_vel<=0:
      self.shoot = False
    self.rect = pygame.Rect((self.x_pos - 10, self.y_pos - 10), (20, 20))
  def bounce_detection(self):
    if self.rect.x <=10:
      print(self.angle)
      self.angle = abs(self.angle-90) +90
      print(self.angle)
    if (self.rect.x+self.rect.width)>=w-10:
      if self.angle >180 and self.angle<270 :

        self.angle = (270-self.angle)+(-90)
      else:
        self.angle = math.degrees(math.atan(abs(self.y_pos - mouse_pos[1]) / abs(self.x_pos - mouse_pos[0])))
    if self.rect.y <=10:
      if self.angle >90 and self.angle<180:
        self.angle = 270 - (self.angle-90)
      else:
        self.angle = 0-self.angle
    if (self.rect.y + self.rect.height)>=h:
      if self.angle<0 and self.angle>-90:
        self.angle = (self.angle*-1)
      else:
        self.angle = 180 - (self.angle-180)




    
  def update(self):
    pygame.draw.circle(screen, "Blue", (self.rect.centerx, self.rect.centery), 10)
    if self.shoot:
      self.shooting()
      self.bounce_detection()
    self.mouse_click_manager()
    self.line_manager()

golf_ball = Golf_Ball(-3.5, w*.5, h*.8, "White", 0.04593)
while running:
  #Event Loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
          running = False

  #Time increase
  time +=2*dt
  mouse_pos = pygame.mouse.get_pos()

  screen.fill('White') 
  
  
  grass = pygame.draw.rect(screen, 'Green', ((0+10, 0+10),(w-20, h-20)))
  

    

  golf_ball.update()
    
  
  #pygame.mouse.set_pos([50,50])
    #print("X-y displacement: ",abs(x_pos-mouse_pos[0]),abs(y_pos-mouse_pos[1]),"Angle:", round(angle, 1), 'Resultant: ', round(resultant,1), 'Speed', round(initial_vel*0.3))
  fired = False
  
  
  #print(time)
  #print(golf_ball.angle)
  dt = clock.tick(70) / 1000
  #print(round(pygame.time.get_ticks()/1000, 0))
  clock.tick(70)

  
  pygame.display.flip()