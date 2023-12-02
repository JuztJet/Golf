# import pygame
# pygame.init() #Start Pygame
#
# screen = pygame.display.set_mode((640,480)) #Start the screen
# image = pygame.image.load('Assets/golf.png').convert_alpha()
# rect = image.get_rect(center = (640/2, 480/2))
# x = 320
# y = 240
# x2 = 0
# running = True
# while running:
#     screen.fill('white')
#     image_copy = pygame.transform.rotate(image, x2)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: #The user closed the window!
#             running = False #Stop running
#     screen.blit(image_copy, (x-int(image_copy.get_width()/2),y-int(image_copy.get_height()/2)))
#     pygame.display.flip()
#     x2+=0.1
#     print(x2)
# pygame.quit() #Close the window
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
    self.counter = 0
    self.dummy_rect = pygame.Rect((self.x_pos-5, self.y_pos - 5), (self.rect.width+10, self.rect.height+10))
    self.in_saftey_area = False




  def bounced(self, golf_ball):

    self.framerate = self.clock
    #print(self.framerate)
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
    pygame.draw.rect(self.screen, 'Blue', self.dummy_rect, )
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)
    self.time = time
    self.clock = clock


