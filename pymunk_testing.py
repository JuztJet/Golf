from __future__ import division

import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
mouse_pos = pygame.mouse.get_pos()
dt = clock.tick(70) / 1000


# Python program to find the point of
# intersection of two lines

# Class used to used to store the X and Y
# coordinates of a point respectively
# A Python3 program to find if 2 given line segments intersect or not

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
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = 0
        self.shoot = False
        self.resistance = 100
        self.velocity_constant = 0.3
        self.spin_angel = 0
        self.image = pygame.image.load('Assets/golf.png').convert_alpha()
        self.image_copy = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.x_inverse, self.y_inverse = False, False
        self.previous_rect = self.rect.copy()
        self.c = False

    def mouse_click_manager(self):
        if pygame.mouse.get_pressed()[0] == True and self.shoot == False:

            if self.rect.collidepoint(self.mouse_pos):

                if self.line == False and self.held_down == False:
                    self.held_down = True
                    self.line = True
            if self.line and self.held_down == False:
                self.held_down = True
                self.line = False

                self.fired_resultant = self.resultant * self.velocity_constant
                self.initial_vel = int(round(((self.fired_resultant / self.mass) * 1), 0))
                print("Hit", self.initial_vel)
                self.shoot = True
                self.x_inverse, self.y_inverse = False, False

        elif not pygame.mouse.get_pressed()[0]:
            self.held_down = False

    def line_manager(self):
        if self.line:

            if abs(self.rect.centerx - self.mouse_pos[0]) != 0:
                self.angle = math.degrees(
                    math.atan(abs(self.rect.centery - self.mouse_pos[1]) / abs(self.rect.centerx - self.mouse_pos[0])))
                if self.mouse_pos[1] < self.rect.centery:
                    self.angle = self.angle * -1
                if self.mouse_pos[0] < self.rect.centerx:
                    self.angle = abs(self.angle - 90) + 90
            elif abs(self.rect.centerx - self.mouse_pos[0]) == 0:
                if self.mouse_pos[1] > self.rect.centery:
                    self.angle = 90
                else:
                    self.angle = -90

            self.resultant = math.sqrt(
                abs(self.rect.centerx - self.mouse_pos[0]) ** 2 + abs(self.rect.centery - self.mouse_pos[1]) ** 2)

            pygame.draw.line(self.screen, "Black", (self.rect.centerx, self.rect.centery), self.mouse_pos, 3)

    def shooting(self):
        self.previous_rect = self.rect.copy()

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
                self.spin_angel += self.initial_vel * 10 * self.dt
                self.image_copy = pygame.transform.rotate(self.image, self.spin_angel)

            else:
                self.mouse_click_manager()
                self.line_manager()
            self.resistance = 1400
            print(self.angle)
            self.screen.blit(self.image_copy, (self.rect.centerx - int(self.image_copy.get_width() / 2),
                                               self.rect.centery - int(self.image_copy.get_height() / 2)))
            # Driver code
            p1 = Point(self.rect.centerx, self.rect.centery)
            q1 = Point(self.previous_rect.centerx, self.previous_rect.centery)
            p2_1 = Point(block_1.rect.x, block_1.rect.y)
            q2_1 = Point(block_1.rect.x + block_1.width, block_1.rect.y)

            p2_2 = Point(block_1.rect_points['top_left_x'], block_1.rect_points['top_left_y'])
            q2_2 = Point(block_1.rect_points['bottom_left_x'], block_1.rect_points['bottom_left_y'])

            if doIntersect(p1, q1, p2_1, q2_1):
                print("Yes")
                self.rect.bottom = block_1.rect.top
                self.rect.bottom -= 7
                if self.y_inverse:
                    self.y_inverse = False
                else:
                    self.y_inverse = True

            elif doIntersect(p1, q1, p2_2, q2_2):

                print("Yes")
                self.rect.right = block_1.rect.left
                self.rect.bottom -= 7
                if self.x_inverse:
                    self.x_inverse = False
                else:
                    self.x_inverse = True

            pygame.draw.rect(self.screen, 'White', self.rect, 1)
            pygame.draw.line(self.screen, 'Blue', self.rect.center, self.previous_rect.center, 2)


class Block:

    def __init__(self, x_pos, y_pos, width, height, screen, disabled, dt):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.screen = screen
        self.disabled = disabled
        self.width = width
        self.height = height
        self.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'),
                                                  (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.mask = pygame.mask.from_surface(self.image)
        self.dt = dt

        self.clock = 0
        self.counter = 0
        self.dummy_rect = pygame.Rect((self.x_pos - 5, self.y_pos - 5), (self.rect.width + 10, self.rect.height + 10))
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

    def bounced(self, golf_ball):

        if golf_ball.rect.colliderect(self.rect):
            if abs(self.rect.left - golf_ball.rect.right) <= 5:

                if golf_ball.rect.right > self.rect.left:
                    golf_ball.rect.right = self.rect.left
                    golf_ball.rect.right -= 1
                if golf_ball.x_inverse:
                    golf_ball.x_inverse = False
                else:
                    golf_ball.x_inverse = True  # Left

            if abs(self.rect.right - golf_ball.rect.left) <= 5:

                if golf_ball.rect.left < self.rect.right:
                    golf_ball.rect.left = self.rect.right
                    golf_ball.rect.left += 1

                if golf_ball.x_inverse:
                    golf_ball.x_inverse = False
                else:
                    golf_ball.x_inverse = True

            if abs(self.rect.bottom - golf_ball.rect.top) <= 5:  # Bottom

                if golf_ball.rect.top < self.rect.bottom:
                    golf_ball.rect.top = self.rect.bottom
                    golf_ball.rect.top += 1
                if golf_ball.y_inverse:
                    golf_ball.y_inverse = False
                else:
                    golf_ball.y_inverse = True

            if abs(self.rect.top - golf_ball.rect.bottom) <= 5:
                if golf_ball.rect.bottom > self.rect.top:
                    golf_ball.rect.bottom = self.rect.top
                    golf_ball.rect.bottom -= 1

                if golf_ball.y_inverse:
                    golf_ball.y_inverse = False
                else:
                    golf_ball.y_inverse = True

    def update(self, golf_ball):
        self.bounced(golf_ball)

        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, 'Black', self.rect, 1)

        pygame.draw.line(self.screen, 'Blue', (block_1.rect_points['top_left_x'], block_1.rect_points['top_left_y']),
                         (block_1.rect_points['top_right_x'], block_1.rect_points['top_right_y']), 2)
        pygame.draw.line(self.screen, 'Purple', (block_1.rect_points['top_left_x'], block_1.rect_points['top_left_y']),
                         (block_1.rect_points['bottom_left_x'], block_1.rect_points['bottom_left_y']), 2)


golf_ball = Golf_Ball(200, 200, 0.04593, 20, 20, mouse_pos, screen, dt)
block_1 = Block(100, 300, 50, 20, screen, False, dt)

block = pygame.transform.rotate(
    pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png').convert_alpha(), (100, 50)), 45)
block_rect = block.get_rect(topleft=(300, 200))

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
    block_1.update(golf_ball)

    # screen.blit(block, block_rect)
    clock.tick(70)
    dt = clock.tick(70) / 1000
    pygame.display.flip()

pygame.quit()
