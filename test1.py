import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
mouse_pos = pygame.mouse.get_pos()
dt = clock.tick(70) / 1000

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





class Golf_Ball:
    def __init__(self, x_pos, y_pos, mass, w, h, mouse_pos, screen, dt):
        self.screen = screen
        self.resisting = False

        # self.dt = dt
        self.mass = mass
        self.w = w
        self.h = h
        self.location_vector = pygame.math.Vector2(x_pos, y_pos)
        self.horizontal_vector = pygame.math.Vector2(x_pos-w/2, y_pos)
        self.speed_vector = pygame.math.Vector2(0, 0)
        self.mouse_pos_vector = pygame.math.Vector2(mouse_pos)
        self.visible = True
        self.initial_vel = 0
        self.x_vel, self.y_vel = 0, 0
        self.resultant = 0
        self.mouse_pos = mouse_pos
        self.fired = True
        self.hit_time = 0
        self.held_down = False
        self.line = False
        self.fired_resultant = 0
        self.angle = 0
        self.shoot = False
        self.resistance = 100
        self.velocity_constant = 0.3
        self.spin_angel = 0
        self.boundary_pos = [(), (), ()]
        self.image = pygame.image.load('Assets/golf.png').convert_alpha()
        self.image_copy = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=self.location_vector)
        self.x_inverse, self.y_inverse = False, False

    def mouse_click_manager(self):
        if pygame.mouse.get_pressed()[0] == True and self.shoot == False:

            if self.rect.collidepoint(self.mouse_pos):

                if self.line == False and self.held_down == False:
                    self.held_down = True
                    self.line = True
            if self.line and self.held_down == False and self.resultant <= 190:
                self.held_down = True
                self.line = False
                print("Hit")
                self.fired_resultant = self.resultant * self.velocity_constant
                self.initial_vel = int(round((((self.fired_resultant) / self.mass) * 1), 0))
                self.shoot = True
                self.x_inverse, self.y_inverse = False, False

        elif pygame.mouse.get_pressed()[0] == False:
            self.held_down = False

    def line_manager(self):
        if self.line:

            if abs(self.rect.centerx - self.mouse_pos[0]) != 0:
                self.angle = math.degrees(math.atan(abs(self.rect.centery - self.mouse_pos[1]) / abs(self.rect.centerx  - self.mouse_pos[0])))
                if self.mouse_pos[1] < self.rect.centery:
                    self.angle = self.angle * -1
                if self.mouse_pos[0] < self.rect.centerx:
                    self.angle = abs(self.angle - 90) + 90
            elif abs(self.rect.centerx  - self.mouse_pos[0]) == 0:
                if self.mouse_pos[1] > self.rect.centery:
                    self.angle = 90
                else:
                    self.angle = -90

            self.resultant = math.sqrt(abs(self.rect.centerx  - self.mouse_pos[0]) ** 2 + abs(self.rect.centery - self.mouse_pos[1]) ** 2)
            if self.resultant <= 190:
                self.boundary_pos[0] = self.mouse_pos

            if self.resultant > 190:
                pygame.draw.line(self.screen, "Red", (self.rect.centerx , self.rect.centery), self.boundary_pos[0], 3)
            elif self.resultant > 120:
                pygame.draw.line(self.screen, "Orange", (self.rect.centerx , self.rect.centery), self.mouse_pos, 3)
            elif self.resultant > 70:
                pygame.draw.line(self.screen, "Yellow", (self.rect.centerx , self.rect.centery), self.mouse_pos, 3)

            else:
                pygame.draw.line(self.screen, "Black", (self.rect.centerx , self.rect.centery), self.mouse_pos, 3)


    def shooting(self):

        self.x_vel = self.initial_vel * (math.cos(math.radians(self.angle)))
        self.y_vel = self.initial_vel * (math.sin(math.radians(self.angle)))
        if self.x_inverse:
            self.x_vel *= -1
        if self.y_inverse:
            self.y_vel *= -1
        self.rect.centerx -= self.x_vel * self.dt
        self.rect.centery -= self.y_vel * self.dt
        self.initial_vel -= self.resistance * self.dt
        if self.initial_vel <= 10:
            self.shoot = False

    def bounce_detection(self):
        if self.rect.left <= 0:  # Left
            if self.rect.left < 0:
                self.rect.left = 1

            if self.x_inverse:
                self.x_inverse = False
            else:
                self.x_inverse = True

        if self.rect.right >= 640:  # Right
            if self.rect.right > 640:
                self.rect.right = 639
            if self.x_inverse:
                self.x_inverse = False
            else:
                self.x_inverse = True

        if self.rect.top <= 0:  # Top
            if self.rect.top < 0:
                self.rect.top = 1
            if self.y_inverse:
                self.y_inverse = False
            else:
                self.y_inverse = True

        if self.rect.bottom >= 480:  # Bottom
            if self.rect.bottom > 480:
                self.rect.bottom = 479
            if self.y_inverse:
                self.y_inverse = False
            else:
                self.y_inverse = True


    def update(self, mouse_pos, dt):
        self.mouse_pos = mouse_pos
        self.dt = dt

        if self.visible:
            if self.shoot:
                self.shooting()
                self.bounce_detection()
                self.spin_angel += self.initial_vel * 6 * self.dt
                self.image_copy = pygame.transform.rotate(self.image, self.spin_angel)

            else:
                self.mouse_click_manager()
                self.line_manager()

            self.resistance = 420
            self.screen.blit(self.image_copy, (self.rect.centerx - int(self.image_copy.get_width() / 2),
                                               self.rect.centery - int(self.image_copy.get_height() / 2)))


