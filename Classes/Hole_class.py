import pygame
class Hole:

  def __init__(self, x_pos, y_pos, width, height, screen):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.screen = screen
    self.width = width
    self.height = height
    self.image = pygame.transform.smoothscale(pygame.image.load('Assets\Hole.png'), (self.width, self.height))
    self.rect = self.image.get_rect(topleft= (self.x_pos, self.y_pos))
    self.mask = pygame.mask.from_surface(self.image)

  def ball_in_hole(self, golf_ball):
    if golf_ball.rect.colliderect(self.rect):
      if self.rect.collidepoint(golf_ball.rect.centerx, golf_ball.rect.centery):
        golf_ball.visible = False






  def update(self, golf_ball):
    self.ball_in_hole(golf_ball)
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)