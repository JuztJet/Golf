import pygame
import math
class Block:

  def __init__(self, x_pos, y_pos, width, height, screen, disabled, dt, time, clock, reciprocating, start_p, end_p, speed):
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
    self.reciprocating = reciprocating
    self.start_p = start_p
    self.end_p = end_p
    self.speed = speed
    self.time = time
    self.clock = 0
    self.saftey_factor = 0
    self.counter = 0
    self.dummy_rect = pygame.Rect((self.x_pos-5, self.y_pos - 5), (self.rect.width+10, self.rect.height+10))
    self.in_saftey_area = False
    self.direction = True
    self.in_block = False




  def bounced(self, golf_ball):

    self.framerate = self.clock
    #print(self.framerate)
    if self.framerate>=65 or golf_ball.initial_vel <=70:
      self.saftey_factor=5
      self.dummy_rect = pygame.Rect((self.x_pos - 5, self.y_pos - 5), (self.rect.width + 10, self.rect.height + 10))
    elif self.framerate>=50 or golf_ball.initial_vel<150:
      self.dummy_rect = pygame.Rect((self.x_pos - 6, self.y_pos - 6), (self.rect.width + 12, self.rect.height + 12))
      self.saftey_factor=7
    elif self.framerate>=30 or golf_ball.initial_vel<270:
      self.saftey_factor=10
    else:
      self.saftey_factor=100000000


    if golf_ball.rect.colliderect(self.rect):
          if abs(self.rect.left-golf_ball.rect.right)<=10:
            if not self.reciprocating:
              if golf_ball.rect.right > self.rect.left:
                golf_ball.rect.x -= 14
              if golf_ball.x_inverse:
                golf_ball.x_inverse = False
              else:
                golf_ball.x_inverse = True#Left
            else:
              self.side_bounce(golf_ball)
              return

          if abs(self.rect.right-golf_ball.rect.left)<=10:
            if not self.reciprocating:
              if golf_ball.rect.left <self.rect.right:
                golf_ball.rect.x +=14
              if golf_ball.x_inverse:
                golf_ball.x_inverse = False
              else:
                golf_ball.x_inverse = True#Right
            else:
              self.side_bounce(golf_ball)
              return

          if abs(self.rect.bottom - golf_ball.rect.top)<=10:#Bottom


            if golf_ball.rect.top <self.rect.bottom:
              golf_ball.rect.y +=14
            if golf_ball.y_inverse:
              golf_ball.y_inverse = False
            else:
              golf_ball.y_inverse = True

          if abs(self.rect.top - golf_ball.rect.bottom)<=10:
            if golf_ball.rect.bottom >self.rect.top:
              golf_ball.rect.bottom = self.rect.top
              golf_ball.rect.y -=7

            if golf_ball.y_inverse:
              golf_ball.y_inverse = False
            else:
              golf_ball.y_inverse = True#Top



    else:
      self.in_block=False
  def side_bounce(self, golf_ball):
    if not self.in_block:
      print(2)
      self.in_block = True
      if abs(golf_ball.rect.centerx - self.rect.centerx)==0:
        golf_ball.rect.centerx-=10
        return


      if golf_ball.rect.centerx<self.rect.centerx:
        golf_ball.shoot = True
        golf_ball.initial_vel = self.speed * self.dt * 90
        print(golf_ball.initial_vel)
        if abs(golf_ball.rect.centerx - self.rect.centerx) != 0:

          if golf_ball.rect.centery>self.rect.centery:
            golf_ball.angle = 10 - (math.degrees(math.atan(
              abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))
            golf_ball.rect.centery-=10

          elif golf_ball.rect.centery<self.rect.centery:
            golf_ball.angle = 10+(math.degrees(math.atan(
              abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))
            golf_ball.rect.centery += 10

      else:
        golf_ball.shoot = True
        golf_ball.initial_vel = self.speed * self.dt * 90
        print(golf_ball.initial_vel)
        if abs(golf_ball.rect.centerx - self.rect.centerx) != 0:
          if golf_ball.rect.centery>self.rect.centery:
            golf_ball.angle = 190+ (math.degrees(math.atan(
                abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))
            golf_ball.rect.centery -= 10
          elif golf_ball.rect.centery<self.rect.centery:
            golf_ball.angle = 170-(math.degrees(math.atan(
              abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))
            golf_ball.rect.centery += 10
        print(3)




  def reciprocator(self, start_point, end_point, speed):
    self.speed = speed

    if self.direction:
      self.rect.x += speed*self.dt
    elif self.direction==False:

      self.rect.x -= speed*self.dt
    if self.rect.left<start_point:
      self.direction=True
    elif self.rect.right>end_point:
      self.direction=False



  def update(self, golf_ball, time, clock):
    self.bounced(golf_ball)
    if self.reciprocating:
      self.reciprocator(self.start_p,self.end_p, self.speed)
    #pygame.draw.rect(self.screen, 'Blue', self.dummy_rect, )
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)
    self.time = time
    self.clock = clock
    #print(golf_ball.initial_vel)
    # print(math.degrees(math.atan(
    #         abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx))))
    print(golf_ball.angle)



