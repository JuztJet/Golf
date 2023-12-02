import pygame
import math


class slope:
    def __init__(self, x, y, golf_ball, width, height, slope, screen):
        self.slope = slope
        self.golf_ball = golf_ball
        self.screen = screen
        if self.slope == "Down":
            self.image = pygame.transform.smoothscale(pygame.image.load("Assets\golf.png").convert_alpha(), (width,height))
        self.rect = pygame.Rect(x, y, width, height)

    def slow(self):
        print(self.golf_ball.y_vel)
        if self.golf_ball.rect.colliderect(self.rect):
            if  self.golf_ball.y_vel>0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel-=10
                print(1)
            elif self.golf_ball.y_vel<0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel+=10
                print(3)
            elif self.golf_ball.shoot==False:
                self.golf_ball.resisting = True
                print(3)
                self.golf_ball.shoot=True
                self.golf_ball.initial_vel= 25
                self.golf_ball.angle=268
                if self.golf_ball.y_inverse:
                    self.golf_ball.y_inverse = False
                else:
                    self.golf_ball.y_inverse = True
        else:
            self.golf_ball.resisting = False
    def update(self):
        if self.slope == "Down":
            self.slow()
            self.screen.blit(self.image,self.rect)

