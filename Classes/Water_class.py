import pygame
class water:

  def __init__(self, x_pos, y_pos, width, height, screen, rotation):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.screen = screen
    self.width = width
    self.height = height
    self.image = pygame.transform.rotate(pygame.transform.smoothscale(pygame.image.load('Assets\Water.png'), (self.width, self.height)), rotation)
    self.rect = self.image.get_rect(topleft= (self.x_pos, self.y_pos))
    self.mask = pygame.mask.from_surface(self.image)

  def ball_in_hole(self, golf_ball):
    if golf_ball.rect.colliderect(self.rect):
      golf_ball.visible = False






  def update(self, golf_ball):
    self.ball_in_hole(golf_ball)
    self.screen.blit(self.image, self.rect)
