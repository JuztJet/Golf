import pygame
import math
class corner_block:

  def __init__(self, x_pos, y_pos, width, height, screen, disabled, dt, rotation):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.screen = screen
    self.disabled = disabled
    self.width = width
    self.height = height
    self.rotation = rotation
    self.image = pygame.transform.rotate(pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png').convert_alpha(), (width, height)), self.rotation)
    self.rect = self.image.get_rect(topleft= (self.x_pos, self.y_pos))
    self.mask = pygame.mask.from_surface(self.image)
    self.dt = dt
    self.clock = 0
    self.counter = 0
    self.dummy_rect = pygame.Rect((self.x_pos-5, self.y_pos - 5), (self.rect.width+10, self.rect.height+10))
    self.in_saftey_area = False
    self.direction = True
    self.in_block = False




  def bounced(self, golf_ball):



    if golf_ball.rect.colliderect(self.rect):
      if not self.in_block:
        offset_x = self.rect.x - golf_ball.rect.x
        offset_y = self.rect.y - golf_ball.rect.y
        if golf_ball.mask.overlap(self.mask, (offset_x, offset_y)):
          print(golf_ball.mask.overlap(self.mask, (offset_x, offset_y)))
          if self.rotation == -45:
            if golf_ball.angle ==0:
              golf_ball.angle = -90
            elif golf_ball.angle >0 and golf_ball.angle<179:
              golf_ball.angle +=90
            elif golf_ball.angle<=269 and golf_ball.angle>=90:
              golf_ball.angle-=90
            elif golf_ball.angle==-90:
              golf_ball.angle = 180
            elif golf_ball.angle < 0:
              golf_ball.angle = 269- abs(golf_ball.angle)
          elif self.rotation == 45:
            if golf_ball.angle ==0:
              golf_ball.angle = -90
            elif golf_ball.angle >=90 and golf_ball.angle<179:
              golf_ball.angle +=90
            elif golf_ball.angle>0 and golf_ball.angle<90:
              golf_ball.angle= (90-golf_ball.angle)*-1
            elif golf_ball.angle<0:
              golf_ball.angle = 269-golf_ball.angle
          elif self.rotation == 135:
            if golf_ball.angle ==180:
              golf_ball.angle = -90
            elif golf_ball.angle ==90:
              golf_ball.angle =0
            elif golf_ball.angle>180:
              golf_ball.angle= (golf_ball.angle-90)
            elif golf_ball.angle>90 and golf_ball.angle <180:
              golf_ball.angle = golf_ball.angle-90
            elif golf_ball.angle<90 and golf_ball.angle >0:
              golf_ball.angle = (90-golf_ball.angle)*-1
            elif golf_ball.angle <0 and golf_ball.angle <-45:
              golf_ball.angle = 269+golf_ball.angle
              print(golf_ball.angle)
              self.in_block = True
              print(2)
            elif golf_ball.angle <0 and golf_ball.angle >-45:
              golf_ball.angle = (90+golf_ball.angle)
              print(golf_ball.angle)
              self.in_block = True
              print(2)
          elif self.rotation == -135:
            if golf_ball.angle == -90:
              golf_ball.angle = 0
              self.in_block = True

            elif golf_ball.angle == 180:
              golf_ball.angle = 90
              self.in_block = True

            elif golf_ball.angle<0:
              golf_ball.angle = 90 + golf_ball.angle
              print(2, golf_ball.angle)
              self.in_block = True

            elif golf_ball.angle < 180 and golf_ball.angle >=90:
              golf_ball.angle = golf_ball.angle-90
              self.in_block = True

            elif golf_ball.angle > 180 and golf_ball.angle <225:
              golf_ball.angle = golf_ball.angle-90
              self.in_block = True

            elif golf_ball.angle > 180 and golf_ball.angle > 225:
              golf_ball.angle = (golf_ball.angle-269)
              self.in_block = True
            elif golf_ball.angle == 225:

              if golf_ball.y_inverse:
                golf_ball.y_inverse = False
              else:
                golf_ball.y_inverse = True

              if golf_ball.x_inverse:
                golf_ball.x_inverse = False
              else:
                golf_ball.x_inverse = True
              self.in_block = True


          #269
    else:
      self.in_block = False





  def update(self, golf_ball):
    self.bounced(golf_ball)

    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)



