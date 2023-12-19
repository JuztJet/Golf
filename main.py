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

pygame.init()  # Starting Pygame


#screen = pygame.display.set_mode((1000,700))  # Main windows called screen
screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])  # Main windows called screen
window_w, window_h = pygame.display.get_desktop_sizes()[0]
w, h = (window_w/2-(350-20)/2)+10, (window_h/2-(570-20)/2)+10  # Getting width height
box_w, box_h = 330, 550
background_rect1 = pygame.Rect((0,0), (w, window_h))
background_rect2 = pygame.Rect((w+box_w,0), (w, window_h))

running = True
clock = pygame.time.Clock()
mouse_pos = pygame.mouse.get_pos()
dt = clock.tick(70) / 1000
time = 0  # Setting up a Time variable

golf_ball = Golf_Ball(-3.5, w+box_w * .5, h+box_h * .8, "White", 0.04593, dt, box_w, box_h, mouse_pos, screen,w, h)

counter = 5
level1 = Level1(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand, time)  # Instantiating class called Level 2
level2 = Level2(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand)  # Instantiating class called Level 2
level3 = Level3(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand)  # Instantiating class called Level 2
level4 = Level4(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand)  # Instantiating class called Level 2
level5 = Level5(golf_ball, Button, Hole, mouse_pos, screen, w, h, dt, Block, box_w, box_h, slope, power_up, water, corner_block, Sand, time)  # Instantiating class called Level 2

grass = pygame.transform.smoothscale(pygame.image.load('Assets/grass.png').convert_alpha(), (box_w,box_h))
level1.create_objects()
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
        elif event.type == pygame.KEYDOWN:

            key = event.key
            if event.key == pygame.K_ESCAPE:
                running = False

    time += 2 * dt  # Time increase
    mouse_pos = pygame.mouse.get_pos()  # Updating mouse position
    screen.fill((107, 201, 97))


    #grass = pygame.draw.rect(screen, 'Green', ((w, h), (box_w, box_h))) # Creating and drawing a grass
    screen.blit(grass, (w, h))
    # background

    # level3.update()


    # level2.update(time, clock.get_fps())  # Updating level 2
    #level3.update(time, clock.get_fps())  # Updating level 3
    #level4.update(time, clock.get_fps())  # Updating level 4
    #print(counter)
    if golf_ball.visible == False:
        golf_ball.initial_vel = 0
        golf_ball.x_pos = w+box_w * .5
        golf_ball.y_pos = h+box_h * .8
        golf_ball.rect.centerx = golf_ball.x_pos
        golf_ball.rect.centery = golf_ball.y_pos
        golf_ball.visible = True
        golf_ball.shoot = False
        counter += 1
    #print(2, golf_ball.rect.centerx, golf_ball.rect.centery,counter, golf_ball.initial_vel, golf_ball.shoot, mouse_pos)
    if counter == 1:
        pass


    if counter == 1:
        level1.update(time, clock.get_fps())  # Updating level 4
    elif counter == 2:
        level2.update(time, clock.get_fps())  # Updating level 4
    elif counter == 3:
        level3.update(time, clock.get_fps())  # Updating level 4
    elif counter == 4:
        level4.update(time, clock.get_fps())  # Updating level 4
    elif counter == 5:
        level5.update(time, clock.get_fps())  # Updating level 4
    pygame.draw.rect(screen, (107, 201, 97), background_rect1)
    pygame.draw.rect(screen, (107, 201, 97), background_rect2)
    golf_ball.update(mouse_pos, dt)  # Updating the golf ball instance
    #print(golf_ball.rect.x, golf_ball.rect.centerx, golf_ball.angle, golf_ball.initial_vel)
    dt = clock.tick(70) / 1000
    clock.tick(70)
    pygame.display.flip()