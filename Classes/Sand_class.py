import pygame


class Sand:
    def __init__(self, w, h, golf_ball, dt, x, y, sand_resistance, screen):
        self.w = w
        self.h = h
        self.golf_ball = golf_ball
        self.dt = dt
        self.x = x
        self.y = y
        self.sand_resistance = sand_resistance
        self.image = pygame.transform.smoothscale(pygame.image.load("Assets\sand.png").convert_alpha(), (self.w,self.h))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.screen = screen

    def sand_process(self):
        if self.golf_ball.rect.colliderect(self.rect):
            self.golf_ball.resistance = 300 + self.sand_resistance

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.sand_process()