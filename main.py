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
x = 0
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
    self.mass = mass
    self.angle = 0
    self.shoot = False
    self.resistance = 300
    self.velocity_constant = 0.3
    self.image = pygame.image.load('golf.png').convert_alpha()
    self.image_copy = pygame.transform.rotate(self.image, 0)
    self.rect = self.image.get_rect(center =(self.x_pos, self.y_pos) )
    self.spin_angel = 0
    self.x_inverse, self.y_inverse = False,False
    self.mask = pygame.mask.from_surface(self.image)

  def mouse_click_manager(self):
    if pygame.mouse.get_pressed()[0] == True and self.shoot == False:
    
      if self.rect.collidepoint(mouse_pos):
      
        
        if self.line == False and self.held_down ==False:
          self.held_down = True
          self.line = True
      if self.line and self.held_down==False and self.resultant<=190:
          self.held_down = True
          self.line = False
          #print("Hit")
          self.fired_resultant = self.resultant*self.velocity_constant
          self.initial_vel = int(round((((self.fired_resultant)/self.mass)*1), 0))
          #print(self.initial_vel, "m/s", self.fired_resultant)
          self.shoot = True
          self.x_inverse, self.y_inverse = False, False

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
        if mouse_pos[1]>self.y_pos:
          self.angle = -90
        else:
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
    #print('\nInitial Velocity = ', self.initial_vel, '\nTheta = ', self.angle)
    self.x_vel = self.initial_vel * (math.cos(math.radians(self.angle)))
    self.y_vel = self.initial_vel * (math.sin(math.radians(self.angle)))
    #print(self.x_vel, self.y_vel)
    if self.x_inverse:
      self.x_vel *=-1
    if self.y_inverse:
      self.y_vel*=-1
    self.x_pos -= self.x_vel*dt
    self.y_pos -= self.y_vel*dt

    self.initial_vel -= self.resistance*dt
    if self.initial_vel<=0:
      self.shoot = False
    #self.rect = pygame.Rect((self.x_pos - 10, self.y_pos - 10), (20, 20))
    self.rect.centerx = self.x_pos
    self.rect.centery = self.y_pos
    #self.rect.move_ip(self.x_pos,self.y_pos)
  def bounce_detection(self):
    if self.rect.x <10:
      self.rect.x = 10
      if self.x_inverse:
        self.x_inverse=False
      else:
        self.x_inverse=True

    if (self.rect.x+self.rect.width)>w-10:
      self.rect.x = w-10-self.rect.width
      if self.x_inverse:
        self.x_inverse = False
      else:
        self.x_inverse = True

    if self.rect.y <=10:
      if self.y_inverse:
        self.y_inverse = False
      else:
        self.y_inverse = True

    if (self.rect.bottom)>=h-10:
      if self.y_inverse:
        self.y_inverse = False
      else:
        self.y_inverse = True
    if self.rect.bottom >h-10:
      self.rect.y =(h-10)-self.rect.height
    if self.rect.top <10:
      self.rect.y = 10


  def update(self):


    #pygame.draw.circle(screen, "Blue", (self.rect.centerx, self.rect.centery), 10)
    if self.shoot:
      self.shooting()
      self.bounce_detection()
      self.spin_angel += self.initial_vel*10*dt
      self.image_copy = pygame.transform.rotate(self.image, self.spin_angel)
    screen.blit(self.image_copy, (self.rect.centerx-int(self.image_copy.get_width()/2),self.rect.centery-int(self.image_copy.get_height()/2 )))
    pygame.draw.rect(screen, 'White', self.rect, 1)


    self.mouse_click_manager()
    self.line_manager()

