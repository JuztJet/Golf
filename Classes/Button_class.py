
import pygame
class Button:

  def __init__(self, x_pos, y_pos, mode, direction, disable_after_use, screen, close_hole, block, box_width, box_height, dt, time):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.screen = screen
    self.mode = mode
    self.dt = dt
    self.box_width = box_width
    self.box_height = box_height
    self.direction = direction
    self.time = time
    self.disable_after_use = disable_after_use
    self.on_button1 = False
    self.on_button2 = False
    self.enabled_button_images = {
      'Flat': pygame.transform.scale(pygame.image.load('Assets/Green Button.png').convert_alpha(), (50, 50)),
      'Left':pygame.image.load('Assets/Green Button Facing left.png').convert_alpha(),
      'Right':pygame.transform.flip(pygame.image.load('Assets/Green Button Facing left.png').convert_alpha(), True, False),
      'Down':pygame.transform.rotate(pygame.image.load('Assets/Green Button Facing left.png').convert_alpha(), 90),
      'Up':pygame.transform.rotate(pygame.image.load('Assets/Green Button Facing left.png').convert_alpha(), 270)
      }
    self.disabled_button_images = {
      'Flat': pygame.transform.scale(pygame.image.load('Assets/Red Button.png').convert_alpha(), (50, 50)),
      'Left':pygame.image.load('Assets/Red button facing left.png').convert_alpha(),
      'Right':pygame.transform.flip(pygame.image.load('Assets/Red button facing left.png').convert_alpha(), True, False),
      'Down':pygame.transform.rotate(pygame.image.load('Assets/Red button facing left.png').convert_alpha(), 90),
      'Up':pygame.transform.rotate(pygame.image.load('Assets/Red button facing left.png').convert_alpha(), 270)
      }
    self.close_hole = close_hole
    if self.close_hole:
      self.wall= [
        #Top
        block(self.box_width+120, self.box_height, 100, 30, self.screen, False, self.dt, self.time, 0, False, 0, 0, 0),
        block(self.box_width+90, self.box_height, 30, 130, self.screen, False, self.dt, self.time, 0, False, 0, 0, 0),
        #Bottom
        block(self.box_width+120, self.box_height+100, 100, 30, self.screen, False, self.dt, self.time, 0, False, 0, 0, 0),
        block(self.box_width+220, self.box_height, 30, 130, self.screen, False, self.dt, self.time, 0, False, 0, 0, 0)
      ]


    if self.mode == 'Enabled':
      self.image = self.enabled_button_images[self.direction]
    elif self.mode == 'Disabled':
      self.image = self.disabled_button_images[self.direction]
    else:
      print('No Mode given')


    self.image.set_colorkey('White')

    self.rect = self.image.get_rect(topleft= (self.x_pos+10, self.y_pos+10))
    self.mask = pygame.mask.from_surface(self.image)
  def clicked(self, golf_ball):
    if golf_ball.rect.colliderect(self.rect):
      offset_x, offset_y = golf_ball.rect.left - self.rect.left, golf_ball.rect.top - self.rect.top
      if self.direction != 'Flat':
        if abs(self.rect.bottom - golf_ball.rect.top)<10:#Bottom
          if self.direction == 'Down':

            if self.mask.overlap(golf_ball.mask, (offset_x, offset_y)):
              if self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] >= 14 and \
                      self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] >= 5.5 and \
                      self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] <= 49:
                print(self.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the bottom')
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

            if self.mask.overlap(golf_ball.mask, (offset_x, offset_y)):

              if self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] <= 7 and \
                      self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] <= 43:
                print(self.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the Top')
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

              if self.mask.overlap(golf_ball.mask, (offset_x, offset_y)):
                if self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] <= 8 and \
                        self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] <= 43 and \
                        self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] >= 5.5:
                  print(self.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the left')
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

            if self.mask.overlap(golf_ball.mask, (offset_x, offset_y)):
              if self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[0] >= 14 and \
                      self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] <= 43 and \
                      self.mask.overlap(golf_ball.mask, (offset_x, offset_y))[1] >= 5.5:
                print(self.mask.overlap(golf_ball.mask, (offset_x, offset_y)), 'Button Hit at the Right')
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
      else:
        self.on_button1 = True
    elif self.on_button1 == True:
      self.on_button2 = True
    if self.on_button2 and self.on_button1:
      self.on_button2, self.on_button1 = False, False
      if self.mode == 'Disabled':
        self.mode = 'Enabled'
      else:
        self.mode = 'Disabled'
      self.update_golf_ball_colour()

  def close_hole(self):
    pass


  def update_golf_ball_colour(self):
    if self.mode == 'Enabled':
      self.image = self.enabled_button_images[self.direction]
      print(2)
    elif self.mode == 'Disabled':
      self.image = self.disabled_button_images[self.direction]
      print(3)
    self.image.set_colorkey('White')
    self.mask = pygame.mask.from_surface(self.image)


  def update(self, golf_ball):
    if  not self.disable_after_use:
      self.clicked(golf_ball)
    elif self.mode == 'Enabled':
      self.clicked(golf_ball)
    else:
      self.wall[0].update(golf_ball)
      self.wall[1].update(golf_ball)
      self.wall[2].update(golf_ball)
      self.wall[3].update(golf_ball)
      pygame.draw.line(self.screen, 'Blue', (self.wall[3].rect.x+self.wall[3].rect.width, self.wall[3].rect.y), (self.wall[3].rect.x+self.wall[3].rect.width, self.wall[3].rect.y+self.wall[3].rect.height), 2)
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)