class Block:

  def __init__(self, x_pos, y_pos, width, height, screen, disabled, dt, time, clock, reciprocating, start_p, end_p, speed):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.screen = screen
    self.disabled = disabled
    self.width = width
    self.height = height
    self.image = pygame.transform.smoothscale(pygame.image.load('Assets/Wooden_Block.png'), (self.width, self.height))
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

    if doIntersect(p1, q1, p2_2, q2_2):

      print("Yes-----------")
      golf_ball.rect.right = self.rect.left
      golf_ball.rect.right -= 7
      if golf_ball.x_inverse:
        golf_ball.x_inverse = False
      else:
        golf_ball.x_inverse = True
    if doIntersect(p1, q1, p2_3, q2_3): # Right

      print("Yes-----------")
      golf_ball.rect.left = self.rect.right
      golf_ball.rect.left += 7
      if golf_ball.x_inverse:
        golf_ball.x_inverse = False
      else:
        golf_ball.x_inverse = True
    if doIntersect(p1, q1, p2_4, q2_4): # Bottom

      print("Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-Yep-")
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
                golf_ball.rect.right = self.rect.left
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
                golf_ball.rect.left = self.rect.right
                self.side_bounce(golf_ball)
                return

          if abs(golf_ball.rect.top - self.rect.bottom)<=9:#Bottom
            #print(7)

            if golf_ball.rect.top <self.rect.bottom:
              golf_ball.rect.top = self.rect.bottom
              golf_ball.rect.top +=4
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

      #print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
      self.in_block = True



      if golf_ball.rect.centerx<self.rect.centerx: # Golfball to left
        golf_ball.shoot = True
        golf_ball.initial_vel = self.speed * self.dt * 140

        if abs(golf_ball.rect.centerx - self.rect.centerx) != 0:

          if golf_ball.rect.centery>self.rect.centery:
            golf_ball.angle = 10 - (math.degrees(math.atan(
              abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))

          elif golf_ball.rect.centery<self.rect.centery:
            golf_ball.angle = 10+(math.degrees(math.atan(
              abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))#
        if golf_ball.rect.centery==self.rect.centery:
            golf_ball.angle = 10


      else:
        golf_ball.shoot = True
        golf_ball.initial_vel = self.speed * self.dt * 160
        if abs(golf_ball.rect.centerx - self.rect.centerx) != 0:
          if golf_ball.rect.centery>self.rect.centery: # when golfball is lower
            golf_ball.angle = 200+ (math.degrees(math.atan(
                abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))
            # golf_ball.rect.centery -= 10
          elif golf_ball.rect.centery<self.rect.centery: #when golfball is higher
            golf_ball.angle = 160-(math.degrees(math.atan(
              abs(golf_ball.rect.centery - self.rect.centery) / abs(golf_ball.rect.centerx - self.rect.centerx+1))))

            # golf_ball.rect.centery += 10
        if golf_ball.rect.centery == self.rect.centery:
            golf_ball.angle = 190

      print(golf_ball.angle)
      self.x_inverse, self.y_inverse = False, False


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
    #self.side_bounce(golf_ball)
    #pygame.draw.rect(self.screen, 'Blue', self.dummy_rect, )
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)

golf_ball = Golf_Ball(200, 200, 0.04593, 20, 20, mouse_pos, screen, dt)
#640, 480
block1 = Block(90, 110, 100, 70, screen, False,dt, 0, 0, True,
                         90, 450, 385)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            key = event.key
            if event.key == pygame.K_ESCAPE:
                running = False

    mouse_pos = pygame.mouse.get_pos()
    screen.fill('Green')
    golf_ball.update(mouse_pos, dt)
    block1.update(golf_ball)

    # screen.blit(block, block_rect)
    clock.tick(70)
    dt = clock.tick(70) / 1000
    pygame.display.flip()

pygame.quit()