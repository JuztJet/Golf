#Physics engine

import pygame
from Classes.Golf_Ball_Class import Golf_Ball
from Classes.Button_class import Button
from Classes.Block_class import Block
from Classes.Hole_class import Hole
from Classes.Level_Editor_Class import Level_Editor
from Classes.Level_1 import Level1
from Classes.Level_2 import Level2
from Classes.Level_3 import Level3
from Classes.Sand_class import Sand



pygame.init()  #Starting Pygame
w,h = 350, 570  #Getting width height

screen = pygame.display.set_mode((w,h)) #Main widnows called screen, width,height is w,h
screen.fill('White')
running = True
line = False
dt = 1

x = 0
clock = pygame.time.Clock()
#Variable for physics
mouse_pos = pygame.mouse.get_pos()
dt = clock.tick(70) / 1000




#Pygame Loop



golf_ball = Golf_Ball(-3.5, w*.5, h*.8, "White", 0.04593, dt, w, h, mouse_pos, screen)
# button_1 = Button(200, h-400, 'Enabled', 'Down', 'False', screen)
# test_block = Block(170, button_1.rect.bottom+20, 130, 20, screen, False)
# test_block2 = Block(170, button_1.rect.top-40, 130, 20, screen, False)
# test_block3 = Block(170, button_1.rect.top-40, 20, 100, screen, False)
# test_block4 = Block(270, button_1.rect.top-40, 20, 100, screen, False)
# hole = Hole(50,50, 55, 55, screen)
level1= Level1(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt)
level2= Level2(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block)
level3= Level3(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, Sand)
level3.create_objects()
# level_editor = Level_Editor(mouse_pos, screen, w, h, Golf_Ball, Button, Hole, Block, dt)
# level_editor.level_edit_mode()
while running:
  #Event Loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:

      key = event.key
      if event.key == pygame.K_ESCAPE:
          running = False


  #Time increase

  mouse_pos = pygame.mouse.get_pos()

  screen.fill('White')

  grass = pygame.draw.rect(screen, 'Green', ((0+10, 0+10),(w-20, h-20)))

  level3.update()
  golf_ball.update(mouse_pos, dt)


  #level1.update()
  #level2.update()


  fired = False
  dt = clock.tick(70) / 1000

  clock.tick(70)
  print(clock.get_fps())
  pygame.display.flip()