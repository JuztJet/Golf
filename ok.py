import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
mouse_pos = pygame.mouse.get_pos()
dt = clock.tick(70) / 1000


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
        self.image = pygame.image.load('Assets/golf.png').convert_alpha()
        self.image_copy = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=self.location_vector)
        self.x_inverse, self.y_inverse = False, False

    def mouse_click_manager(self):
        if pygame.mouse.get_pressed()[0] == True and self.shoot == False:

            if self.rect.collidepoint(self.mouse_pos_vector):

                if self.line == False and self.held_down == False:
                    self.held_down = True
                    self.line = True
                    print(2)
            if self.line and self.held_down == False:
                self.held_down = True
                self.line = False

                self.fired_resultant = self.resultant * self.velocity_constant
                self.initial_vel = int(round(((self.fired_resultant / self.mass) * 1), 0))
                print("Hit", self.initial_vel)
                self.location_vector = self.location_vector.move_towards(self.mouse_pos_vector, -100)

                #self.shoot = True
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

            pygame.draw.line(self.screen, "Black", self.location_vector, self.mouse_pos_vector, 3)
            pygame.draw.line(self.screen, "Black", (0,self.horizontal_vector.y), self.horizontal_vector, 3)
            horizontal_vector = pygame.math.Vector2(self.horizontal_vector-(0, self.horizontal_vector.y))
            #print((self.location_vector-self.mouse_pos_vector).angle_to(horizontal_vector))
           # print(self.mouse_pos_vector)

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
        self.mouse_pos_vector.update(mouse_pos)

        self.dt = dt


        self.mouse_click_manager()
        self.line_manager()
        self.resistance = 800

        self.rect.center = self.location_vector
        self.screen.blit(self.image, (self.rect))
        pygame.draw.rect(self.screen, 'White', self.rect, 1)


class Block:

    def __init__(self, x_pos, y_pos, width, height, screen, disabled, dt):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.screen = screen
        self.disabled = disabled
        self.width = width
        self.height = height
        self.image = pygame.transform.smoothscale(pygame.image.load('Assets/Wooden_Block.png'),
                                                  (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.mask = pygame.mask.from_surface(self.image)
        self.dt = dt

        self.clock = 0
        self.counter = 0
        self.dummy_rect = pygame.Rect((self.x_pos - 5, self.y_pos - 5), (self.rect.width + 10, self.rect.height + 10))
        self.direction = True
        self.in_block = False

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


golf_ball = Golf_Ball(200, 200, 0.04593, 20, 20, mouse_pos, screen, dt)
block_1 = Block(100, 300, 50, 20, screen, False, dt)

block = pygame.transform.rotate(
    pygame.transform.smoothscale(pygame.image.load('Assets/Wooden_Block.png').convert_alpha(), (100, 50)), 45)
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

# class Block:
#
#   def __init__(self, x_pos, y_pos, width, height, screen, disabled, dt, time, clock):
#     self.x_pos = x_pos
#     self.y_pos = y_pos
#     self.screen = screen
#     self.disabled = disabled
#     self.width = width
#     self.height = height
#     self.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (self.width, self.height))
#     self.rect = self.image.get_rect(topleft= (self.x_pos, self.y_pos))
#     self.mask = pygame.mask.from_surface(self.image)
#     self.dt = dt
#     self.time = time
#     self.clock = 0
#     self.saftey_factor = 0
#     self.counter = 0
#     self.dummy_rect = pygame.Rect((self.x_pos-5, self.y_pos - 5), (self.rect.width+10, self.rect.height+10))
#     self.in_saftey_area = False


# print(self.framerate)
# if self.framerate>=65:
#   self.saftey_factor=1000
#   self.dummy_rect = pygame.Rect((self.x_pos - 5, self.y_pos - 5), (self.rect.width + 10, self.rect.height + 10))
# elif self.framerate>=50:
#   self.dummy_rect = pygame.Rect((self.x_pos - 6, self.y_pos - 6), (self.rect.width + 12, self.rect.height + 12))
#   self.saftey_factor=1000
# elif self.framerate>=30:
#   self.saftey_factor=50000
# else:
#   self.saftey_factor=1000000
# if golf_ball.rect.colliderect(self.dummy_rect):
#   if self.in_saftey_area==False:
#     if golf_ball.shoot:
#       self.saftey_speed = golf_ball.initial_vel
#       self.projected_x = golf_ball.rect.x
#       self.projected_y = golf_ball.rect.y
#
#
#       for x in range(0, self.saftey_factor):
#         self.counter +=1
#
#         self.projected_x -= (self.saftey_speed * (math.cos(math.radians(golf_ball.angle)))) * self.dt
#         self.projected_y -= (self.saftey_speed * (math.sin(math.radians(golf_ball.angle)))) * self.dt
#         if abs(self.rect.bottom - self.projected_y)<=10:
#           print(2)
#           if golf_ball.y_inverse:
#             golf_ball.y_inverse = False
#           else:
#             golf_ball.y_inverse = True
#           self.in_saftey_area = True
#
#
#
#         elif abs(self.rect.top-self.projected_y+golf_ball.rect.height)<=10:
#           if golf_ball.y_inverse:
#             golf_ball.y_inverse = False
#           else:
#             golf_ball.y_inverse = True
#           print(3)
#           self.in_saftey_area = True
#
#
#         elif abs(self.rect.left - self.projected_x+golf_ball.rect.width)<=10:
#           if golf_ball.x_inverse:
#             golf_ball.x_inverse = False
#           else:
#             golf_ball.x_inverse = True
#           print(4)
#           self.in_saftey_area = True
#
#         elif abs(self.rect.right - self.projected_x)<=10:
#           if golf_ball.x_inverse:
#             golf_ball.x_inverse = False
#           else:
#             golf_ball.x_inverse = True
#           self.in_saftey_area = True
#
#         self.saftey_speed -=golf_ball.resistance * self.dt
#         print(x, '- Xpos=', self.projected_x, '- Ypos=', self.projected_y, '- Saftey Speed=',self.saftey_speed)
#       print(self.counter)
#       print(self.saftey_factor)
#       self.counter = 0
# else:
#   self.in_saftey_area = False
