from __future__ import division

import pygame
import math


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Given three collinear points p, q, r, the function checks if


# point q lies on line segment 'pr'
def onSegment(p, q, r):
  if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
          (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
    return True
  return False


def orientation(p, q, r):
  # to find the orientation of an ordered triplet (p,q,r)
  # function returns the following values:
  # 0 : Collinear points
  # 1 : Clockwise points
  # 2 : Counterclockwise

  # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
  # for details of below formula.

  val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
  if (val > 0):

    # Clockwise orientation
    return 1
  elif (val < 0):

    # Counterclockwise orientation
    return 2
  else:

    # Collinear orientation
    return 0


# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def doIntersect(p1, q1, p2, q2):
  # Find the 4 orientations required for
  # the general and special cases
  o1 = orientation(p1, q1, p2)
  o2 = orientation(p1, q1, q2)
  o3 = orientation(p2, q2, p1)
  o4 = orientation(p2, q2, q1)

  # General case
  if ((o1 != o2) and (o3 != o4)):
    return True

  # Special Cases

  # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
  if ((o1 == 0) and onSegment(p1, p2, q1)):
    return True

  # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
  if ((o2 == 0) and onSegment(p1, q2, q1)):
    return True

  # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
  if ((o3 == 0) and onSegment(p2, p1, q2)):
    return True

  # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
  if ((o4 == 0) and onSegment(p2, q1, q2)):
    return True

  # If none of the cases
  return False


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

    self.rect_points = {
      'top_right_x': self.rect.x + self.rect.width,
      'top_right_y': self.rect.y,

      'bottom_right_x': self.rect.x + self.rect.width,
      'bottom_right_y': self.rect.y + self.rect.height,

      'top_left_x': self.rect.x,
      'top_left_y': self.rect.y,

      'bottom_left_x': self.rect.x,
      'bottom_left_y': self.rect.y + self.rect.height,
    }


  def ccd(self, golf_ball):
    p1 = Point(golf_ball.rect.centerx, golf_ball.rect.centery)
    q1 = Point(golf_ball.previous_rect.centerx, golf_ball.previous_rect.centery)
    p2_1 = Point(self.rect.x, self.rect.y)
    q2_1 = Point(self.rect.x + self.width, self.rect.y)

    p2_2 = Point(self.rect_points['top_left_x'], self.rect_points['top_left_y'])
    q2_2 = Point(self.rect_points['bottom_left_x'], self.rect_points['bottom_left_y'])

    p2_3 = Point(self.rect_points['top_right_x'], self.rect_points['top_right_y'])
    q2_3 = Point(self.rect_points['bottom_right_x'], self.rect_points['bottom_right_y'])

    p2_4 = Point(self.rect_points['bottom_left_x'], self.rect_points['bottom_left_y'])
    q2_4 = Point(self.rect_points['bottom_right_x'], self.rect_points['bottom_right_y'])

    if doIntersect(p1, q1, p2_1, q2_1):
      print("Yes")
      golf_ball.rect.bottom = self.rect.top
      golf_ball.rect.bottom -= 7
      if golf_ball.y_inverse:
        golf_ball.y_inverse = False
      else:
        golf_ball.y_inverse = True

    elif doIntersect(p1, q1, p2_2, q2_2):

      print("Yes")
      golf_ball.rect.right = self.rect.left
      golf_ball.rect.right -= 7
      if golf_ball.x_inverse:
        golf_ball.x_inverse = False
      else:
        golf_ball.x_inverse = True
    elif doIntersect(p1, q1, p2_3, q2_3): # Right

      print("Yes")
      golf_ball.rect.left = self.rect.right
      golf_ball.rect.left += 7
      if golf_ball.x_inverse:
        golf_ball.x_inverse = False
      else:
        golf_ball.x_inverse = True
    elif doIntersect(p1, q1, p2_4, q2_4): # Bottom

      print("Yes")
      golf_ball.rect.top = self.rect.bottom
      golf_ball.rect.top -= 7
      if golf_ball.y_inverse:
        golf_ball.y_inverse = False
      else:
        golf_ball.y_inverse = True

  def bounced(self, golf_ball):

    if golf_ball.rect.colliderect(self.rect):
          if abs(self.rect.left-golf_ball.rect.right)<=5:
            if not self.reciprocating:
              if golf_ball.rect.right > self.rect.left:
                golf_ball.rect.right -= 1
              if golf_ball.x_inverse:
                golf_ball.x_inverse = False
              else:
                golf_ball.x_inverse = True#Left
            else:
              self.side_bounce(golf_ball)
              return

          if abs(self.rect.right-golf_ball.rect.left)<=5:
            if not self.reciprocating:
              if golf_ball.rect.left <self.rect.right:
                golf_ball.rect.left +=1
              if golf_ball.x_inverse:
                golf_ball.x_inverse = False
              else:
                golf_ball.x_inverse = True#Right
            else:
              self.side_bounce(golf_ball)
              return

          if abs(self.rect.bottom - golf_ball.rect.top)<=5:#Bottom


            if golf_ball.rect.top <self.rect.bottom:
              golf_ball.rect.top +=1
            if golf_ball.y_inverse:
              golf_ball.y_inverse = False
            else:
              golf_ball.y_inverse = True

          if abs(self.rect.top - golf_ball.rect.bottom)<=5:
            if golf_ball.rect.bottom >self.rect.top:
              golf_ball.rect.bottom = self.rect.top
              golf_ball.rect.bottom -=1

            if golf_ball.y_inverse:
              golf_ball.y_inverse = False
            else:
              golf_ball.y_inverse = True



    else:
      self.in_block=False
  def side_bounce(self, golf_ball):
    if not self.in_block:
      self.in_block = True
      if abs(golf_ball.rect.left - self.rect.right)==0:
        golf_ball.rect.left+=10
        return


      if golf_ball.rect.centerx<self.rect.centerx:
        golf_ball.shoot = True
        golf_ball.initial_vel = self.speed * self.dt * 140
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
        golf_ball.initial_vel = self.speed * self.dt * 140
        if abs(golf_ball.rect.centerx - self.rect.centerx) != 0:
          if golf_ball.rect.centery>self.rect.centery:
            golf_ball.angle = 190+ (math.degrees(math.atan(
                abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))
            golf_ball.rect.centery -= 10
          elif golf_ball.rect.centery<self.rect.centery:
            golf_ball.angle = 170-(math.degrees(math.atan(
              abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))
            golf_ball.rect.centery += 10




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



  def update(self, golf_ball):
    self.bounced(golf_ball)
    if self.reciprocating:
      self.reciprocator(self.start_p,self.end_p, self.speed)
    #pygame.draw.rect(self.screen, 'Blue', self.dummy_rect, )
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)




