import pygame
import math


class slope:
    def __init__(self, x, y, golf_ball, width, height, slope, screen, intensity):
        self.slope = slope
        self.intensity = intensity
        self.golf_ball = golf_ball
        self.screen = screen
        if self.slope == "Down":
            self.image = pygame.transform.smoothscale(pygame.image.load("Assets/Red_slope_down_test.png").convert_alpha(), (width,height))
        elif self.slope == "Up":
            self.image = pygame.transform.rotate(pygame.transform.smoothscale(
                pygame.image.load("Assets/Red_slope_down_test.png").convert_alpha(),
                (width, height)), 180)
        elif self.slope == "Right":
            self.image = pygame.transform.rotate(pygame.transform.smoothscale(
                pygame.image.load("Assets/Red_slope_down_test.png").convert_alpha(),
                (width, height)), 90)
        elif self.slope == "Left":
            self.image = pygame.transform.rotate(pygame.transform.smoothscale(
                pygame.image.load("Assets/Red_slope_down_test.png").convert_alpha(),
                (width, height)), -90)
        self.rect = self.image.get_rect(topleft=(x, y))

    def slow_down(self):
        if self.golf_ball.rect.colliderect(self.rect):
            if self.golf_ball.rect.bottom > self.rect.top:
                if  self.golf_ball.y_vel>0 and self.golf_ball.shoot:
                    self.golf_ball.initial_vel-=self.intensity
                elif self.golf_ball.y_vel<0 and self.golf_ball.shoot:
                    self.golf_ball.initial_vel+=self.intensity
                elif self.golf_ball.shoot==False:
                    self.golf_ball.resisting = True
                    self.golf_ball.shoot=True
                    self.golf_ball.initial_vel= 25
                    self.golf_ball.angle=268
                    if self.golf_ball.y_inverse:
                        self.golf_ball.y_inverse = False
                    else:
                        self.golf_ball.y_inverse = True
        else:
            self.golf_ball.resisting = False
    def slow_right(self):
        if self.golf_ball.rect.colliderect(self.rect):
            if self.golf_ball.x_vel > 0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel -= self.intensity
            elif self.golf_ball.x_vel < 0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel += self.intensity
            elif self.golf_ball.shoot == False:
                self.golf_ball.resisting = True
                self.golf_ball.shoot = True
                self.golf_ball.initial_vel = 25
                self.golf_ball.angle = 180
                if self.golf_ball.x_inverse:
                    self.golf_ball.x_inverse = False
                else:
                    self.golf_ball.x_inverse = True
        else:
            self.golf_ball.resisting = False
    def slow_up(self):
        if self.golf_ball.rect.colliderect(self.rect):
            if self.golf_ball.y_vel > 0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel += self.intensity
            elif self.golf_ball.y_vel < 0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel -= self.intensity
            elif self.golf_ball.shoot == False:
                self.golf_ball.resisting = True
                self.golf_ball.shoot = True
                self.golf_ball.initial_vel = 25
                self.golf_ball.angle = 268
                if self.golf_ball.y_inverse:
                    self.golf_ball.y_inverse = False
                else:
                    self.golf_ball.y_inverse = True
        else:
            self.golf_ball.resisting = False

    def slow_left(self):
        if self.golf_ball.rect.colliderect(self.rect):
            if self.golf_ball.x_vel > 0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel += self.intensity
            elif self.golf_ball.x_vel < 0 and self.golf_ball.shoot:
                self.golf_ball.initial_vel -= self.intensity
            elif self.golf_ball.shoot == False:
                self.golf_ball.resisting = True
                self.golf_ball.shoot = True
                self.golf_ball.initial_vel = 25
                self.golf_ball.angle = 180
                if self.golf_ball.x_inverse:
                    self.golf_ball.x_inverse = False
                else:
                    self.golf_ball.x_inverse = True
        else:
            self.golf_ball.resisting = False
    def update(self):
        if self.slope == "Up":
            self.slow_up()
        elif self.slope == "Down":
            self.slow_down()
        elif self.slope == "Right":
            self.slow_right()
        elif self.slope == "Left":
            self.slow_left()
        self.screen.blit(self.image,self.rect)

