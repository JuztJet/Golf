import pygame
import math


class power_up:
    def __init__(self, x, y, golf_ball, type, screen, destroy):

        self.golf_ball = golf_ball
        self.screen = screen
        self.type = type
        self.on_powerup = False
        self.destroy = destroy
        self.destroyed = False
        if self.type == "Slow":
            self.image = pygame.transform.smoothscale(pygame.image.load("Assets\slow_down_powerup.png").convert_alpha(), (50,50))
        elif self.type == "Speed":
            self.image = pygame.transform.smoothscale(
                pygame.image.load("Assets\speed_up_power_up.png").convert_alpha(),
                (50, 50))

        self.rect = self.image.get_rect(topleft=(x, y))

    def slow(self):
        print(self.golf_ball.y_vel)
        if self.golf_ball.rect.colliderect(self.rect):
            if not self.on_powerup:
                self.on_powerup = True
                self.golf_ball.initial_vel -= 100
                if self.destroy:
                    self.destroyed = True
        else:
            self.on_powerup = False
    def speed(self):
        if self.golf_ball.rect.colliderect(self.rect):
            if not self.on_powerup:
                self.on_powerup = True
                self.golf_ball.initial_vel += 200
                if self.destroy:
                    self.destroyed = True
        else:
            self.on_powerup = False

    def update(self):
        if not self.destroyed:
            if self.type == "Slow":
                self.slow()
            elif self.type == "Speed":
                self.speed()

            self.screen.blit(self.image,self.rect)