class button:

  def __init__(self, x_pos, y_pos, mode, direction, disable_after_use):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.mode = mode
    self.direction = direction
    self.disable_after_use = disable_after_use
    self.enabled_button_images = {
      'Flat': pygame.transform.scale(pygame.image.load('Green Button.png').convert_alpha(), (50, 50)),
      'Left':pygame.image.load('Green Button Facing left.png').convert_alpha(),
      'Right':pygame.transform.flip(pygame.image.load('Green Button Facing left.png').convert_alpha(), True, False),
      'Down':pygame.transform.rotate(pygame.image.load('Green Button Facing left.png').convert_alpha(), 90),
      'Up':pygame.transform.rotate(pygame.image.load('Green Button Facing left.png').convert_alpha(), 270)
      }
    self.disabled_button_images = {
      'Flat': pygame.transform.scale(pygame.image.load('Red Button.png').convert_alpha(), (50, 50)),
      'Left':pygame.image.load('Red button facing left.png').convert_alpha(),
      'Right':pygame.transform.flip(pygame.image.load('Red button facing left.png').convert_alpha(), True, False),
      'Down':pygame.transform.rotate(pygame.image.load('Red button facing left.png').convert_alpha(), 90),
      'Up':pygame.transform.rotate(pygame.image.load('Red button facing left.png').convert_alpha(), 270)
      }


    if self.mode == 'Enabled':
      self.image = self.enabled_button_images[self.direction]
    elif self.mode == 'Disabled':
      self.image = self.disabled_button_images[self.direction]
    else:
      print('No Mode given')


    self.image.set_colorkey('White')

    self.rect = self.image.get_rect(topleft= (self.x_pos+10, self.y_pos+10))
    self.mask = pygame.mask.from_surface(self.image)
  def clicked(self):
    if golf_ball.rect.colliderect(self.rect):
      offset_x, offset_y = golf_ball.rect.left - button_1.rect.left, golf_ball.rect.top - button_1.rect.top
      if abs(self.rect.bottom - golf_ball.rect.top)<10:#Bottom
        if self.direction == 'Down':

          if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)):
            if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] >= 14 and \
                    button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] >= 5.5 and \
                    button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] <= 49:
              print(button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the bottom')
              if self.mode == 'Disabled':
                self.mode ='Enabled'
              else:
                self.mode = 'Disabled'
              self.update_golf_ball_colour()
        else:
          print('Bottom side was hit')
        if golf_ball.rect.top <self.rect.bottom:
          golf_ball.rect.y +=11
        if golf_ball.y_inverse:
          golf_ball.y_inverse = False
        else:
          golf_ball.y_inverse = True


      if abs(self.rect.top - golf_ball.rect.bottom)<10:
        if self.direction == 'Up':

          if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)):

            if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] <= 7 and \
                    button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] <= 43:
              print(button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the Top')
              if self.mode == 'Disabled':
                self.mode ='Enabled'
              else:
                self.mode = 'Disabled'
              self.update_golf_ball_colour()
        else:
          print('Top side was hit')

        if golf_ball.rect.bottom >self.rect.top:
          golf_ball.rect.y -=11

        if golf_ball.y_inverse:
          golf_ball.y_inverse = False
        else:
          golf_ball.y_inverse = True#Top

      if abs(self.rect.left-golf_ball.rect.right)<10:
          if golf_ball.rect.right > self.rect.left:
            golf_ball.rect.x -= 11

          if self.direction=='Left':

            if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)):
              if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] <= 8 and \
                      button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] <= 43 and \
                      button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] >= 5.5:
                print(button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the left')
                if self.mode == 'Disabled':
                  self.mode = 'Enabled'
                else:
                  self.mode = 'Disabled'
                self.update_golf_ball_colour()
          else:
            print('Left Side hit')
          if golf_ball.x_inverse:
            golf_ball.x_inverse = False
          else:
            golf_ball.x_inverse = True
          self.ball_in_button = True#Left


      elif abs(self.rect.right-golf_ball.rect.left)<10:
        if golf_ball.rect.left <self.rect.right:
          golf_ball.rect.x +=11
        if self.direction == 'Right':

          if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)):
            if button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] >= 14 and \
                    button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] <= 43 and \
                    button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] >= 5.5:
              print(button_1.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the Right')
              if self.mode == 'Disabled':
                self.mode ='Enabled'
              else:
                self.mode = 'Disabled'
              self.update_golf_ball_colour()
        else:
          print('Hit Right Side')
        if golf_ball.x_inverse:
          golf_ball.x_inverse = False
        else:
          golf_ball.x_inverse = True
        self.ball_in_button=True#Right
  def update_golf_ball_colour(self):
    if self.mode == 'Enabled':
      self.image = self.enabled_button_images[self.direction]
      print(2)
    elif self.mode == 'Disabled':
      self.image = self.disabled_button_images[self.direction]
      print(3)
    self.image.set_colorkey('White')
    self.mask = pygame.mask.from_surface(self.image)


  def update(self):
    self.clicked()
    screen.blit(self.image, self.rect)
    pygame.draw.rect(screen, 'Black', self.rect, 1)

golf_ball = Golf_Ball(-3.5, w*.5, h*.8, "White", 0.04593)
button_1 = button(200, h-400, 'Disabled', 'Right', 'False')
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


  button_1.update()
  golf_ball.update()

    
  
  #pygame.mouse.set_pos([50,50])
    #print("X-y displacement: ",abs(x_pos-mouse_pos[0]),abs(y_pos-mouse_pos[1]),"Angle:", round(angle, 1), 'Resultant: ', round(resultant,1), 'Speed', round(initial_vel*0.3))
  fired = False
  
  
  #print(time)
  #print(golf_ball.angle)
  dt = clock.tick(70) / 1000
  #print(golf_ball.rect.x, golf_ball.rect.y)
  #print(round(pygame.time.get_ticks()/1000, 0))
  clock.tick(70)
  #print(golf_ball.angle)
  #print(button_1.ball_in_button)
  pygame.display.flip()