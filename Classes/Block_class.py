import pygame
import math
class Block:

  def __init__(self, x_pos, y_pos, width, height, screen, disabled, dt, time, clock):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.screen = screen
    self.disabled = disabled
    self.width = width
    self.height = height
    self.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (self.width, self.height))
    self.rect = self.image.get_rect(topleft= (self.x_pos, self.y_pos))
    self.mask = pygame.mask.from_surface(self.image)
    self.dt = dt
    self.time = time
    self.clock = 0
    self.saftey_factor = 0




  def bounced(self, golf_ball):
    self.saftey_speed = golf_ball.initial_vel

    if self.time <=1:
      self.framerate = self.clock
    elif self.framerate>=65:
      self.saftey_factor=2
    elif self.framerate>=50:
      self.saftey_factor=4
    elif self.framerate>=25:
      self.saftey_factor=6
    else:
      self.saftey_factor=100



    for x in range(0, self.saftey_factor):
      print(self.saftey_speed)
      self.projected_x = (self.saftey_speed * (math.cos(math.radians(golf_ball.angle)))) * self.dt
      self.projected_y = (self.saftey_speed * (math.sin(math.radians(golf_ball.angle)))) * self.dt
      if abs(self.rect.bottom - self.projected_y)<=10:
        if golf_ball.y_inverse:
          golf_ball.y_inverse = False
        else:
          golf_ball.y_inverse = True

      elif abs(self.rect.top-self.projected_y+golf_ball.rect.height)<=10:
        if golf_ball.y_inverse:
          golf_ball.y_inverse = False
        else:
          golf_ball.y_inverse = True

      elif abs(self.rect.left - self.projected_x+golf_ball.rect.width)<=10:
        if golf_ball.x_inverse:
          golf_ball.x_inverse = False
        else:
          golf_ball.x_inverse = True

      elif abs(self.rect.right - self.projected_x)<=10:
        if golf_ball.x_inverse:
          golf_ball.x_inverse = False
        else:
          golf_ball.x_inverse = True
      self.saftey_speed -=golf_ball.resistance * self.dt

    if golf_ball.rect.colliderect(self.rect):
        if abs(self.rect.bottom - golf_ball.rect.top)<=10:#Bottom

          if golf_ball.rect.top <self.rect.bottom:
            golf_ball.rect.y +=11
          if golf_ball.y_inverse:
            golf_ball.y_inverse = False
          else:
            golf_ball.y_inverse = True


        elif abs(self.rect.top - golf_ball.rect.bottom)<=10:
          if golf_ball.rect.bottom >self.rect.top:
            golf_ball.rect.bottom = self.rect.top
            golf_ball.rect.y -=2

          if golf_ball.y_inverse:
            golf_ball.y_inverse = False
          else:
            golf_ball.y_inverse = True#Top

        elif abs(self.rect.left-golf_ball.rect.right)<=10:
            if golf_ball.rect.right > self.rect.left:
              golf_ball.rect.x -= 11
            if golf_ball.x_inverse:
              golf_ball.x_inverse = False
            else:
              golf_ball.x_inverse = True#Left


        elif abs(self.rect.right-golf_ball.rect.left)<=10:
          if golf_ball.rect.left <self.rect.right:
            golf_ball.rect.x +=11
          if golf_ball.x_inverse:
            golf_ball.x_inverse = False
          else:
            golf_ball.x_inverse = True#Right




  def update(self, golf_ball, time, clock):
    self.bounced(golf_ball)
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)
    self.time = time
    self.clock = clock
