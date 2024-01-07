# Import
import pygame

# Getting necessary classes from files in folder called Classes
from Classes.Golf_Ball_Class import Golf_Ball
from Classes.Button_class import Button
from Classes.Block_class import Block
from Classes.Hole_class import Hole
from Classes.Level_Editor_Class import Level_Editor
from Classes.Level_1 import Level1
from Classes.Level_2 import Level2
from Classes.Level_3 import Level3
from Classes.Level_4 import Level4
from Classes.Level_5 import Level5
from Classes.Sand_class import Sand
from Classes.Slope_class import slope
from Classes.power_up import power_up
from Classes.Water_class import water
from Classes.Corner_Block_Class import corner_block
from Classes.home import home

pygame.init()  # Starting Pygame
#screen = pygame.display.set_mode((1300,900))  # Main windows called screen
screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])  # Main windows called screen
window_w, window_h = pygame.display.get_desktop_sizes()[0]
print(pygame.display.get_desktop_sizes()[0])
w, h = (window_w/2-(350-20)/2)+10, (window_h/2-(570-20)/2)+10  # Getting width height
box_w, box_h = 330, 550
pygame.key.set_repeat(100)

background_rect1 = pygame.Rect((0,0), (w, window_h))
background_rect2 = pygame.Rect((w+box_w,0), (w, window_h))

running = True
clock = pygame.time.Clock()
mouse_pos = pygame.mouse.get_pos()
dt = clock.tick(70) / 1000
time = 0
counter = 1

golf_ball = Golf_Ball(-3.5, w+box_w * .5, h+box_h * .8, "White", 0.04593, dt, box_w, box_h, mouse_pos, screen,w, h)
grass = pygame.transform.smoothscale(pygame.image.load('Assets/grass.png').convert_alpha(), (box_w,box_h))
home = home(screen, window_w, window_h)
level_num, game, home_screen = 0, False, True

level1 = Level1(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand, time)  # Instantiating class called Level 2
level2 = Level2(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand)  # Instantiating class called Level 2
level3 = Level3(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand)  # Instantiating class called Level 2
level4 = Level4(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand)  # Instantiating class called Level 2
level5 = Level5(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand, time)  # Instantiating class called Level 2
level1.create_objects()  # Running method inside Level 1 which will create the objects (eg Blocks, golf hole)
level2.create_objects()  # Running method inside Level 2 which will create the objects (eg Blocks, golf hole)
level3.create_objects()  # Running method inside Level 3 which will create the objects (eg Blocks, golf hole)
level4.create_objects()  # Running method inside Level 3 which will create the objects (eg Blocks, golf hole)
level5.create_objects()  # Running method inside Level 3 which will create the objects (eg Blocks, golf hole)


# Pygame Loop
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif home.login_text_clicked:
                if event.type == pygame.TEXTINPUT:
                    home.add_text_to_username(event.text)
                elif pygame.key.get_focused():
                    home.add_text_to_username(None)
        elif event.type == pygame.KEYDOWN:

            key = event.key
            if event.key == pygame.K_ESCAPE:
                running = False

    time += 2 * dt  # Time increase
    mouse_pos = pygame.mouse.get_pos()  # Updating mouse position
    if game:
        screen.fill('#74C850')
        screen.blit(grass, (w, h))

        if golf_ball.visible == False:
            golf_ball.initial_vel = 0
            golf_ball.x_pos = w+box_w * .5
            golf_ball.y_pos = h+box_h * .8
            golf_ball.rect.centerx = golf_ball.x_pos
            golf_ball.rect.centery = golf_ball.y_pos
            golf_ball.visible = True
            golf_ball.shoot = False
            level_num += 1



        if level_num == 1:
            level1.update(time, clock.get_fps())  # Updating level 1
        elif level_num == 2:
            level2.update(time, clock.get_fps())  # Updating level 2
        elif level_num == 3:
            level3.update(time, clock.get_fps())  # Updating level 3
        elif level_num == 4:
            level4.update(time, clock.get_fps())  # Updating level 4
        elif level_num == 5:
            level5.update(time, clock.get_fps())  # Updating level 5

        pygame.draw.rect(screen, '#74C850', background_rect1)
        pygame.draw.rect(screen, '#74C850', background_rect2)

        golf_ball.update(mouse_pos, dt)  # Updating the golf ball instance
    if home_screen:
        screen.fill('#7ED957')
        level_num, game, home_screen = home.update(mouse_pos)

    dt = clock.tick(70) / 1000
    clock.tick(70)
    pygame.display.flip()