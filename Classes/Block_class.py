import pygame
class Block:

  def __init__(self, x_pos, y_pos, width, height, screen, disabled):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.screen = screen
    self.disabled = disabled
    self.width = width
    self.height = height
    self.image = pygame.transform.smoothscale(pygame.image.load('Assets\Wooden_Block.png'), (self.width, self.height))
    self.rect = self.image.get_rect(topleft= (self.x_pos, self.y_pos))
    self.mask = pygame.mask.from_surface(self.image)

  def bounced(self, golf_ball):
    if golf_ball.rect.colliderect(self.rect):
        if abs(self.rect.bottom - golf_ball.rect.top)<=10:#Bottom

          if golf_ball.rect.top <self.rect.bottom:
            golf_ball.rect.y +=11
          if golf_ball.y_inverse:
            golf_ball.y_inverse = False
          else:
            golf_ball.y_inverse = True


        if abs(self.rect.top - golf_ball.rect.bottom)<=10:
          if golf_ball.rect.bottom >self.rect.top:
            golf_ball.rect.bottom = self.rect.top
            golf_ball.rect.y -=2

          if golf_ball.y_inverse:
            golf_ball.y_inverse = False
          else:
            golf_ball.y_inverse = True#Top

        if abs(self.rect.left-golf_ball.rect.right)<=10:
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






  def update(self, golf_ball):
    self.bounced(golf_ball)
    self.screen.blit(self.image, self.rect)
    pygame.draw.rect(self.screen, 'Black', self.rect, 1)